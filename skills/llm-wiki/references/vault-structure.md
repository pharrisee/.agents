# Vault Structure Reference

Complete directory layout and file organization for LLM Wiki.

## Directory Tree

```
wiki/                            # Top-level wiki folder
├─ raw/                          # Immutable source packets
│  └─ sources/
│     └─ SRC-YYYY-MM-DD-NNN/
│        ├─ manifest.json        # capture metadata
│        ├─ original/            # original artifact
│        ├─ extracted.md         # normalized text
│        └─ attachments/
├─ sources/                      # Source summary pages
├─ concepts/                     # Concept pages
├─ entities/                     # Entity pages
├─ syntheses/                    # Synthesis pages
├─ analyses/                     # Analysis pages
├─ meta/                         # Generated metadata
│  ├─ registry.json              # all pages index
│  ├─ backlinks.json             # reverse link index
│  ├─ index.md                   # human-readable catalog
│  ├─ events.jsonl               # append-only operation log
│  ├─ log.md                     # generated from events
│  └─ lint-report.md             # health check results
├─ .wiki/                        # Config and templates
│  ├─ config.json
│  └─ templates/
├─ scripts/                      # Optional helper scripts
│  └─ rebuild_metadata.py        # Rebuild metadata files
└─ SCHEMA.md                      # Operating rules and conventions
```

## Folder Purposes

### `raw/sources/`
**Rule**: Immutable after capture. Never edit directly.

Each source gets a directory `SRC-YYYY-MM-DD-NNN/` containing:
- `manifest.json` — capture metadata (URL, date, extractor used)
- `original/` — original file as captured
- `extracted.md` — normalized text extraction
- `attachments/` — images, PDFs, etc.

### `sources/`
Source summary pages. One per captured source.

Filename: `SRC-YYYY-MM-DD-NNN.md`

Links to raw packet but never cite raw files directly in other pages.

### `concepts/`
Stable concept definitions. What a concept means *in this wiki*.

Examples: `attention-mechanism.md`, `retrieval-augmented-generation.md`

### `entities/`
Facts about specific things: people, orgs, products, papers.

Examples: `karpathy-andrej.md`, `openai-gpt-4.md`, `attention-is-all-you-need.md`

### `syntheses/`
Cross-source theses, arguments, tensions, unresolved questions.

Examples: `scaling-laws-controversy.md`, `rlhf-effectiveness.md`

### `analyses/`
Durable answers from queries. Filed when user explicitly asks.

Examples: `analysis-transformer-vs-rnn.md`, `analysis-moe-tradeoffs.md`

### `meta/`
**Rule**: Machine-generated only. Never edit directly.

- `registry.json` — index of all wiki pages
- `backlinks.json` — reverse link index
- `index.md` — human-readable catalog (auto-generated)
- `events.jsonl` — append-only operation log
- `log.md` — human-readable log (generated from events)
- `lint-report.md` — health check results

### `.wiki/`
Per-wiki configuration and templates.

- `config.json` — wiki settings
- `templates/` — custom page templates (optional)

## Path References in Config

```json
{
  "paths": {
    "raw": "raw",
    "meta": "meta"
  }
}
```

Note: `sources/`, `concepts/`, `entities/`, `syntheses/`, `analyses/` are implicit and fixed.
