# Workflow Reference

Detailed step-by-step workflows for all wiki operations.

---

## Bootstrap Workflow

Initialize a new wiki vault.

### Steps

1. **Confirm wiki root path**
   - Default: `~/wiki`
   - Accept custom path if specified

2. **Create directory structure:**
   ```
   raw/sources/
   sources/
   concepts/
   entities/
   syntheses/
   analyses/
   meta/
   .wiki/templates/
   scripts/           # Optional, for helper scripts
   ```

3. **Write SCHEMA.md**
   - Use template from [[references/templates.md]]
   - Customize Purpose section for domain

4. **Write .wiki/config.json**
   - Use template from [[references/templates.md]]
   - Set wiki name and preferences

5. **Create meta/registry.json**
   ```json
   {
     "version": "1.0.0",
     "pages": [],
     "sources": [],
     "concepts": [],
     "entities": [],
     "syntheses": [],
     "analyses": []
   }
   ```

6. **Create meta/index.md**
   ```markdown
   # Wiki Index

   Generated catalog of all pages.

   ## Sources
   (Empty - populate as sources are added)

   ## Concepts
   (Empty)

   ## Entities
   (Empty)

   ## Syntheses
   (Empty)

   ## Analyses
   (Empty)
   ```

7. **Create meta/events.jsonl**
   - Empty file, ready for append

8. **Log bootstrap event**
   ```json
   {"timestamp":"2026-04-14T10:00:00Z","kind":"bootstrap","path":"~/wiki","details":"Initialized wiki vault"}
   ```

9. **Report to user**

---

## Capture Workflow

Add a new source to the wiki.

### Steps

1. **Generate source ID**
   - Format: `SRC-YYYY-MM-DD-NNN`
   - Check existing directories in `raw/sources/` for today's date
   - Find highest NNN: list dirs matching `SRC-2026-04-14-*`, extract numbers
   - Increment: if SRC-2026-04-14-003 exists, use SRC-2026-04-14-004
   - If none exist for today, start at 001

2. **Create raw packet directory**
   ```
   raw/sources/SRC-YYYY-MM-DD-NNN/
   ```

3. **Write manifest.json**
   ```json
   {
     "id": "SRC-YYYY-MM-DD-NNN",
     "captured_at": "2026-04-14T10:30:00Z",
     "source_type": "url|file|text",
     "source_url": "https://... or /path/to/file",
     "title": "Source Title",
     "extracted": true,
     "extractor": "manual|tool_name"
   }
   ```

4. **Store original content**
   - URL: Save HTML or fetch text
   - File: Copy to `original/` subdirectory
   - Text: Write to `extracted.md`

5. **Create extracted.md**
   - Normalized text from source
   - Clean formatting, no boilerplate

6. **Create source page**
   - Path: `sources/SRC-YYYY-MM-DD-NNN.md`
   - Use template from [[references/templates.md]]
   - Fill all sections from extracted content

