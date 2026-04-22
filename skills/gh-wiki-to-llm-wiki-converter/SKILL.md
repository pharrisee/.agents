---
name: gh-wiki-to-llm-wiki-converter
description: Use this skill when the user wants to convert an existing gh-wiki (GitHub Markdown format) to llm-wiki (Obsidian vault format). Provides tools and workflows for migrating standard Markdown links to wikilinks and updating wiki conventions for Obsidian compatibility.
---

# GitHub Wiki to LLM Wiki Converter Skill

Skill for converting an existing gh-wiki (using standard GitHub Markdown links) to llm-wiki (using Obsidian-style wikilinks). Handles link conversion, schema updates, and configuration migration for Obsidian compatibility.

## When to Use This Skill

- **Migration**: User has an existing gh-wiki vault and wants to convert it to Obsidian wikilinks format
- **Partial conversion**: User wants to convert specific files or directories to wikilinks
- **Validation**: Check if a wiki is already in llm-wiki format or needs conversion
- **Batch processing**: Convert multiple files with Markdown links to wikilinks
- **Obsidian integration**: Prepare wiki for use with Obsidian or other wikilink-based tools

## Non-Negotiable Rules

1. **Always backup first** — Never modify source files without backup option
2. **Dry-run by default** — Show what would change before making changes
3. **Preserve frontmatter** — Keep all YAML frontmatter intact
4. **Handle edge cases** — Report on links that can't be automatically converted
5. **Update schema** — Ensure SCHEMA.md reflects Obsidian wikilink conventions after conversion
6. **Navigation sections** — Keep or adapt navigation sections as appropriate for target format

## Startup Protocol

When this skill activates:

1. **Check for wiki**: Look for `SCHEMA.md` or `.wiki/config.json` in current directory or specified path
2. **Determine format**: Check if wiki uses `[Markdown links](...)` (gh-wiki) or `[[wikilinks]]` (llm-wiki)
3. **Assess conversion scope**: Count files, estimate changes needed
4. **Check for README.md**: Determine if README.md exists and needs conversion
5. **Present conversion plan**: Show user what will be changed
6. **Get confirmation**: Only proceed after user approval

## Workflows Overview

### Full Conversion
Convert entire wiki vault from gh-wiki to llm-wiki format.

### Partial Conversion  
Convert specific files or directories.

### Validation Check
Report on conversion readiness and potential issues.

### Schema Update
Update SCHEMA.md and config files for Obsidian wikilink conventions.

### README.md Handling
Convert README.md links to wikilinks or create Obsidian-friendly version.

## Conversion Rules

### Link Conversion Patterns

| From (gh-wiki) | To (llm-wiki) | Notes |
|----------------|---------------|-------|
| `[page-name](page-name.md)` | `[[page-name]]` | Same directory |
| `[page-name](folder/page-name.md)` | `[[folder/page-name]]` | Folder-qualified |
| `[display](folder/page-name.md)` | `[[folder/page-name\|display]]` | With display text |
| `[SRC-...](sources/SRC-....md)` | `[[sources/SRC-...]]` | Source citations |
| `[...](concepts/....md)` | `[[concepts/...]]` | Concept links |
| `[...](entities/....md)` | `[[entities/...]]` | Entity links |
| `[...](syntheses/....md)` | `[[syntheses/...]]` | Synthesis links |
| `[...](analyses/....md)` | `[[analyses/...]]` | Analysis links |
| `[...](raw/....md)` | `[[raw/...]]` | Raw file links |
| `[README.md](../README.md)` | `[[README]]` or keep as is | Navigation links |

### Frontmatter Updates
- Keep all existing frontmatter fields
- No changes needed to YAML structure
- Ensure `type`, `status`, `aliases` remain intact

### Schema Updates
- Update linking conventions in SCHEMA.md to use wikilinks
- Update examples to use `[[wikilinks]]` format
- Add Obsidian-specific references if needed
- Remove GitHub Markdown-specific guidance

### README.md Handling Options
1. **Convert fully**: Change all Markdown links to wikilinks
2. **Hybrid approach**: Keep README.md with Markdown links for GitHub, create separate `INDEX.md` with wikilinks
3. **Navigation sections**: Convert navigation sections to use wikilinks or remove if not needed for Obsidian
4. **Create Obsidian-friendly version**: Generate `Obsidian-README.md` with wikilinks

## Tool Usage Patterns

### Checking for Markdown links
```bash
# Count Markdown links in a file
grep -o "\[[^]]*\]([^)]*\.md)" file.md | wc -l

# Find all files with Markdown links to .md files
grep -r "\[[^]]*\]([^)]*\.md)" . --include="*.md" -l
```

### Dry-run conversion
```bash
# Show what would change (simple links)
sed -n "s/\[\([^]]*\)\](\([^)]*\)\.md)/[[\2|\1]]/gp" file.md
sed -n "s/\[\([^]]*\)\](\([^)]*\)\.md)/[[\2]]/gp" file.md

# Show what would change (links where display text matches filename)
sed -n "s/\[\([^)]*\)\](\([^)]*\)\.md)/[[\2]]/gp" file.md
```

