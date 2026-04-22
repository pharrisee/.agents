#!/usr/bin/env python3
import os
import re
import sys
import json
from pathlib import Path

def convert_markdown_link(match):
    """Convert a markdown link to wikilink."""
    display = match.group(1)  # text in [...]
    url = match.group(2)      # URL in (...)
    
    # Remove .md extension from URL
    url = url.rstrip('.md')
    
    # Handle display text vs URL
    if display == url:
        # Display matches URL (like [page-name](page-name)), use simple [[page-name]]
        return f'[[{url}]]'
    else:
        # Display differs from URL (like [display](folder/page)), use [[folder/page|display]]
        return f'[[{url}|{display}]]'

def convert_file(filepath):
    """Convert markdown links in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match [display](folder/page.md) but NOT external links
    # Only match .md links
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    
    # Replace all markdown links
    new_content = re.sub(pattern, convert_markdown_link, content)
    
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
    if not wiki_dir.exists():
        print(f"Directory not found: {wiki_dir}")
        sys.exit(1)
    
    # Find all .md files except in raw/ directory
    md_files = []
    for root, dirs, files in os.walk(wiki_dir):
        if 'raw' in root.split(os.sep):
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    
    print(f"Found {len(md_files)} markdown files")
    
    converted_count = 0
    for filepath in md_files:
        if convert_file(filepath):
            converted_count += 1
            print(f"Converted: {filepath.relative_to(wiki_dir)}")
    
    print(f"\nConversion complete: {converted_count} files modified")
    
    # Update SCHEMA.md linking conventions
    schema_file = wiki_dir / 'SCHEMA.md'
    if schema_file.exists():
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_content = f.read()
        
        # Update linking examples
        schema_content = schema_content.replace(
            '- Internal: `[api-testing](concepts/api-testing.md)` (folder-qualified)',
            '- Internal: `[[concepts/api-testing]]` (folder-qualified)'
        )
        schema_content = schema_content.replace(
            '- Citations: `[SRC-2026-04-22-001](sources/SRC-2026-04-22-001.md)` (source ID)',
            '- Citations: `[[sources/SRC-2026-04-22-001]]` (source ID)'
        )
        schema_content = schema_content.replace(
            '`[SRC-2026-04-22-001](sources/SRC-2026-04-22-001.md)`',
            '`[[sources/SRC-2026-04-22-001]]`'
        )
        schema_content = schema_content.replace(
            '`[api-testing](concepts/api-testing.md)`',
            '`[[concepts/api-testing]]`'
        )
        schema_content = schema_content.replace(
            '`[postman](entities/postman.md)`',
            '`[[entities/postman]]`'
        )
        schema_content = schema_content.replace(
            '`[pricing-comparison](syntheses/pricing-comparison.md)`',
            '`[[syntheses/pricing-comparison]]`'
        )
        
        with open(schema_file, 'w', encoding='utf-8') as f:
            f.write(schema_content)
        print("Updated SCHEMA.md linking conventions")
    
    # Update .wiki/config.json format flag if exists
    config_file = wiki_dir / '.wiki' / 'config.json'
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        config['format'] = 'llm-wiki'
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print("Updated .wiki/config.json format flag")

if __name__ == '__main__':
    main()