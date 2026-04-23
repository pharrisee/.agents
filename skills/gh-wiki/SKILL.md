---
name: gh-wiki
description: Use this skill when the user wants to capture sources, integrate knowledge into a wiki, query accumulated understanding, or audit wiki health. Initializes and maintains a persistent, compounding markdown wiki following Karpathy's LLM Wiki pattern but using GitHub Markdown conventions (standard Markdown links). Creates a middle layer between raw sources and answers that grows richer over time.
---

# GitHub Wiki Skill

Pure skill implementation of [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) adapted for GitHub Markdown conventions. Uses standard tools to maintain a structured, interlinked knowledge base with plain Markdown files (`.md`) and standard links.

## When to Use This Skill

- Capturing sources, URLs, files, or text to add to knowledge base
- Integrating source material into concept/entity/synthesis pages
- Querying accumulated wiki knowledge
- Auditing wiki health for contradictions, orphans, or stale content
- Bootstrapping a new wiki vault
- Building persistent, compounding knowledge over time

## When NOT to Use This Skill

- **Simple Q&A**: Direct questions with clear answers (e.g., "What is X?") — answer directly
- **Single-source capture**: Adding one simple URL without integration needs — use basic capture tools
- **Non-wiki content**: Content that doesn't benefit from persistent interlinked structure
- **Temporary notes**: Drafts or transient work better suited to scratch files
- **Personal journals**: Content not intended for shared knowledge base
- **Already-indexed sources**: Content already captured and indexed in the wiki
- **Automated scraping**: Bulk automated capture without curation or review

## Core Rules

1. **Never edit `raw/` directly** — sources are immutable after capture
2. **Never edit `meta/*` directly** — all metadata is generated
3. **Every source becomes a source page first** — before influencing canonical knowledge
4. **Search before creating** — use registry to find existing pages
5. **Cite with source IDs** — use plain IDs like `SRC-2026-04-04-001` or `[SRC-2026-04-04-001]` as a reference tag (not a link)
6. **Use folder-qualified standard Markdown links** — always include `.md` extension: `[Retrieval-Augmented-Generation](concepts/retrieval-augmented-generation.md)`
7. **Preserve uncertainty** — write tensions/caveats when evidence is mixed

## Implementation Notes

This skill provides a complete workflow and tool integration for maintaining a structured knowledge base. For one-off lookups or simple queries, direct answers are more appropriate.

## Commands & Tool Integration

When this skill is active, use the following tools to manage the wiki:

- `terminal` to create, read, search files and maintain directory structure
- `search_files` to query the wiki registry and content
- `write_file` and `patch` to edit pages

### Common Operations

1. **Bootstrap** (first time setup):
   ```bash
   mkdir -p wiki/{raw,sources,concepts,entities,syntheses,meta}
   echo "# Wiki Registry" > wiki/registry.md
   ```

2. **Capture a source** (URL/text):
   - Save raw content to `wiki/raw/YYYY-MM-DD-<slug>.{txt,json,html}`
   - Create a source page `wiki/sources/SRC-YYYY-MM-DD-NNN.md` with frontmatter
   - Update `wiki/registry.md` with a link to the new source

3. **Search**:
   ```bash
   search_files -p "query" wiki --target=content
   ```

4. **Audit**:
   - Check for orphan pages (no incoming links)
   - Find stale content (last modified > 6 months)
   - Identify contradictions by searching for conflicting claims

See the `llm-wiki` skill for an alternative implementation using Obsidian wikilinks.

## Workflow Pattern

**Capture → Integrate → Query → Audit → Bootstrap**

Each source follows a strict lifecycle: capture as raw source, integrate into concepts/synthesis, query for answers, audit for quality, and bootstrap new content only when necessary.

## Quality Gates

- All sources must have traceable provenance
- Claims must be tiered (confirmed/high/medium)
- Contradictions must be flagged and resolved
- Orphan pages must be reviewed periodically
- Stale content must be updated or archived

## Related Skills

- `gh-wiki-fact-checker` — Verify wiki content accuracy
- `llm-wiki` — Alternative LLM wiki pattern implementation (Obsidian wikilinks)
- `gh-wiki-to-llm-wiki-converter` — Migration from GitHub to LLM wiki
- `llm-wiki-to-gh-wiki-converter` — Migration from LLM wiki to GitHub

## Non-Negotiable Rules (Restated)

1. Never edit `raw/` directly — sources are immutable after capture
2. Never edit `meta/*` directly — all metadata is generated
3. Every source becomes a source page first — before influencing canonical knowledge
4. Search before creating — use registry to find existing pages
5. Cite with source IDs — use plain IDs or bracketed references, e.g., `SRC-2026-04-04-001`
6. Use folder-qualified standard Markdown links — e.g., `[page title](concepts/page-name.md)`
7. Preserve uncertainty — write tensions/caveats when evidence is mixed

### Markdown Link Syntax

- Use standard GitHub-flavored Markdown links: `[link text](relative/path/to/page.md)`
- Always include the `.md` extension in the target.
- For root-level pages: `[Registry](registry.md)`
- For nested pages: `[Retrieval-Augmented-Generation](concepts/retrieval-augmented-generation.md)`

### Citation Format

- When referencing a source in text, use the plain ID: `SRC-2026-04-04-001`
- Optionally wrap the ID in brackets for clarity: `[SRC-2026-04-04-001]`
- Do not use wikilinks for source IDs.

### Folder Structure

- `wiki/` (root of the wiki vault)
  - `raw/` (immutable raw source captures)
  - `sources/` (individual source pages, each with unique ID)
  - `concepts/` (concept pages, e.g., retrieval-augmented-generation.md)
  - `entities/` (entity pages for specific people/places/things)
  - `syntheses/` (synthesis pages that integrate multiple sources)
  - `meta/` (auto-generated registry.json, indexes, caches)
  - `registry.md` (human-readable index of all pages)

### Registry

Maintain a `wiki/registry.md` that lists all pages with brief descriptions and last-modified dates. Update it when creating new pages.