### Actual conversion
```bash
# Convert Markdown links with display text different from filename
sed -i "s/\[\([^]]*\)\](\([^)]*\)\.md)/[[\2|\1]]/g" file.md

# Convert simple Markdown links where display matches filename
sed -i "s/\[\([^)]*\)\](\([^)]*\)\.md)/[[\2]]/g" file.md
```

### Backup before conversion
```bash
# Create backup directory
cp -r wiki/ wiki-backup-$(date +%Y%m%d-%H%M%S)/
```

### README.md specific handling
```bash
# Convert README.md links but keep structure
sed -i "s/\[\([^]]*\)\](\([^)]*\))/[[\2|\1]]/g" README.md
sed -i "s/\[\([^)]*\)\](\([^)]*\))/[[\2]]/g" README.md
```

### Using Python conversion scripts
```bash
# Full conversion using Python scripts
python3 scripts/convert_markdown_links.py /path/to/wiki
python3 scripts/remove_navigation.py /path/to/wiki

# Check for remaining Markdown links after conversion
grep -r "\[[^]]*\]([^)]*\.md)" /path/to/wiki --include="*.md" | wc -l
```

## Response Templates

### After Validation Check
```
## Wiki Format Analysis

**Location**: /path/to/wiki

**Format detected**: gh-wiki (GitHub Markdown links)

**Statistics**:
- Total .md files: 42
- Files with Markdown links: 38 (90%)
- Total Markdown links: 215
- README.md present: Yes/No
- Estimated conversion time: < 1 minute

**Issues found**:
- 5 files have complex relative paths (`../../`) that need review
- SCHEMA.md references `[Markdown links](...)` conventions
- README.md has navigation sections that may need adaptation

**Recommendation**: Run full conversion with backup.
```

### After Dry-Run
```
## Conversion Preview

**Files to modify**: 38 files

**Sample changes**:

File: `concepts/attention.md`
- `[SRC-2026-04-01](sources/SRC-2026-04-01.md)` → `[[sources/SRC-2026-04-01]]`
- `[Transformer](entities/Transformer.md)` → `[[entities/Transformer]]`

File: `sources/SRC-2026-04-01.md`
- `[attention](concepts/attention.md)` → `[[concepts/attention]]`
- `[README.md](../README.md)` → `[[README]]` (navigation link)

**README.md changes**:
- `[sources/](sources/)` → `[[sources]]` (directory link)
- `[SCHEMA.md](SCHEMA.md)` → `[[SCHEMA]]`

**Total changes**: 215 link conversions

**README.md handling**: Will convert all links to wikilinks

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
- README.md converted: Yes (links updated to wikilinks)

**Schema updated**:
- SCHEMA.md linking conventions updated to wikilinks
- .wiki/config.json format flag set to "llm-wiki"
- Examples updated for Obsidian compatibility

**Next steps**:
1. Verify conversion with: `grep -r "\[[^]]*\]([^)]*\.md)" . --include="*.md"` (should return minimal results)
2. Test links in Obsidian or wikilink-compatible viewer
3. Consider creating Obsidian workspace file if needed
4. Update git repository if version controlled
```

## Error Handling

