---
name: gh-wiki
description: Use this skill when the user wants to capture sources, integrate knowledge into a wiki, query accumulated understanding, or audit wiki health. Initializes and maintains a persistent, compounding markdown wiki following Karpathy's LLM Wiki pattern but using GitHub Markdown conventions (standard Markdown links). Creates a middle layer between raw sources and answers that grows richer over time.
---

# GitHub Wiki Skill

Pure skill implementation of [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) adapted for GitHub Markdown conventions. No extension required—uses standard tools to maintain a structured, interlinked knowledge base using standard Markdown links.

## Core Idea

Instead of one-shot RAG (re-deriving answers from raw documents every query), build a **persistent, compounding wiki**—markdown files that accumulate structured knowledge with provenance, cross-references, and evolving synthesis.

## When to Use This Skill

- **Capture**: User provides URL, file, or text to add to knowledge base
- **Integrate**: Source needs to be woven into concept/entity/synthesis pages
- **Query**: Answer questions using accumulated wiki knowledge
- **Audit**: Health-check the wiki for contradictions, orphans, stale content
- **Bootstrap**: Initialize a new wiki vault

## Non-Negotiable Rules

1. **Never edit `raw/` directly** — sources are immutable after capture
2. **Never edit `meta/*` directly** — all metadata is generated
3. **Every source becomes a source page first** — before influencing canonical knowledge
4. **Search before creating** — use registry to find existing pages
5. **Cite with source IDs** — `[SRC-2026-04-04-001](sources/SRC-2026-04-04-001.md)`
6. **Use folder-qualified standard Markdown links** — `[retrieval-augmented-generation](concepts/retrieval-augmented-generation.md)`
7. **Preserve uncertainty** — write tensions/caveats when evidence is mixed
8. **Query is read-only by default** — only file analyses when explicitly asked

## Startup Protocol

When this skill activates:

1. **Check for wiki**: Look for `SCHEMA.md` or `.wiki/config.json` in:
   - Current directory
   - Default location `~/wiki`
2. **If no wiki**: Offer to bootstrap at `~/wiki` (or custom path if specified)
3. **If wiki exists**:
   - Read `SCHEMA.md`
   - Read `.wiki/config.json`
   - Read `meta/index.md` (or `meta/registry.json`)
   - Identify user's intent (capture/integrate/query/audit)

## Workflows Overview

For detailed steps for each workflow, see [references/workflows.md](references/workflows.md).

### Bootstrap
Initialize a new wiki vault at `~/wiki` (default) or custom path. Creates directory structure, config files, and initial metadata.

### Capture
Add a new source: create raw packet + source page + log event.

### Integrate
Weave source into canonical pages (concepts, entities, syntheses). Always cite with `[[sources/SRC-...]]`.

### Query
Answer questions using wiki knowledge. Read-only by default; file as analysis only if explicitly asked.

### Audit
Health-check: broken links, orphans, duplicates, stale content, contradictions.

## Vault Structure

```
wiki/                            # Top-level wiki folder
├─ raw/sources/                  # Immutable source packets
├─ sources/                      # Source summary pages
├─ concepts/                     # Concept pages
├─ entities/                     # Entity pages
├─ syntheses/                    # Synthesis pages
├─ analyses/                     # Analysis pages
├─ meta/                         # Generated metadata
├─ .wiki/                        # Config and templates
└─ SCHEMA.md                     # Operating rules and conventions
```

For full details, see [references/vault-structure.md](references/vault-structure.md).

## Page Templates

See [references/templates.md](references/templates.md) for:
- SCHEMA.md template
- .wiki/config.json template
- Source, Concept, Entity, Synthesis, Analysis page templates
- Frontmatter field reference

## Tool Usage Patterns

### Creating a source packet
```
write path=raw/sources/SRC-2026-04-14-001/manifest.json
{
  "id": "SRC-2026-04-14-001",
  "captured_at": "2026-04-14T10:30:00Z",
  "source_type": "url",
  "source_url": "https://...",
  "title": "Article Title",
  "extracted": true
}
```

### Creating source page
```
write path=sources/SRC-2026-04-14-001.md
[source page content from template]
```

### Searching wiki
```
# Find pages mentioning a term
grep pattern="attention mechanism" glob="*.md"

# Find all concept pages
find path=concepts pattern="*.md"

# Read registry
read path=meta/registry.json
```

