# Page Templates Reference

Templates for all page types in the wiki.

---

## SCHEMA.md Template

Placed at wiki root. Defines operating rules for this wiki.

```markdown
# Wiki Schema

## Purpose
[Brief description of this wiki's domain]

## Conventions

### Page Types
- `sources/SRC-*.md` = what an individual source says
- `concepts/*.md` = what a concept means in this wiki
- `entities/*.md` = facts about a specific thing
- `syntheses/*.md` = cross-source theses and tensions
- `analyses/*.md` = durable answers from queries

### Linking
- Internal: `[page-name](concepts/page-name.md)` (folder-qualified with .md extension)
- Citations: `[SRC-YYYY-MM-DD-NNN](sources/SRC-YYYY-MM-DD-NNN.md)` (source ID)
- External: `[text](url)`

### Frontmatter
```yaml
---
title: "Page Title"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: source|concept|entity|synthesis|analysis
status: active|stale|contested|archived
aliases: ["Alt Name", "Another Name"]
sources: ["SRC-YYYY-MM-DD-NNN"]
---
```

### Citation Style
Cite factual claims with source page links:
> "Transformers use self-attention [SRC-2026-04-04-001](sources/SRC-2026-04-04-001.md)"

Do not cite raw packet files directly.

### Section Standards

Source pages should include:
- `## Source at a glance` — what is this?
- `## Executive summary` — 2-3 sentence overview
- `## Main claims` — bulleted key claims
- `## Important details` — concrete data points
- `## Entities and concepts mentioned` — links to canonical pages
- `## Reliability / caveats` — limitations, bias, speculation level
- `## Integration targets` — which pages should change
- `## Open questions` — gaps or follow-ups

Canonical pages should include:
- `## Definition` or `## Overview`
- `## Key claims` — with citations
- `## Related` — wikilinks
- `## Sources` — source page links
- `## Tensions / caveats` — if evidence conflicts
```

---

## .wiki/config.json Template

```json
{
  "name": "My Wiki",
  "version": "1.0.0",
  "paths": {
    "raw": "raw",
    "meta": "meta"
  },
  "capture": {
    "autoExtract": true,
    "preserveOriginal": true
  },
  "lint": {
    "checkBrokenLinks": true,
    "checkOrphans": true,
    "checkDuplicates": true
  }
}
```

---

## README.md Template

Path: `README.md`

```markdown
# Wiki Overview

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

*This wiki was initialized on YYYY-MM-DD using the gh-wiki pattern.*
```

---

## Source Page Template

Path: `sources/SRC-YYYY-MM-DD-NNN.md`

```markdown
---
title: "[Source Title]"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: source
status: captured|summarized|integrated
source_id: SRC-YYYY-MM-DD-NNN
source_url: "[URL or file path]"
captured_by: [user/model]
---

## Source at a glance
- **What**: [brief description]
- **Format**: article|paper|video|transcript|notes
- **Author/Source**: [name]
- **Date**: [YYYY-MM-DD]

## Executive summary
[2-3 sentence overview of what this source covers]

## Main claims
1. [Key claim 1]
2. [Key claim 2]
3. [Key claim 3]

## Important details and data points
- [Concrete detail with numbers/dates if available]
- [Specific examples or evidence]

## Entities and concepts mentioned
- [Entity Name](entities/Entity-Name.md)
- [Concept Name](concepts/concept-name.md)

## Reliability / caveats
- [Limitations of the source]
- [Potential bias]
- [Speculation level]

## Integration targets
Pages that should be created or updated:
- [concept-name](concepts/concept-name.md)
- [entity-name](entities/entity-name.md)
- [synthesis-name](syntheses/synthesis-name.md)

## Open questions
- [What remains unclear]
- [What to follow up on]

## Related pages
- [related-page](related-page.md)

## Navigation
- [README.md](../README.md) - Wiki overview and table of contents
- [SCHEMA.md](../SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](../meta/index.md) - Catalog of all pages

---
*Raw packet: [extracted.md](raw/sources/SRC-YYYY-MM-DD-NNN/extracted.md)*
```

---

## Concept Page Template

Path: `concepts/[name].md`

```markdown
---
title: "Concept Name"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: concept
status: active
aliases: ["Alt Name"]
sources: ["SRC-YYYY-MM-DD-NNN"]
---

## Definition
[Clear, concise definition]

## Key claims
- [Claim with citation [SRC-...](sources/SRC-....md)]
- [Another claim with citation]

## Related concepts
- [concept-name](concepts/concept-name.md)

## Entities involved
- [entity-name](entities/entity-name.md)

## Syntheses
- [synthesis-name](syntheses/synthesis-name.md)

## Sources
- [SRC-YYYY-MM-DD-NNN](sources/SRC-YYYY-MM-DD-NNN.md)

## Tensions / caveats
[Where sources disagree or evidence is weak]

## Navigation
- [README.md](../README.md) - Wiki overview and table of contents
- [SCHEMA.md](../SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](../meta/index.md) - Catalog of all pages
```

---

## Entity Page Template

Path: `entities/[name].md`

```markdown
---
title: "Entity Name"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: entity
status: active
aliases: ["Alt Name"]
sources: ["SRC-YYYY-MM-DD-NNN"]
---

## Overview
[What/who this is]

## Key facts
- [Fact with citation [SRC-...](sources/SRC-....md)]

## Relationships
- Related to [entity-name](entities/entity-name.md)

## Appears in
- [SRC-...](sources/SRC-....md)

## Navigation
- [README.md](../README.md) - Wiki overview and table of contents
- [SCHEMA.md](../SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](../meta/index.md) - Catalog of all pages
```

---

## Synthesis Page Template

Path: `syntheses/[name].md`

```markdown
---
title: "Synthesis Title"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: synthesis
status: active
aliases: []
sources: ["SRC-...", "SRC-..."]
---

## Thesis
[Main argument or conclusion]

## Evidence for
- [Point with citation]

## Evidence against / tensions
- [Counterpoint with citation]

## Open questions
- [Unresolved issues]

## Related syntheses
- [synthesis-name](syntheses/synthesis-name.md)

## Navigation
- [README.md](../README.md) - Wiki overview and table of contents
- [SCHEMA.md](../SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](../meta/index.md) - Catalog of all pages
```

---

## Analysis Page Template

Path: `analyses/[name].md`

```markdown
---
title: "Analysis: Question"
created: YYYY-MM-DD
modified: YYYY-MM-DD
type: analysis
status: active
query: "Original question asked"
sources: ["SRC-..."]
---

## Question
[Original query]

## Answer
[Synthesized answer with citations]

## Reasoning
[How the answer was derived from sources]

## Confidence
[High/Medium/Low with explanation]

## Related
- [concept-name](concepts/concept-name.md)
- [synthesis-name](syntheses/synthesis-name.md)

## Navigation
- [README.md](../README.md) - Wiki overview and table of contents
- [SCHEMA.md](../SCHEMA.md) - Wiki conventions and rules
- [meta/index.md](../meta/index.md) - Catalog of all pages
```

---

## Frontmatter Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Display name for the page |
| `created` | Yes | ISO date page created |
| `modified` | Yes | ISO date last modified |
| `type` | Yes | `source`\|`concept`\|`entity`\|`synthesis`\|`analysis` |
| `status` | Yes | `active`\|`stale`\|`contested`\|`archived` |
| `aliases` | No | Alternative names for this page |
| `sources` | No | Array of source IDs cited |
| `source_id` | Source pages | The source ID (SRC-...) |
| `source_url` | Source pages | Original URL or file path |
| `captured_by` | Source pages | Who/what captured it |
| `query` | Analysis pages | Original question asked |
