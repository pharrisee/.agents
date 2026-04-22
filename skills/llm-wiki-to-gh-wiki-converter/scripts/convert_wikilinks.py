#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def convert_wikilink(match):
    """Convert a wikilink to markdown link."""
    wikilink = match.group(1)  # content inside [[...]]
    
    # Handle [[folder/page]] pattern
    if '/' in wikilink:
        # Split into folder and page
        parts = wikilink.split('/')
        folder = '/'.join(parts[:-1])
        page = parts[-1]
        # Create markdown link: [page](folder/page.md)
        return f'[{page}]({folder}/{page}.md)'
    else:
        # Simple [[page]] -> [page](page.md)
        return f'[{wikilink}]({wikilink}.md)'

def convert_file(filepath):
    """Convert wikilinks in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match [[...]] but not inside code blocks
    # Simple regex for now, assuming no nested brackets
    pattern = r'\[\[([^]]+)\]\]'
    
    # Replace all wikilinks
    new_content = re.sub(pattern, convert_wikilink, content)
    
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
        # Skip raw directory
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
    
    # Also need to update SCHEMA.md linking conventions
    schema_file = wiki_dir / 'SCHEMA.md'
    if schema_file.exists():
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_content = f.read()
        
        # Update linking examples
        schema_content = schema_content.replace(
            '- Internal: `[[concepts/api-testing]]` (folder-qualified)',
            '- Internal: `[api-testing](concepts/api-testing.md)` (folder-qualified with .md extension)'
        )
        schema_content = schema_content.replace(
            '- Citations: `[[sources/SRC-2026-04-22-001]]` (source ID)',
            '- Citations: `[SRC-2026-04-22-001](sources/SRC-2026-04-22-001.md)` (source ID)'
        )
        schema_content = schema_content.replace(
            '`[[sources/SRC-2026-04-22-001]]`',
            '`[SRC-2026-04-22-001](sources/SRC-2026-04-22-001.md)`'
        )
        schema_content = schema_content.replace(
            '`[[concepts/api-testing]]`',
            '`[api-testing](concepts/api-testing.md)`'
        )
        schema_content = schema_content.replace(
            '`[[entities/postman]]`',
            '`[postman](entities/postman.md)`'
        )
        schema_content = schema_content.replace(
            '`[[syntheses/pricing-comparison]]`',
            '`[pricing-comparison](syntheses/pricing-comparison.md)`'
        )
        
        with open(schema_file, 'w', encoding='utf-8') as f:
            f.write(schema_content)
        print("Updated SCHEMA.md linking conventions")
    
    # Create or update README.md
    readme_file = wiki_dir / 'README.md'
    if not readme_file.exists():
        # Create from template
        readme_content = """# Wiki Overview

Welcome to this knowledge wiki! This wiki follows a structured approach to capturing and synthesizing information from various sources.

## Quick Start

1. **Browse content**: Use the table of contents below or explore directories
2. **Add a source**: Capture URLs, files, or text to create source pages
3. **Integrate knowledge**: Connect sources to concepts, entities, and syntheses
4. **Query**: Ask questions based on accumulated knowledge

## Table of Contents

### Core Directories
- [sources/](sources/) - Individual source summaries
- [concepts/](concepts/) - Concept definitions and explanations  
- [entities/](entities/) - Facts about specific things (people, orgs, products)
- [syntheses/](syntheses/) - Cross-source analyses and tensions
- [analyses/](analyses/) - Durable answers to specific questions

### Supporting Files
- [SCHEMA.md](SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](meta/index.md) - Generated catalog of all pages
- [meta/lint-report.md](meta/lint-report.md) - Wiki health report

## How This Wiki Works

This wiki uses a **source-first** approach:

1. **Capture**: Sources are captured with unique IDs (SRC-YYYY-MM-DD-NNN)
2. **Summarize**: Each source gets a summary page in `sources/`
3. **Integrate**: Source claims are woven into canonical pages
4. **Synthesize**: Conflicting or related information is analyzed in synthesis pages

## Linking Conventions

- Internal links: `[page-name](folder/page-name.md)`
- Source citations: `[SRC-2026-04-01](sources/SRC-2026-04-01.md)`
- External links: `[text](https://example.com)`

## Maintenance

- **Audit**: Run periodic health checks to find broken links, orphans, stale content
- **Rebuild metadata**: Regenerate indexes after batch changes
- **Backup**: Keep regular backups of the wiki directory

## Getting Help

For questions about using this wiki, refer to:
- [SCHEMA.md](SCHEMA.md) for detailed conventions
- The wiki tool's documentation for operational guidance

---

*This wiki was initialized on 2026-04-22 using the gh-wiki pattern.*
"""
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("Created README.md")
    else:
        # Convert any wikilinks in existing README.md
        convert_file(readme_file)
        print("Updated README.md")
    
    # Update .wiki/config.json format flag if exists
    config_file = wiki_dir / '.wiki' / 'config.json'
    if config_file.exists():
        import json
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        config['format'] = 'gh-wiki'
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print("Updated .wiki/config.json format flag")

if __name__ == '__main__':
    main()