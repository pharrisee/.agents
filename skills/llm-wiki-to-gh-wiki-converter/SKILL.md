---
name: llm-wiki-to-gh-wiki-converter
description: Use this skill when the user wants to convert an existing llm-wiki (Obsidian vault format) to gh-wiki (GitHub Markdown format). Provides tools and workflows for migrating wikilinks to standard Markdown links and updating wiki conventions.
---

# LLM Wiki to GitHub Wiki Converter Skill

Skill for converting an existing llm-wiki (using Obsidian-style wikilinks) to gh-wiki (using standard GitHub Markdown links). Handles link conversion, schema updates, and configuration migration.

## When to Use This Skill

- **Migration**: User has an existing llm-wiki vault and wants to convert it to GitHub Markdown format
- **Partial conversion**: User wants to convert specific files or directories
- **Validation**: Check if a wiki is already in gh-wiki format or needs conversion
- **Batch processing**: Convert multiple files with wikilinks to standard Markdown links

## Non-Negotiable Rules

1. **Always backup first** — Never modify source files without backup option
2. **Dry-run by default** — Show what would change before making changes
3. **Preserve frontmatter** — Keep all YAML frontmatter intact
4. **Handle edge cases** — Report on links that can't be automatically converted
5. **Update schema** — Ensure SCHEMA.md reflects GitHub Markdown conventions after conversion

## Startup Protocol

When this skill activates:

1. **Check for wiki**: Look for `SCHEMA.md` or `.wiki/config.json` in current directory or specified path
2. **Determine format**: Check if wiki uses `[[wikilinks]]` (llm-wiki) or `[Markdown links](...)` (gh-wiki)
3. **Assess conversion scope**: Count files, estimate changes needed
4. **Present conversion plan**: Show user what will be changed
5. **Get confirmation**: Only proceed after user approval

## Workflows Overview

### Full Conversion
Convert entire wiki vault from llm-wiki to gh-wiki format.

### Partial Conversion  
Convert specific files or directories.

### Validation Check
Report on conversion readiness and potential issues.

### Schema Update
Update SCHEMA.md and config files for GitHub Markdown conventions.

## Conversion Rules

### Link Conversion Patterns

| From (llm-wiki) | To (gh-wiki) | Notes |
|-----------------|--------------|-------|
| `[[page-name]]` | `[page-name](page-name.md)` | Assumes same directory |
| `[[folder/page-name]]` | `[page-name](folder/page-name.md)` | Folder-qualified |
| `[[folder/page-name\|display]]` | `[display](folder/page-name.md)` | With display text |
| `[[sources/SRC-...]]` | `[SRC-...](sources/SRC-....md)` | Source citations |
| `[[concepts/...]]` | `[...](concepts/....md)` | Concept links |
| `[[entities/...]]` | `[...](entities/....md)` | Entity links |
| `[[syntheses/...]]` | `[...](syntheses/....md)` | Synthesis links |
| `[[analyses/...]]` | `[...](analyses/....md)` | Analysis links |
| `[[raw/...]]` | `[...](raw/....md)` | Raw file links |

### Frontmatter Updates
- Keep all existing frontmatter fields
- No changes needed to YAML structure
- Ensure `type`, `status`, `aliases` remain intact

### Schema Updates
- Update linking conventions in SCHEMA.md
- Update examples to use Markdown links
- Remove any Obsidian-specific references

### README.md Handling
- **If README.md exists**: Convert any wikilinks to Markdown links
- **If README.md doesn't exist**: Create using gh-wiki template after conversion
- **Navigation sections**: Ensure README.md includes proper table of contents and links
- **Root directory links**: Update relative paths in README.md (e.g., `[sources/](sources/)`)

## Tool Usage Patterns

### Checking for wikilinks
```bash
# Count wikilinks in a file
grep -o "\[\[[^]]*\]\]" file.md | wc -l

# Find all files with wikilinks
grep -r "\[\[.*\]\]" . --include="*.md" -l
```

### Dry-run conversion
```bash
# Show what would change
sed -n "s/\[\[\([^]|]*\)\|\([^]]*\)\]\]/[\2](\1.md)/gp" file.md
sed -n "s/\[\[\([^]]*\)\]\]/[\1](\1.md)/gp" file.md
```

### Actual conversion
```bash
# Convert wikilinks with display text
sed -i "s/\[\[\([^]|]*\)\|\([^]]*\)\]\]/[\2](\1.md)/g" file.md

# Convert simple wikilinks
sed -i "s/\[\[\([^]]*\)\]\]/[\1](\1.md)/g" file.md
```

### Backup before conversion
```bash
# Create backup directory
cp -r wiki/ wiki-backup-$(date +%Y%m%d-%H%M%S)/
```

### Using Python conversion scripts
```bash
# Full conversion using Python scripts
python3 scripts/convert_wikilinks.py /path/to/wiki
python3 scripts/convert_raw.py /path/to/wiki
python3 scripts/add_navigation.py /path/to/wiki
python3 scripts/fix_navigation.py /path/to/wiki

# Check for remaining wikilinks after conversion
grep -r "\[\[.*\]\]" /path/to/wiki --include="*.md" | wc -l
```

## Response Templates

### After Validation Check
```
## Wiki Format Analysis

**Location**: /path/to/wiki

**Format detected**: llm-wiki (Obsidian wikilinks)

**Statistics**:
- Total .md files: 42
- Files with wikilinks: 38 (90%)
- Total wikilinks: 215
- Estimated conversion time: < 1 minute

**Issues found**:
- 3 files have complex wikilinks with pipes `|` that need manual review
- SCHEMA.md references `[[wikilinks]]` conventions

**Recommendation**: Run full conversion with backup.
```