7. **Queue for metadata update**
   - Note: Do NOT edit registry directly (violates rule #2)
   - New source will be indexed on next metadata rebuild
   - Or trigger rebuild after batch of captures

8. **Append to meta/events.jsonl**
   ```json
   {"timestamp":"2026-04-14T10:35:00Z","kind":"capture","source_id":"SRC-2026-04-14-001","details":"Captured [source type]"}
   ```

9. **Present summary to user**

---

## Integrate Workflow

Weave captured source into canonical knowledge.

### Steps

1. **Read source page thoroughly**
   - Path: `sources/SRC-YYYY-MM-DD-NNN.md`
   - Understand main claims and entities

2. **Search for existing pages**
   - Check meta/registry.json
   - Use grep for related terms
   - Identify: concepts to update, entities to create, syntheses to extend

3. **Process each integration target**

   For each target:
   
   a. **Check if page exists**
      - `ls path=concepts/target-name.md`
   
   b. **If exists**: Read existing page
   
   c. **Decide**: Update or create new?
      - New concept/entity → Create
      - Existing needs expansion → Update
      - Conflict with existing → Create synthesis
   
   d. **Create/update page**
      - Use appropriate template
      - Add citations: `[[sources/SRC-...]]`
      - Update frontmatter `modified` date
   
   e. **Update backlinks**
      - Add outgoing links to new page
      - Registry will catch incoming on rebuild

4. **Update source page status**
   - Change `status: captured` → `status: integrated`
   - Update `modified` date

5. **Append to events.jsonl**
   ```json
   {"timestamp":"2026-04-14T10:40:00Z","kind":"integrate","source_id":"SRC-2026-04-14-001","pages_updated":["concepts/...","entities/..."],"details":"Integrated into canonical knowledge"}
   ```

6. **Trigger metadata rebuild**
   - See Metadata Rebuild workflow

---

## Query Workflow

Answer questions using wiki knowledge.

### Steps

1. **Parse query intent**
   - What is the user asking?
   - What page types might contain the answer?

2. **Search wiki content**
   
   Strategy A - Registry lookup:
   - Read meta/registry.json
   - Filter by type/title matching query terms
   
   Strategy B - Grep search:
   ```bash
   grep -r "search term" . --include="*.md" -l
   ```
   
   Strategy C - Follow links:
   - Start with known relevant page
   - Follow outgoing links

3. **Read relevant pages**
   - Source pages for evidence
   - Concept pages for definitions
   - Synthesis pages for balanced views
   - Analysis pages for prior answers

4. **Synthesize answer**
   - Ground claims in wiki content
   - Cite with source page IDs: `[[sources/SRC-...]]`
   - Note confidence level
   - Flag gaps in knowledge

5. **Present answer to user**

6. **IF explicitly asked**: File as analysis
   - Create `analyses/query-slug.md`
   - Use analysis template
   - ELSE: Stop (read-only by default)

---

## Audit Workflow

Health-check the wiki.

### Steps

1. **Mechanical lint**

   a. **Broken links**
      - Grep for `[[...]]` patterns
      - Verify target files exist
      - List broken: `[[missing-page]]` in `sources/SRC-...]`
   
   b. **Orphan pages**
      - Check meta/backlinks.json
      - Find pages with zero incoming links
      - List orphans (excluding recent captures)
   
   c. **Duplicate detection**
      - Check for duplicate titles in registry
      - Check for duplicate aliases
      - Flag potential merges
   
   d. **Invalid frontmatter**
      - Scan all .md files for YAML errors
      - Check required fields present
   
   e. **Stale content**
      - Find pages not modified in 90+ days
      - Flag `status: active` stale pages

2. **Semantic audit**

   a. **Read synthesis pages**
      - Look for contradictions
      - Check evidence quality
   
   b. **Check claims vs evidence**
      - Strong claims with weak citations?
      - Claims exceeding source support?
   
   c. **Identify gaps**
      - Referenced concepts without pages?
      - Missing syntheses for disputed topics?

3. **Write lint-report.md**
   ```markdown
   # Lint Report
   Generated: YYYY-MM-DD

   ## Summary
   - Pages: N
   - Issues: N

   ## Broken Links
   - ...

   ## Orphan Pages
   - ...

   ## Stale Pages
   - ...

   ## Semantic Issues
   - ...
   ```

4. **Present summary to user**

---

## Metadata Rebuild Workflow

Regenerate all machine-owned metadata files.

### Steps

1. **Scan for all .md files**
   ```bash
   find . -name "*.md" -not -path "./raw/*"
   ```

2. **Extract frontmatter from each**
   - Parse YAML between `---` delimiters
   - Extract: title, type, status, aliases, sources

3. **Build registry.json**
   ```json
   {
     "version": "1.0.0",
     "generated": "2026-04-14T12:00:00Z",
     "pages": [
       {
         "path": "concepts/attention.md",
         "title": "Attention Mechanism",
         "type": "concept",
         "status": "active",
         "aliases": ["Self-Attention"],
         "outgoing_links": [...],
         "modified": "2026-04-10"
       }
     ]
   }
   ```

4. **Build backlinks.json**
   ```json
   {
     "concepts/attention.md": [
       "sources/SRC-2026-04-01-001",
       "syntheses/transformer-history.md"
     ]
   }
   ```

5. **Regenerate index.md**
   - Human-readable catalog
   - Group by type (sources, concepts, entities...)
   - Include last modified dates

6. **Regenerate log.md**
   - Parse events.jsonl
   - Format as readable changelog

7. **Update .wiki/last-rebuild.json**
   ```json
   {"timestamp":"2026-04-14T12:00:00Z","pages_indexed":42}
   ```