| Issue | Resolution |
|-------|------------|
| Complex relative paths (`../../folder/file.md`) | Flag for manual review, may need path adjustment |
| External links (non-.md files) | Keep as Markdown links, don't convert to wikilinks |
| Broken links (target doesn't exist) | Report in conversion log, don't convert |
| Permission errors | Suggest running with appropriate permissions |
| Large wiki (>1000 files) | Batch processing, progress reporting |
| Mixed format (some files already have wikilinks) | Skip already converted files |
| README.md navigation sections with complex formatting | Offer to preserve as Markdown or create separate index |

## Integration with Other Skills

This skill composes well with:
- **llm-wiki**: For working with the converted wiki
- **gh-wiki**: For understanding source format
- **llm-wiki-to-gh-wiki-converter**: For bidirectional conversion workflows
- **file-operations**: For batch file processing

## Examples

### Example 1: Full Conversion
**User**: "Convert my gh-wiki at ~/research-wiki to llm-wiki format for Obsidian"

1. **Validation**: Check wiki format, count files, check README.md
2. **Backup**: Create timestamped backup
3. **Conversion**: Process all .md files, convert Markdown links to wikilinks
4. **README.md conversion**: Update README.md links to wikilinks
5. **Schema update**: Update SCHEMA.md with wikilink conventions
6. **Verification**: Run check to ensure Markdown links are converted

### Example 2: Partial Conversion  
**User**: "Convert just the concepts/ directory to wikilinks"

1. **Scope limitation**: Only process files in concepts/
2. **Dry-run**: Show changes for concepts/ files only
3. **Conversion**: Apply changes to specified directory
4. **README.md handling**: Skip README.md or convert only relevant links
5. **Report**: Summary of converted files in concepts/

### Example 3: README.md Only Conversion
**User**: "Make my README.md work with Obsidian wikilinks"

1. **Analysis**: Scan README.md for Markdown links
2. **Conversion options**: Present choices (full convert, hybrid, separate index)
3. **Execution**: Apply chosen conversion strategy
4. **Verification**: Test links in Obsidian

### Example 4: Schema Update Only
**User**: "Update my SCHEMA.md for Obsidian but don't convert links yet"

1. **Read current SCHEMA.md**: Understand existing conventions
2. **Update**: Change linking examples to wikilinks
3. **Add Obsidian notes**: Optional section on Obsidian setup
4. **No file conversions**: Leave all .md files unchanged

## Limitations

### What This Skill Cannot Do

1. **No Obsidian plugin configuration** — Only converts link format, doesn't set up Obsidian plugins
2. **No vault creation** — Assumes wiki directory exists, doesn't create Obsidian vault
3. **No bidirectional link generation** — Doesn't create backlinks or graph view
4. **No image/embed handling** — Only converts .md file links, not image embeds
5. **No template updates** — Doesn't modify page templates, only existing content

### Scope Boundaries

| In Scope | Out of Scope |
|----------|--------------|
| Markdown link to wikilink conversion | Obsidian plugin installation |
| Schema convention updates | Vault configuration files |
| README.md adaptation | Graph view optimization |
| Format migration | Custom CSS/themes |
| Backup creation | Sync service setup |
| Dry-run previews | Manual editing of edge cases |

## README.md Specific Considerations

### Conversion Strategies for README.md

1. **Full wikilink conversion**:
   - Pros: Consistent, works fully in Obsidian
   - Cons: May not render well on GitHub/GitLab
   - Use when: Wiki is primarily for Obsidian use

2. **Hybrid approach**:
   - Keep README.md with Markdown links for web viewing
   - Create `INDEX.md` or `Obsidian-README.md` with wikilinks
   - Use when: Wiki needs to work both on web and in Obsidian

3. **Navigation section preservation**:
   - Convert navigation links but keep section structure
   - May need to adjust relative paths for wikilinks
   - Use when: Navigation is important for both formats

4. **Minimal conversion**:
   - Only convert internal .md file links, leave external links as Markdown
   - Use when: README.md has many external references

### Recommended Default
For most conversions, use **full wikilink conversion** for consistency, with the understanding that README.md may not render perfectly on GitHub but will work best in Obsidian.

## Troubleshooting

### Conversion Failed
**Symptom**: "Conversion failed with error"

**Causes & Fixes**:
1. Permission denied → Check file permissions, run with sudo if appropriate
2. Disk full → Check available space
3. Malformed Markdown links → Run validation first to identify problem files
4. Complex regex patterns → Use simpler conversion in batches

### Partial Conversion
**Symptom**: "Some Markdown links remain after conversion"

**Causes & Fixes**:
1. Complex link patterns → Manual review needed for files with special characters
2. Read-only files → Check file permissions
3. Encoding issues → Check file encoding (UTF-8 required)
4. External links → These are intentionally not converted

### Schema Not Updated
**Symptom**: "SCHEMA.md still references Markdown links"

**Fix**: Manual update of SCHEMA.md using template from llm-wiki skill

### README.md Rendering Issues
**Symptom**: "README.md looks broken on GitHub after conversion"

**Fix Options**:
1. Revert README.md changes and use hybrid approach
2. Create GitHub-specific README-GH.md
3. Use relative paths that work in both formats

## Scripts

Optional helper scripts in `scripts/`:

- `scripts/convert-to-wikilinks.sh` — Batch conversion from Markdown to wikilinks
## Scripts

Python helper scripts in `scripts/`:

- `scripts/convert_markdown_links.py` — Main conversion script for Markdown links to wikilinks
- `scripts/convert_raw.py` — Convert Markdown links in raw/sources/ extracted.md files
- `scripts/remove_navigation.py` — Remove navigation sections added by gh-wiki

### Usage Examples

```bash
# Full conversion workflow
python3 scripts/convert_markdown_links.py /path/to/wiki
python3 scripts/convert_raw.py /path/to/wiki
python3 scripts/remove_navigation.py /path/to/wiki

# Check for remaining Markdown links after conversion
grep -r "\[[^]]*\]([^)]*\.md)" /path/to/wiki --include="*.md" | wc -l
```

### Script Descriptions

**convert_markdown_links.py**
- Converts `[display](folder/page.md)` to `[[folder/page|display]]` or `[[folder/page]]`
- Preserves display text when different from page name
- Updates SCHEMA.md linking conventions to wikilinks
- Updates .wiki/config.json format flag to "llm-wiki"

**convert_raw.py**
- Converts Markdown links in raw/sources/ extracted.md files
- Handles same conversion patterns as main script

**remove_navigation.py**
- Removes "## Navigation" sections added by gh-wiki
- Obsidian wikilinks provide navigation through clicking
- Cleans up gh-wiki specific formatting