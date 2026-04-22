#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def fix_relative_links(wiki_path):
    """Fix relative links that are missing ../ prefix for cross-directory links."""
    wiki_path = Path(wiki_path)
    
    dirs = ['sources', 'concepts', 'entities', 'syntheses', 'analyses', 'meta', 'references']
    
    # Map filenames to their directories
    file_to_dir = {}
    for dir_name in dirs:
        dir_path = wiki_path / dir_name
        if dir_path.exists():
            for md_file in dir_path.glob('*.md'):
                file_to_dir[md_file.stem] = dir_name
                file_to_dir[f'{dir_name}/{md_file.stem}'] = dir_name
    
    fixed_count = 0
    
    for dir_name in dirs:
        dir_path = wiki_path / dir_name
        if not dir_path.exists():
            continue
            
        for md_file in dir_path.glob('*.md'):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_lines = []
            changed = False
            
            for line in content.split('\n'):
                def replace_link(match):
                    nonlocal changed
                    display = match.group(1)
                    url = match.group(2)
                    
                    # Skip external links
                    if url.startswith('http') or url.startswith('#'):
                        return match.group(0)
                    
                    # Skip links that already have ../ or ./
                    if url.startswith('../') or url.startswith('./'):
                        return match.group(0)
                    
                    # Get target filename without extension
                    target_name = url.replace('.md', '')
                    
                    # Check if target exists
                    if target_name in file_to_dir:
                        target_dir = file_to_dir[target_name]
                        
                        if target_dir == dir_name:
                            # Same directory - just use filename
                            new_url = f'{target_name.split("/")[-1]}.md'
                            if new_url != url:
                                changed = True
                                return f'[{display}]({new_url})'
                        else:
                            # Different directory - need ../
                            new_url = f'../{target_dir}/{target_name.split("/")[-1]}.md'
                            changed = True
                            return f'[{display}]({new_url})'
                    
                    return match.group(0)
                
                new_line = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', replace_link, line)
                new_lines.append(new_line)
            
            if changed:
                new_content = '\n'.join(new_lines)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_count += 1
                print(f"Fixed: {md_file.relative_to(wiki_path)}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <wiki-directory>")
        sys.exit(1)
    
    fix_relative_links(sys.argv[1])