### Ensuring a page exists
```
# Check if page exists
ls path=concepts/retrieval-augmented-generation.md

# If not exists, create with template
write path=concepts/retrieval-augmented-generation.md
[concept page template]
```

### Logging events
```
read path=meta/events.jsonl
[add new line]
write path=meta/events.jsonl content=[updated]
```

## Response Templates

### After Bootstrap
```
Wiki initialized at `[path]` (default: `~/wiki`)

Structure created:
- raw/sources/ — immutable source packets
- sources/, concepts/, entities/, syntheses/, analyses/ — knowledge pages
- meta/ — generated metadata
- SCHEMA.md — operating rules

Next: capture your first source with:
"Capture this article: [URL]"

Or initialize elsewhere:
"Initialize an llm wiki at ~/projects/research-wiki"
```

### After Capture
```
Captured to `sources/SRC-YYYY-MM-DD-NNN.md`

Source summary:
- Title: [title]
- Type: [type]
- Key claims: [N] identified

Next steps:
1. Review and improve the source page
2. Identify integration targets
3. Update relevant concept/entity pages
```

### After Query (Read-Only)
```
## Answer

[Synthesized answer with citations like [SRC-...](sources/SRC-....md)]

### Sources consulted
- [SRC-...](sources/SRC-....md) — [brief description]
- [SRC-...](sources/SRC-....md) — [brief description]

Want me to file this as a durable analysis page?
```

### After Audit
```
## Wiki Health Report

### Mechanical
- Pages: [N]
- Broken links: [N] [list if any]
- Orphan pages: [N] [list if any]
- Stale pages: [N] (not modified in 90 days)

### Semantic
- Contradictions found: [N] [describe]
- Missing pages suggested: [list]
- Confidence concerns: [list pages with weak evidence]

Full report: [meta/lint-report.md](meta/lint-report.md)
```

## Common Patterns

### Handling URLs
1. If URL content is accessible: extract text, summarize, create packet
2. If URL requires scraping: note limitation, capture URL + user summary
3. Always store original URL in manifest

### Handling Files
1. PDF: extract text (note tool used), store original.pdf, create extracted.md
2. Markdown: copy to extracted.md, preserve original
3. Other: store original, note extraction limitations

### Handling Pasted Text
1. Create extracted.md with the text
2. User becomes "source"
3. Ask clarifying questions to improve source page

## Error Handling

| Issue | Resolution |
|-------|------------|
| Wiki not initialized | Offer to bootstrap |
| Source ID collision | Increment counter, retry |
| Broken Markdown link found in lint | Add to lint report, suggest fixes |
| Duplicate page detected | Suggest merge or disambiguation |
| Conflicting sources | Note tension in synthesis page, don't resolve arbitrarily |

## Integration with Other Skills

This skill composes well with:
- **websearch**: For capturing web sources
- **codesearch**: For capturing code/API documentation
- **visual-explainer**: For generating diagrams of wiki structure
- **planning-with-files**: For complex integration workflows

## Examples

### Example 1: Capture → Integrate → Query

**User**: "Initialize an llm wiki for my AI research"

1. **Bootstrap** at `~/wiki`
2. Creates directory structure, SCHEMA.md, config.json

**User**: "Capture this article: https://karpathy.ai/blog/transformer-math.html"

3. **Capture** creates:
   - `raw/sources/SRC-2026-04-14-001/` with manifest, original, extracted
   - `sources/SRC-2026-04-14-001.md` with summary, claims, entities

**User**: "Integrate this source"

4. **Integrate** reads source page, identifies targets:
   - Creates `concepts/transformer-scaling-laws.md` (new concept)
   - Updates `entities/karpathy-andrej.md` (existing entity)
   - Creates `syntheses/chinchilla-vs-kaplan-laws.md` (synthesis of conflicting sources)
   - Marks source status: `integrated`

**User**: "What do we know about transformer scaling?"

5. **Query** searches:
   - Finds `concepts/transformer-scaling-laws.md`
   - Finds `syntheses/chinchilla-vs-kaplan-laws.md`
   - Synthesizes answer with citations
   - Presents: "According to [SRC-2026-04-14-001](sources/SRC-2026-04-14-001.md), compute-optimal scaling... However, [chinchilla-vs-kaplan-laws](syntheses/chinchilla-vs-kaplan-laws.md) notes tension with..."

### Example 2: Multi-Source Integration

**User**: "Capture these papers: [URL1], [URL2], [URL3]"

