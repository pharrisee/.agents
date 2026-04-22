#!/usr/bin/env python3
import os
import re
import sys

def convert_wikilink(match):
    wikilink = match.group(1)
    if '/' in wikilink:
        parts = wikilink.split('/')
        folder = '/'.join(parts[:-1])
        page = parts[-1]
        return f'[{page}]({folder}/{page}.md)'
    else:
        return f'[{wikilink}]({wikilink}.md)'

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\[\[([^]]+)\]\]'
    new_content = re.sub(pattern, convert_wikilink, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    import glob
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <wiki-directory>")
        sys.exit(1)
    
    wiki_dir = sys.argv[1]
    raw_files = glob.glob(f'{wiki_dir}/raw/**/*.md', recursive=True)
    for filepath in raw_files:
        if convert_file(filepath):
            print(f"Converted: {filepath}")