#!/bin/bash
# Metadata Rebuild Script for LLM Wiki
# Rebuilds registry.json, backlinks.json, index.md, log.md from wiki contents
# Usage: ./scripts/rebuild-metadata.sh [wiki-path]

WIKI_PATH="${1:-.}"
cd "$WIKI_PATH" || exit 1

echo "Rebuilding metadata in: $(pwd)"

# Ensure meta directory exists
mkdir -p meta

# Build registry.json from all markdown files
cat > meta/registry.json << 'REGISTRY_HEADER'
{
  "version": "1.0.0",
  "generated": "REGISTRY_DATE",
  "pages": [
REGISTRY_HEADER

REGISTRY_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
sed -i "s/REGISTRY_DATE/$REGISTRY_DATE/" meta/registry.json

# Find all wiki pages (excluding raw/ and meta/)
FIRST=true
find sources concepts entities syntheses analyses -name "*.md" 2>/dev/null | while read -r file; do
    [ -f "$file" ] || continue
    
    # Extract frontmatter
    if head -1 "$file" | grep -q "^---"; then
        # Parse frontmatter
        title=$(grep "^title:" "$file" | head -1 | sed 's/title: *//; s/^"//; s/"$//')
        type=$(grep "^type:" "$file" | head -1 | sed 's/type: *//')
        status=$(grep "^status:" "$file" | head -1 | sed 's/status: *//')
        modified=$(grep "^modified:" "$file" | head -1 | sed 's/modified: *//')
        
        # Extract outgoing links
        links=$(grep -oE '\[\[[^\]]+\]\]' "$file" | tr '\n' ',' | sed 's/,$//')
        
        # Add to registry
        if [ "$FIRST" = true ]; then
            FIRST=false
        else
            echo "," >> meta/registry.json
        fi
        
        cat >> meta/registry.json << PAGE_ENTRY
    {
      "path": "$file",
      "title": "${title:-$file}",
      "type": "${type:-unknown}",
      "status": "${status:-unknown}",
      "modified": "${modified:-unknown}",
      "outgoing_links": [${links:+"$links"}]
    }
PAGE_ENTRY
    fi
done

# Close registry.json
echo "" >> meta/registry.json
echo "  ]" >> meta/registry.json
echo "}" >> meta/registry.json

# Build backlinks.json
echo "Building backlinks..."
node > meta/backlinks.json << 'NODE_SCRIPT'
const fs = require('fs');

const registry = JSON.parse(fs.readFileSync('meta/registry.json', 'utf8'));
const backlinks = {};

// Initialize empty arrays for all pages
registry.pages.forEach(p => {
  backlinks[p.path] = [];
});

// Build reverse index
registry.pages.forEach(source => {
  if (source.outgoing_links && source.outgoing_links.length > 0) {
    source.outgoing_links.forEach(target => {
      // Extract target path from [[...]]
      const clean = target.replace(/\[\[|\]\]/g, '');
      // Check if target exists in registry
      const found = registry.pages.find(p => 
        p.path === clean || 
        p.path === clean + '.md' ||
        p.title === clean
      );
      if (found && found.path !== source.path) {
        if (!backlinks[found.path].includes(source.path)) {
          backlinks[found.path].push(source.path);
        }
      }
    });
  }
});

console.log(JSON.stringify(backlinks, null, 2));
NODE_SCRIPT

# Regenerate index.md
echo "Regenerating index.md..."
cat > meta/index.md << INDEX_HEADER
# Wiki Index

Generated: $(date -u +"%Y-%m-%d %H:%M UTC")

## Statistics
- Total pages: $(find sources concepts entities syntheses analyses -name "*.md" 2>/dev/null | wc -l)

INDEX_HEADER

# Group by type
for dir in sources concepts entities syntheses analyses; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -name "*.md" | wc -l)
        echo "" >> meta/index.md
        echo "## ${dir^} ($count)" >> meta/index.md
        echo "" >> meta/index.md
        find "$dir" -name "*.md" | sort | while read -r f; do
            title=$(grep "^title:" "$f" 2>/dev/null | head -1 | sed 's/title: *//; s/^"//; s/"$//' || echo "$f")
            echo "- [[${f%.md}]] — $title" >> meta/index.md
        done
    fi
done

# Regenerate log.md from events.jsonl
echo "Regenerating log.md..."
cat > meta/log.md << LOG_HEADER
# Wiki Activity Log

Generated: $(date -u +"%Y-%m-%d %H:%M UTC")

LOG_HEADER

if [ -f meta/events.jsonl ]; then
    echo "" >> meta/log.md
    tac meta/events.jsonl | while read -r line; do
        echo "- $line" >> meta/log.md
    done
else
    echo "No events recorded yet." >> meta/log.md
fi

# Update last-rebuild timestamp
node > .wiki/last-rebuild.json << EOF
console.log(JSON.stringify({
  timestamp: new Date().toISOString(),
  pages_indexed: $(find sources concepts entities syntheses analyses -name "*.md" 2>/dev/null | wc -l)
}, null, 2));
EOF

echo "Metadata rebuild complete."
echo "  - meta/registry.json: $(grep -c '"path"' meta/registry.json || echo 0) pages"
echo "  - meta/index.md: updated"
echo "  - meta/log.md: updated"