1. **Capture** all three → three source pages created

**User**: "Integrate all new sources"

2. **Integrate** processes each:
   - Source 1: Creates `concepts/attention-mechanism.md`
   - Source 2: Updates `concepts/attention-mechanism.md` with new variant
   - Source 3: Creates `syntheses/attention-efficiency-tradeoffs.md` (compares approaches from all three)

3. All three sources marked `integrated`

### Example 3: Audit and Repair

**User**: "Audit my wiki"

1. **Audit** runs:
   - Finds 2 broken links: `[[concepts/old-name]]` (renamed)
   - Finds 1 orphan: `entities/random-researcher.md` (no links to it)
   - Finds 3 stale pages (not modified in 90 days)

2. **Report** suggests fixes

**User**: "Fix the broken links"

3. Updates links to `[[concepts/new-name]]` in affected pages

**User**: "Show me orphan pages"

4. Presents orphan with suggestion: "Link from `syntheses/attention-efficiency-tradeoffs.md`?"

## Limitations

### What This Skill Cannot Do

1. **No automatic extraction from paywalled content**
   - Can capture URL + user summary, but not extract full text
   - Requires manual paste for paywalled articles

2. **No semantic search across raw content**
   - Only queries indexed wiki pages, not raw packets
   - Must integrate sources before they're searchable

3. **No automatic contradiction resolution**
   - Flags tensions in synthesis pages
   - Does not auto-resolve; requires human judgment

4. **No version control integration**
   - Works with git, but doesn't manage commits
   - User handles version control separately

5. **No collaborative merge handling**
   - Single-user workflow assumed
   - Concurrent edits may cause conflicts

6. **No automatic metadata rebuilds**
   - Must trigger rebuild explicitly after bulk changes
   - Registry may be stale until rebuild

### Scope Boundaries

| In Scope | Out of Scope |
|----------|--------------|
| Structured note-taking | Task/project management |
| Source provenance tracking | Citation management (BibTeX/Zotero) |
| Cross-source synthesis | Original research/data collection |
| Knowledge auditing | Automated fact-checking |
| Markdown-based wiki | Binary document formats |

## Troubleshooting

### Wiki Not Found

**Symptom**: "No wiki found in current directory or ~/wiki"

**Causes & Fixes**:
1. Never initialized → Run bootstrap workflow
2. Wrong directory → `cd ~/wiki` or specify path
3. Missing SCHEMA.md → May be corrupted; re-initialize or restore from backup

### Source ID Collision

**Symptom**: "Source ID SRC-2026-04-14-001 already exists"

**Fix**: Increment counter: SRC-2026-04-14-002, SRC-2026-04-14-003, etc.
Check `meta/registry.json` for highest existing ID.

### Broken Links After Rename

**Symptom**: Audit shows broken `[old-name](concepts/old-name.md)`

**Fix Options**:
1. Update all links to new name (search/replace)
2. Create redirect page at old name with link to new page: `[new-name](concepts/new-name.md)`
3. Add alias in frontmatter of new page: `aliases: ["old-name"]`

### Registry Out of Sync

**Symptom**: Pages exist but not in registry; search misses them

**Fix**: Trigger metadata rebuild workflow

### Integration Conflicts

**Symptom**: Source contradicts existing wiki content

**Resolution**:
1. Create/update synthesis page documenting the tension
2. Do not silently overwrite existing claims
3. Present both views with source citations
4. Mark related pages `status: contested` if needed

### Large-Scale Import

**Symptom**: Importing 100+ sources is slow

**Workaround**:
1. Batch captures (create all raw packets first)
2. Batch integrations (process sources in groups)
3. Run metadata rebuild once at end, not per source

### Stale Content Detection

**Symptom**: Page marked stale but still accurate

**Fix**: Update `modified` date in frontmatter to reset timer, or change `status: active` to indicate manually verified

## Scripts

Optional helper scripts in `scripts/`:

- `scripts/rebuild_metadata.py` — Rebuilds registry.json, backlinks.json, index.md, log.md from wiki contents
  - Usage: `python3 scripts/rebuild_metadata.py [wiki-path]`
  - Can be run manually or triggered after batch operations

## References

- [references/vault-structure.md](references/vault-structure.md) — Directory layout and folder purposes
- [references/templates.md](references/templates.md) — All page templates and frontmatter reference
- [references/workflows.md](references/workflows.md) — Detailed step-by-step workflows