### After Dry-Run
```
## Conversion Preview

**Files to modify**: 38 files

**Sample changes**:

File: `concepts/attention.md`
- `[[sources/SRC-2026-04-01]]` → `[SRC-2026-04-01](sources/SRC-2026-04-01.md)`
- `[[entities/Transformer]]` → `[Transformer](entities/Transformer.md)`

File: `sources/SRC-2026-04-01.md`
- `[[concepts/attention]]` → `[attention](concepts/attention.md)`

**Total changes**: 215 link conversions

Proceed with conversion? (Yes/No/Backup first)
```

### After Successful Conversion
```
## Conversion Complete

**Location**: /path/to/wiki

**Statistics**:
- Files processed: 38
- Links converted: 215
- Backup created: wiki-backup-20260422-143022/

**Schema updated**:
- SCHEMA.md linking conventions updated
- .wiki/config.json format flag set to "gh-wiki"

**Next steps**:
1. Verify conversion with: `grep -r "\[\[" . --include="*.md"` (should return empty)
2. Test links in GitHub/GitLab viewer
3. Update git repository if version controlled
```

## Error Handling

| Issue | Resolution |
|-------|------------|
| Complex wikilinks with nested brackets | Flag for manual review, skip conversion |
| Broken links (target doesn't exist) | Report in conversion log, don't convert |
| Permission errors | Suggest running with appropriate permissions |
| Large wiki (>1000 files) | Batch processing, progress reporting |
| Mixed format (some files already converted) | Skip already converted files |

## Integration with Other Skills

This skill composes well with:
- **gh-wiki**: For working with the converted wiki
- **llm-wiki**: For understanding source format
- **file-operations**: For batch file processing

## Examples

### Example 1: Full Conversion
**User**: "Convert my llm-wiki at ~/research-wiki to gh-wiki format"

1. **Validation**: Check wiki format, count files
2. **Backup**: Create timestamped backup
3. **Conversion**: Process all .md files, convert wikilinks
4. **Schema update**: Update SCHEMA.md with GitHub Markdown conventions
5. **Verification**: Run check to ensure no wikilinks remain

### Example 2: Partial Conversion  
**User**: "Convert just the concepts/ directory in my wiki"

1. **Scope limitation**: Only process files in concepts/
2. **Dry-run**: Show changes for concepts/ files only
3. **Conversion**: Apply changes to specified directory
4. **Report**: Summary of converted files in concepts/

### Example 3: Validation Only
**User**: "Check if my wiki needs conversion to gh-wiki"

1. **Analysis**: Scan for wikilinks vs Markdown links
2. **Report**: Show percentage of files using each format
3. **Recommendation**: Suggest conversion if needed
4. **No changes made**: Read-only operation

## Limitations

### What This Skill Cannot Do

1. **No semantic link validation** — Doesn't verify that converted links work correctly
2. **No automatic fix for broken links** — Only converts format, doesn't create missing pages
3. **No support for Obsidian plugins** — Only handles basic wikilink syntax
4. **No bidirectional conversion** — Only converts from llm-wiki to gh-wiki, not reverse
5. **No image/attachment relocation** — Assumes same file structure

### Scope Boundaries

| In Scope | Out of Scope |
|----------|--------------|
| Wikilink to Markdown link conversion | Content rewriting |
| Schema convention updates | Adding new features |
| Format migration | Fixing broken links |
| Backup creation | Version control operations |
| Dry-run previews | Manual editing of complex cases |

## Troubleshooting

### Conversion Failed
**Symptom**: "Conversion failed with error"

**Causes & Fixes**:
1. Permission denied → Check file permissions, run with sudo if appropriate
2. Disk full → Check available space
3. Malformed wikilinks → Run validation first to identify problem files

### Partial Conversion
**Symptom**: "Some wikilinks remain after conversion"

**Causes & Fixes**:
1. Complex syntax → Manual review needed for files with pipes, nested brackets
2. Read-only files → Check file permissions
3. Encoding issues → Check file encoding (UTF-8 required)

### Schema Not Updated
**Symptom**: "SCHEMA.md still references wikilinks"

**Fix**: Manual update of SCHEMA.md using template from gh-wiki skill

## Scripts

Python helper scripts in `scripts/`:

- `scripts/convert_wikilinks.py` — Main conversion script for wikilinks to Markdown links
- `scripts/convert_raw.py` — Convert wikilinks in raw/ directory files
- `scripts/add_navigation.py` — Add navigation sections to all wiki pages
- `scripts/fix_navigation.py` — Fix navigation section display text formatting

### Usage Examples

```bash
# Full conversion workflow
python3 scripts/convert_wikilinks.py /path/to/wiki
python3 scripts/convert_raw.py /path/to/wiki
python3 scripts/add_navigation.py /path/to/wiki
python3 scripts/fix_navigation.py /path/to/wiki

# Individual steps
python3 scripts/convert_wikilinks.py /path/to/wiki --dry-run  # Preview changes
python3 scripts/convert_wikilinks.py /path/to/wiki           # Apply changes
```

### Script Descriptions

**convert_wikilinks.py**
- Converts `[[folder/page]]` to `[page](folder/page.md)`
- Updates SCHEMA.md linking conventions
- Creates/updates README.md with table of contents
- Updates .wiki/config.json format flag

**convert_raw.py**
- Converts wikilinks in raw/sources/ extracted.md files
- Handles same conversion patterns as main script

**add_navigation.py**
- Adds "## Navigation" section to all wiki pages
- Includes links to README.md, SCHEMA.md, and meta/index.md
- Calculates correct relative paths for subdirectories

**fix_navigation.py**
- Fixes display text in navigation links (removes `../` prefix)
- Ensures clean navigation section formatting