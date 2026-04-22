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
- Internal: `[[concepts/page-name]]` (folder-qualified)
- Citations: `[[sources/SRC-YYYY-MM-DD-NNN]]` (source ID)
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
> "Transformers use self-attention [[sources/SRC-2026-04-04-001]]"

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
- [[entities/Entity Name]]
- [[concepts/Concept Name]]

## Reliability / caveats
- [Limitations of the source]
- [Potential bias]
- [Speculation level]

## Integration targets
Pages that should be created or updated:
- [[concepts/...]]
- [[entities/...]]
- [[syntheses/...]]

## Open questions
- [What remains unclear]
- [What to follow up on]

## Related pages
- [[...]]

---
*Raw packet: [[raw/sources/SRC-YYYY-MM-DD-NNN/extracted.md]]*
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
- [Claim with citation [[sources/SRC-...]]]
- [Another claim with citation]

## Related concepts
- [[concepts/...]]

## Entities involved
- [[entities/...]]

## Syntheses
- [[syntheses/...]]

## Sources
- [[sources/SRC-YYYY-MM-DD-NNN]]

## Tensions / caveats
[Where sources disagree or evidence is weak]
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
- [Fact with citation [[sources/SRC-...]]]

## Relationships
- Related to [[entities/...]]

## Appears in
- [[sources/SRC-...]]
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
- [[syntheses/...]]
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
- [[concepts/...]]
- [[syntheses/...]]
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
