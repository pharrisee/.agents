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

## When NOT to Use This Skill

- **Already converted**: Wiki is already in llm-wiki format
- **No conversion need**: User only needs to view GitHub Markdown as-is
- **Single file**: One-off conversion better handled by manual edit or editor plugin
- **Different formats**: Source is neither gh-wiki nor target isn't llm-wiki
- **Read-only scenarios**: User only needs to inspect, not convert

## Non-Negotiable Rules

1. **Always backup first** — Never modify source files without backup option
2. **Dry-run by default** — Show what would change before making changes
3. **Preserve frontmatter** — Keep all YAML frontmatter intact
4. **Handle edge cases** — Report on links that can't be automatically converted

## Implementation Notes

This skill preserves git history and file structure during format migration. Always verify converted links work in Obsidian before deleting source files.

## Related Skills

- `gh-wiki` — Source wiki format
- `llm-wiki` — Target wiki format
- `llm-wiki-to-gh-wiki-converter` — Reverse conversion