---
name: llm-wiki
description: Use this skill when the user wants to capture sources, integrate knowledge into a wiki, query accumulated understanding, or audit wiki health. Initializes and maintains a persistent, compounding markdown wiki following Karpathy's LLM Wiki pattern.
---

# LLM Wiki Skill

Pure skill implementation of [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). No extension required—uses standard tools to maintain a structured, interlinked knowledge base.

## When to Use This Skill

- Capturing sources, URLs, files, or text to add to knowledge base
- Integrating source material into concept/entity/synthesis pages
- Querying accumulated wiki knowledge
- Auditing wiki health for contradictions, orphans, or stale content
- Bootstrapping a new wiki vault
- Building persistent, compounding knowledge over time
- Converting between wiki formats (gh-wiki ↔ llm-wiki)

## When NOT to Use This Skill

- **Simple Q&A**: Direct questions with clear answers — answer directly
- **Single-source capture**: Adding one simple URL without integration needs — use basic capture tools
- **Non-wiki content**: Content that doesn't benefit from persistent interlinked structure
- **Temporary notes**: Drafts or transient work better suited to scratch files
- **Personal journals**: Content not intended for shared knowledge base
- **Already-indexed sources**: Content already captured and indexed in the wiki
- **Automated scraping**: Bulk automated capture without curation or review
- **Format conversion only**: If only converting formats without content integration, use dedicated converter skills
- **Small datasets**: Content better managed with simpler tools

## Core Rules

1. **Never edit `raw/` directly** — sources are immutable after capture
2. **Never edit `meta/*` directly** — all metadata is generated
3. **Every source becomes a source page first** — before influencing canonical knowledge
4. **Search before creating** — use registry to find existing pages
5. **Cite with source IDs** — `[[sources/SRC-2026-04-04-001]]`
6. **Use folder-qualified wikilinks** — `[[concepts/retrieval-augmented-generation]]`
7. **Preserve uncertainty** — write tensions/caveats when evidence is mixed

## Implementation Notes

This skill maintains a persistent knowledge graph and is optimized for long-term knowledge management. For one-off lookups or simple queries, direct answers are more appropriate.

## Related Skills

- `gh-wiki` — GitHub Markdown format wiki
- `gh-wiki-to-llm-wiki-converter` — Migration from GitHub to LLM wiki
- `llm-wiki-to-gh-wiki-converter` — Migration from LLM wiki to GitHub
- `llm-wiki-to-gh-wiki-converter` — Format conversion

## Quality Gates

- All sources must have traceable provenance
- Claims must be tiered (confirmed/high/medium)
- Contradictions must be flagged and resolved
- Orphan pages must be reviewed periodically
- Stale content must be updated or archived

## Non-Negotiable Rules

1. **Never edit `raw/` directly** — sources are immutable after capture
2. **Never edit `meta/*` directly** — all metadata is generated
3. **Every source becomes a source page first** — before influencing canonical knowledge
4. **Search before creating** — use registry to find existing pages
5. **Cite with source IDs** — `[[sources/SRC-2026-04-04-001]]`
6. **Use folder-qualified wikilinks** — `[[concepts/retrieval-augmented-generation]]`
7. **Preserve uncertainty** — write tensions/caveats when evidence is mixed