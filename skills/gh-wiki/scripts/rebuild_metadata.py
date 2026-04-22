#!/usr/bin/env python3
"""
Metadata Rebuild Script for LLM Wiki
Rebuilds registry.json, backlinks.json, index.md, log.md from wiki contents
Usage: python3 scripts/rebuild_metadata.py [wiki-path]
"""
import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timezone

def extract_frontmatter(filepath):
    """Extract frontmatter from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return {}
    
    if not content.startswith('---'):
        return {}
    
    # Find end of frontmatter
    lines = content.split('\n')
    frontmatter_lines = []
    in_frontmatter = False
    first_line = True
    
    for line in lines:
        if line.strip() == '---':
            if first_line:
                in_frontmatter = True
                first_line = False
                continue
            else:
                break
        if in_frontmatter:
            frontmatter_lines.append(line)
    
    # Parse frontmatter
    frontmatter = {}
    for line in frontmatter_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value
    
    return frontmatter

def extract_outgoing_links(filepath):
    """Extract wikilinks from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []
    
    # Find all [[links]]
    pattern = r'\[\[([^\]]+)\]\]'
    links = re.findall(pattern, content)
    return links

def rebuild_metadata(wiki_path):
    """Rebuild all metadata files."""
    wiki_path = Path(wiki_path)
    meta_dir = wiki_path / 'meta'
    meta_dir.mkdir(exist_ok=True)
    
    print(f"Rebuilding metadata in: {wiki_path}")
    
    # Directories to scan
    dirs = ['sources', 'concepts', 'entities', 'syntheses', 'analyses']
    
    # Collect all pages
    pages = []
    for dir_name in dirs:
        dir_path = wiki_path / dir_name
        if dir_path.exists():
            for md_file in dir_path.glob('*.md'):
                frontmatter = extract_frontmatter(md_file)
                links = extract_outgoing_links(md_file)
                
                page = {
                    'path': str(md_file.relative_to(wiki_path)),
                    'title': frontmatter.get('title', md_file.stem),
                    'type': frontmatter.get('type', 'unknown'),
                    'status': frontmatter.get('status', 'unknown'),
                    'modified': frontmatter.get('modified', 'unknown'),
                    'outgoing_links': links
                }
                pages.append(page)
    
    # Build registry.json
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    registry = {
        'version': '1.0.0',
        'generated': timestamp,
        'pages': pages
    }
    
    registry_file = meta_dir / 'registry.json'
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)
    print(f"  - meta/registry.json: {len(pages)} pages")
    
    # Build backlinks.json
    backlinks = {}
    for page in pages:
        backlinks[page['path']] = []
    
    for page in pages:
        for link in page.get('outgoing_links', []):
            # Try to find target page
            target_path = link + '.md'
            if link.count('/') == 0:
                # Simple name - check all dirs
                for dir_name in dirs:
                    possible = f"{dir_name}/{link}.md"
                    if possible in backlinks:
                        if page['path'] not in backlinks[possible]:
                            backlinks[possible].append(page['path'])
            else:
                # Folder-qualified
                if target_path in backlinks:
                    if page['path'] not in backlinks[target_path]:
                        backlinks[target_path].append(page['path'])
    
    backlinks_file = meta_dir / 'backlinks.json'
    with open(backlinks_file, 'w', encoding='utf-8') as f:
        json.dump(backlinks, f, indent=2)
    print(f"  - meta/backlinks.json: built")
    
    # Rebuild index.md
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    index_lines = [
        "# Wiki Index",
        "",
        f"Generated: {timestamp}",
        "",
        f"## Statistics",
        f"- Total pages: {len(pages)}",
        ""
    ]
    
    for dir_name in dirs:
        dir_path = wiki_path / dir_name
        if dir_path.exists():
            md_files = sorted(dir_path.glob('*.md'))
            if md_files:
                count = len(list(md_files))
                index_lines.append(f"## {dir_name.capitalize()} ({count})")
                index_lines.append("")
                for md_file in md_files:
                    frontmatter = extract_frontmatter(md_file)
                    title = frontmatter.get('title', md_file.stem)
                    rel_path = md_file.relative_to(wiki_path)
                    # Use Markdown links for gh-wiki format
                    index_lines.append(f"- [{title}]({rel_path})")
                index_lines.append("")
    
    index_file = meta_dir / 'index.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))
    print(f"  - meta/index.md: updated")
    
    # Rebuild log.md from events.jsonl
    log_lines = [
        "# Wiki Activity Log",
        "",
        f"Generated: {timestamp}",
        ""
    ]
    
    events_file = meta_dir / 'events.jsonl'
    if events_file.exists():
        with open(events_file, 'r', encoding='utf-8') as f:
            events = f.readlines()
        
        if events:
            log_lines.append("")
            for event in reversed(events):
                event = event.strip()
                if event:
                    log_lines.append(f"- {event}")
        else:
            log_lines.append("")
            log_lines.append("No events recorded yet.")
    else:
        log_lines.append("")
        log_lines.append("No events recorded yet.")
    
    log_file = meta_dir / 'log.md'
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log_lines))
    print(f"  - meta/log.md: updated")
    
    # Update last-rebuild timestamp
    wiki_dir = wiki_path / '.wiki'
    wiki_dir.mkdir(exist_ok=True)
    last_rebuild = {
        'timestamp': timestamp,
        'pages_indexed': len(pages)
    }
    with open(wiki_dir / 'last-rebuild.json', 'w', encoding='utf-8') as f:
        json.dump(last_rebuild, f, indent=2)
    
    print("Metadata rebuild complete.")

def main():
    if len(sys.argv) < 2:
        wiki_path = '.'
    else:
        wiki_path = sys.argv[1]
    
    if not Path(wiki_path).exists():
        print(f"Error: Directory not found: {wiki_path}")
        sys.exit(1)
    
    rebuild_metadata(wiki_path)

if __name__ == '__main__':
    main()