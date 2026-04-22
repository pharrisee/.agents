#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def add_navigation(filepath, wiki_root):
    """Add navigation section to a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has Navigation section
    if '## Navigation' in content:
        return False
    
    # Determine relative path to root
    rel_path = filepath.parent.relative_to(wiki_root)
    if rel_path == Path('.'):
        prefix = ''
    else:
        # For files in subdirectories, need to go up
        prefix = '../' * len(rel_path.parts)
    
    navigation_section = '\n\n## Navigation\n'
    navigation_section += f'- [{prefix}README.md]({prefix}README.md) - Wiki overview and table of contents\n'
    navigation_section += f'- [{prefix}SCHEMA.md]({prefix}SCHEMA.md) - Wiki conventions and rules\n'
    navigation_section += f'- [{prefix}meta/index.md]({prefix}meta/index.md) - Catalog of all pages\n'
    
    # Append navigation section before any trailing raw packet line
    # or at the end of file
    new_content = content.rstrip() + navigation_section
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <wiki-directory>")
        sys.exit(1)
    
    wiki_dir = Path(sys.argv[1])
    
    # Files to process: all .md files in specific directories
    dirs_to_process = ['sources', 'concepts', 'entities', 'syntheses', 'analyses', 'meta', 'references']
    
    md_files = []
    for dir_name in dirs_to_process:
        dir_path = wiki_dir / dir_name
        if dir_path.exists():
            for file in dir_path.glob('*.md'):
                md_files.append(file)
    
    # Also process root .md files except README.md and SCHEMA.md (they already have navigation)
    for file in wiki_dir.glob('*.md'):
        if file.name not in ['README.md', 'SCHEMA.md']:
            md_files.append(file)
    
    print(f"Found {len(md_files)} markdown files to process")
    
    added_count = 0
    for filepath in md_files:
        if add_navigation(filepath, wiki_dir):
            added_count += 1
            print(f"Added navigation to: {filepath.relative_to(wiki_dir)}")
    
    print(f"\nNavigation added to {added_count} files")

if __name__ == '__main__':
    main()