#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def remove_navigation_section(filepath):
    """Remove navigation section from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation section exists
    if '## Navigation' not in content:
        return False
    
    # Split content into lines
    lines = content.split('\n')
    new_lines = []
    in_navigation = False
    skip_remaining = False
    
    for i, line in enumerate(lines):
        # Skip empty lines before navigation section when we encounter it
        if line.strip() == '## Navigation':
            in_navigation = True
            skip_remaining = True
            # Don't add this line or subsequent navigation content
            continue
        
        # Skip lines until we hit a new top-level heading or end
        if in_navigation:
            if line.startswith('# ') or (line.startswith('## ') and not line.startswith('## Navigation')):
                # Found a new section heading
                in_navigation = False
                new_lines.append(line)
            # Skip all other lines in navigation section
            continue
        
        new_lines.append(line)
    
    # Remove trailing whitespace
    new_content = '\n'.join(new_lines).rstrip() + '\n'
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <wiki-directory>")
        sys.exit(1)
    
    wiki_dir = Path(sys.argv[1])
    
    # Find all .md files with navigation sections
    md_files = []
    for root, dirs, files in os.walk(wiki_dir):
        if 'raw' in root.split(os.sep):
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    
    removed_count = 0
    for filepath in md_files:
        if remove_navigation_section(filepath):
            removed_count += 1
            print(f"Removed navigation from: {filepath.relative_to(wiki_dir)}")
    
    print(f"\nRemoved navigation from {removed_count} files")

if __name__ == '__main__':
    main()