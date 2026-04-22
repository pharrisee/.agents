#!/usr/bin/env python3
import os
import re
import sys
import glob

def convert_markdown_link(match):
    """Convert a markdown link to wikilink."""
    display = match.group(1)
    url = match.group(2)
    
    url = url.rstrip('.md')
    
    if display == url:
        return f'[[{url}]]'
    else:
        return f'[[{url}|{display}]]'

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    new_content = re.sub(pattern, convert_markdown_link, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <wiki-directory>")
        sys.exit(1)
    
    wiki_dir = sys.argv[1]
    raw_files = glob.glob(f'{wiki_dir}/raw/**/*.md', recursive=True)
    for filepath in raw_files:
        if convert_file(filepath):
            print(f"Converted: {filepath}")