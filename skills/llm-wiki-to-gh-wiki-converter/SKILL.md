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

## When NOT to Use This Skill

- **Already converted**: Wiki is already in gh-wiki format
- **Different source**: Source format is neither llm-wiki nor target isn't gh-wiki
- **No link migration needed**: User only needs to view content as-is
- **Read-only access**: User cannot write to destination wiki
- **Single file trivial**: One-off changes better handled manually

## Non-Negotiable Rules

1. **Always backup first** — Never modify source files without backup option
2. **Dry-run by default** — Show what would change before making changes
3. **Preserve frontmatter** — Keep all YAML frontmatter intact
4. **Handle edge cases** — Report on links that can't be automatically converted

## Implementation Notes

This skill maintains bidirectional link compatibility. Verify converted markdown renders correctly in GitHub before removing source files.

## Related Skills

- `llm-wiki` — Source wiki format
- `gh-wiki` — Target wiki format
- `gh-wiki-to-llm-wiki-converter` — Reverse conversion