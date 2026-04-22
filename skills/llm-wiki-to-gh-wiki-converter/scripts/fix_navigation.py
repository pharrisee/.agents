#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def fix_navigation(filepath, wiki_root):
    """Fix navigation section display text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match navigation lines with ../ prefix in display text
    # Example: - [../README.md](../README.md)
    # Replace with: - [README.md](../README.md)
    lines = content.split('\n')
    new_lines = []
    changed = False
    
    for line in lines:
        # Match navigation lines with ../ in brackets
        if line.strip().startswith('- [') and '../' in line:
            # Use regex to remove ../ from display text only
            new_line = re.sub(r'(\[)\.\./([^]]+\])(\([^)]+\))', r'[\2\3', line)
            if new_line != line:
                line = new_line
                changed = True
        new_lines.append(line)
    
    if changed:
        new_content = '\n'.join(new_lines)
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
        # Skip raw directory
        if 'raw' in root.split(os.sep):
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    
    fixed_count = 0
    for filepath in md_files:
        if fix_navigation(filepath, wiki_dir):
            fixed_count += 1
            print(f"Fixed navigation in: {filepath.relative_to(wiki_dir)}")
    
    print(f"\nFixed navigation in {fixed_count} files")

if __name__ == '__main__':
    main()