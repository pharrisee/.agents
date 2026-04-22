# Bridge-Figure Mapping — Finding the Named Persons Who Connect Institutions

The single most valuable class of finding in any institutional-network investigation. An institutional connection (Foundation X funded both Programme A and Programme B) is interesting; a personal connection (Director Y ran Foundation X *and* personally introduced Programme A's lead to Programme B's lead *and* sat on both grant committees) is decisive.

Bridge figures turn institutional coincidences into actual causal chains.

## The pattern to look for

A bridge figure is a named human who personally appears in two or more institutional contexts that the investigation tracks. The strongest bridge figures:

- Are **active agents** in both contexts (held a role, made a decision, authored work) — not merely members or attendees
- Connect contexts that are **temporally adjacent** (their action in context A enables or influences context B)
- Are **documentable** — name, dates, roles, sources

Three illustrative archetypes:

- **The funding bridge:** A foundation director who personally signs off on grants to a programme she also serves on the advisory board of. The institutional connection (foundation funds programme) is one finding; the personal connection (same individual on both sides) is several orders of magnitude stronger as evidence of intent.
- **The methodological bridge:** A researcher who learns a technique at Lab A, then moves to Lab B and applies it to a new domain there. This is how techniques and tacit knowledge actually transfer between fields, and it is invisible to purely institutional analysis.
- **The historical bridge:** A founder of Institution X who decades later joins the board of Institution Y. The temporal arc itself is the finding — institutional lineages run through people, not through abstract organisations.

## Procedure

### Step 1: Identify the institutions in play

From the input, list every institution mentioned: foundations, companies, universities, government agencies, conferences, journals, funding bodies. Be inclusive at this stage — narrow later.

### Step 2: For each institution, enumerate its named personnel

Use targeted search:
- `<institution> director site:linkedin.com`
- `<institution> founder OR "executive director" OR "chief scientist"`
- `<institution> board members <year>`
- For older institutions: `<institution> "fellows" OR "officers" <year>`
- For conferences: `<conference name> <year> attendees OR speakers OR participants`
- For corporate entities: pull officer records from the relevant corporate registry (Companies House, ASIC, ACRA, SEC EDGAR, etc.)

Where official records exist, prefer those over secondary sources. University faculty pages and corporate registry records are higher-quality than press articles.

### Step 3: Cross-reference name lists

Take the personnel from each institution and look for names that appear in two or more lists. This is where bridge figures emerge.

If you have small lists, cross-reference visually. If lists are large, drop them into a working file:

```
/home/claude/<thread>/personnel-by-institution.md

- Institution A: [Person 1, Person 2, Person 3, ...]
- Institution B: [Person 4, Person 1, Person 5, ...]
- Institution C: [Person 6, Person 2, Person 7, ...]
```

Names appearing in 2+ rows are bridge candidates.

### Step 4: Verify the bridging role

A bridge candidate becomes a bridge figure only when you can document their *active* role in both contexts. For each candidate:

- What did they do in context A? (cite source)
- What did they do in context B? (cite source)
- Is there evidence they connected the two — introduced a person, transferred a method, moved funds, co-authored work? (cite source)

Record findings in this format:

```markdown
### <Name> (<dates>)

**Context A (<institution>):** <role and dates with citation>
**Context B (<institution>):** <role and dates with citation>
**Bridging act:** <specific documented connection with citation>
**Confidence:** confirmed / high / medium
**Source quality:** primary / reputable secondary / single source
```

### Step 5: Add to graph

Each verified bridge figure becomes a node (`type: "person"`, `category: "bridge_figure"`). Each documented bridging act becomes an edge between the two institutional nodes, with the person as the source/evidence.

```json
{
  "id": "person-id-kebab-case",
  "type": "concept",
  "domain": "AB",
  "term": "Full Name",
  "category": "bridge_figure",
  "properties": {
    "confidence": "confirmed",
    "source": "Specific citations: registry record, biographical source, archival document",
    "lifespan": "YYYY-YYYY",
    "bridging_role": "Brief description of what they bridge and how"
  }
}
```

## What disqualifies a candidate

- **Membership without action** — "attended a conference" alone is weak; "chaired the conference" is strong
- **Coincidence of name** where biographical details don't match (Henry Smith the chemist vs. Henry Smith the financier are different people; verify dates, locations, professional contexts before merging)
- **Modern figures inferred from organisational charts** without documented personal action

## Enhancement: Role-Context Tension Scoring

**Purpose:** Quantify how much a bridge figure's cross-context behavior resists single-framework explanation. High tension indicates compartmentalization; low tension indicates consistent progression.

**Formula:** `tension = (diversity / 5) × discontinuity × avg_documentation`

- **Diversity** (1–5): Number of distinct institutional contexts
- **Discontinuity** (0.0–1.0): Degree roles require different interpretive frameworks  
- **Documentation** (0.4–1.0): Source quality (medium=0.4, high=0.7, confirmed=1.0)

**Interpretation:**
- 0.00–0.25: Low — consistent narrative
- 0.25–0.50: Medium — normal complexity
- 0.50–0.75: High — red flag for investigation
- 0.75–1.00: Critical — immediate priority

**Illustrative Example:** Bridge-figure tension across three archetypes
| Figure | Score | Interpretation |
|--------|-------|----------------|
| Subject A | 0.95 | Critical — roles span four incompatible institutional frameworks |
| Subject B | 0.60 | High — professional fiduciary role crosses firm/client boundary |
| Subject C | 0.24 | Low — consistent single-field professional progression |

**Usage:** Priority score for Phase 2 expansion. Formalizes analyst intuition.

**Source:** WFGY Asymmetric Self-Consistency.

## Negative findings are valuable

If you searched thoroughly and found no bridge figure between two institutions the investigation has linked, that is worth noting. It means the link is institutional or structural rather than personal — which changes how strongly the connection should be characterised.

Record negative findings in the report's "investigations performed" section so future sessions don't re-run them blind. Format:

> Searched for bridge figures between Institution A and Institution B; cross-referenced 23 personnel from A against 41 from B; no name overlap. The institutional link, if it exists, is not personal at the documented-role level.

## Authoritative-source pathway

If the user has direct knowledge of any candidate (the user is the bridge figure; the candidate is a family member, colleague, or close associate), the user can resolve the bridging-role question directly. In that case:

- Surface the candidate to the user with the specific question (e.g., "Did Person X actually introduce these two parties, or was the meeting arranged through a different route?")
- Note that user-source information cannot be auto-promoted to graph (see `epistemic-tiers.md` authoritative-source section)
- If the user provides confirmation and consents to graph inclusion, treat it as a `high`-tier finding pending public-record corroboration, not a `confirmed`-tier finding

User-source information is valuable for direction-setting but does not by itself meet the public-record bar that the graph's credibility depends on.
