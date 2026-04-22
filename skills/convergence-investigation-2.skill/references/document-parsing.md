# Government / Institutional Document Parsing

When the input is a government solicitation, regulatory filing, court document, foundation grant announcement, formal RFI/RFP, agency report, or analogous institutional document, parse it into the methodology's standard intelligence schema.

## Why this matters

Institutional documents are unusually high-signal sources. They typically name programme managers, state budgets and timelines, list incumbent participants, and disclose technical or substantive priorities that the issuing institution has chosen to make public. Compared to corporate press releases or third-party reporting, they are dense with verifiable structured data.

## Procedure

### Step 1: Fetch and store

If the input is a URL:
- Use `web_fetch` with `html_extraction_method: markdown` — usually best for government portals
- If markdown extraction fails or strips content, fall back to default extraction
- For PDFs, follow the `pdf-reading` skill if available; otherwise extract text and parse

Save the raw text to `/home/claude/<thread>/<doc-id>-raw.md` so subsequent passes don't re-fetch.

### Step 2: Extract the standard fields

Every institutional document parse must produce at minimum:

```markdown
## <Document title> (<reference number>)

| Field | Value |
|-------|-------|
| Issuing institution | Agency / Foundation / Court / etc. |
| Office / division | e.g., specific directorate or programme office |
| Document type | Solicitation / RFI / RFP / BAA / Notice / Order / Report |
| Reference ID | Document number |
| Posted / issued date | YYYY-MM-DD |
| Response deadline (if applicable) | YYYY-MM-DD HH:MM TZ |
| Award type (if applicable) | Contract / Grant / Cooperative Agreement / Other |
| Phase structure (if applicable) | e.g., 18-month Phase 1 + optional Phase 2 |
| Total estimated budget | $X-Y million (or stated; or "not disclosed") |
| Programme manager / responsible official | Name, title, contact |
| Reference URL | Canonical link |
```

Adapt the field set to the document type. A court filing has different metadata than a grant announcement.

### Step 3: Decompose the substantive content

Extract:
- **Task areas / focus areas / claims** — list each as its own subsection with the goal, scope, and key parameters
- **Technical thresholds** — performance, accuracy, size, or other measurable targets stated in the document
- **Excluded approaches** — what the document explicitly says it is not interested in or not authorising
- **Named example technologies, parties, or precedents** — specific organisations, products, papers, or prior cases cited by name (these are the incumbent landscape or precedent set)

The named entities are gold. If a government solicitation lists three companies as exemplar incumbents in a field, that is the issuing agency's view of who counts in the space. If a court filing cites three prior cases, those are the precedents being treated as load-bearing.

### Step 4: Map to the bridge-figure method

Named officials in the document — programme managers, contracting officers, signatories — are bridge figure candidates. Run the bridge-figure procedure on them:
- What was their prior role? (Often academic, prior agency, or prior private-sector — go find the institution)
- What other documents have they issued or signed?
- Do they connect to anyone in the project's existing graph?

Record each named official as a node (`type: "person"`, `category: "official"`) with their bridging context.

### Step 5: Predict the participant landscape

Based on the named exemplar entities plus public knowledge of the field, list likely respondents/parties. Mark each:
- **Confirmed participant** — has publicly stated they will participate (rare)
- **Likely participant** — has the capability and prior track record
- **Possible participant** — has the capability but no documented track record

This becomes a watch-list for post-deadline tracking.

### Step 6: Significance assessment

In a one-paragraph "significance" section, answer:
- What does this document tell us about the issuing institution's priorities?
- Does it confirm, refute, or extend existing graph claims?
- What is the timeline implication — when will outcomes be observable?
- What new threads does it open?

### Step 7: Graph updates

Add to graph:
- The programme / case / order as a node (`type: "concept"`, `category: "government_programme"` or analogous)
- Named officials as person nodes
- Edges from the programme to each named exemplar party already in graph
- Edge from issuing institution (if not already a node) to programme

Confidence is `confirmed` for any field directly read from the document. Inferred fields (predicted participants, significance assessment) are `medium` and don't enter graph.

## Output snippet for the report

Use the standard report template (specified in the main `SKILL.md` Phase 3). Include:

- Document metadata table
- Named officials and their bridging-figure status
- Substantive content breakdown
- Significance paragraph
- Graph actions

## Special cases

- **Amendments and addenda:** if the URL is to an amendment, fetch both the original and the amendment, note the changes, and use the most recent values
- **Restricted or partially-redacted documents:** if the document references unclassified-but-restricted appendices or has redacted sections, note the references but do not attempt to obtain restricted content; flag the gap in the report
- **International equivalents:** the same procedure applies across jurisdictions — UK government tenders, EU Horizon calls, Australian agency notices, court documents from any jurisdiction. Adjust the field names but keep the structure
- **Old documents:** for archival materials, the participant-prediction step may not apply; instead, identify the historical context and any subsequent documents that referenced this one
