---
name: convergence-investigation
description: WFGY-enhanced end-to-end multi-method investigatory pipeline for cross-domain research. Adds WFGY framework integration: role-context tension scoring for bridge-figures, holographic validation for graph updates, tension tier formalism, and S-class taxonomy for structural parallels. Maintains rigorous epistemic-tier discipline while formalizing analyst intuition through quantitative metrics. Use for investigations requiring enhanced pattern recognition and cross-investigation learning.
version: 2.0.0
author: Enhanced from base convergence-investigation
---

# Convergence Investigation Pipeline

A general-purpose research methodology that orchestrates six investigative sub-methods under a strict epistemic-tier discipline and produces a standard deliverable bundle. The skill exists because rigorous research methodologies tend to accrete distinct sub-methods over time (corporate verification, bridge-figure mapping, document parsing, structural-parallel analysis, graph integration, handoff generation), and running them piecemeal across multiple turns wastes effort and breaks continuity. This skill collapses that into one orchestrated pipeline with strong defaults, explicit triage, and an audit gate.

The methodology is project-agnostic. It works equally well for a cross-domain academic investigation, a corporate due-diligence dossier, a journalistic source-mapping exercise, an institutional-history project, or any other research effort that involves multiple sources, multiple methods, and a need for tier-disciplined synthesis.

---

## Operating Principles

These are load-bearing — every output must respect them.

1. **Zero speculative claims in the knowledge graph.** Every node and edge is tiered: `confirmed` (direct evidence), `high` (strong inference from multiple sources), `medium` (single-source or pattern match), or excluded. Speculative material can appear in the report's "open threads" or "candidate findings" sections but never in the graph. This is the credibility gate.

2. **Institutional lineage over isolated overlap.** The strongest findings are chains (Source A → Mediator B → Outcome C), not single-point coincidences. When you find a connection, ask "what's the chain that explains why this connection exists?" before logging it.

3. **Bridge figures are higher-value than institutional links.** Named individuals who personally connect two contexts (a director who chairs both the funding foundation and the recipient programme; a researcher who co-authored work in two otherwise-separate fields) are the single most important class of finding. Always look for them.

4. **Compose, do not duplicate.** This skill calls into existing single-method skills for the work they already cover. It adds orchestration, integration, and synthesis — not new recon primitives. Common companion skills include `web-osint-reconnaissance`, `cross-reference-osint`, `deep-investigate`, or any project-specific research skills present.

5. **File discipline is enforced.** Source artifacts (graphs, prior reports) live in `/mnt/project/` if mounted. Working files in `/home/claude/<thread-name>/`. Final deliverables in `/mnt/user-data/outputs/`. Never write deliverables anywhere else; never edit project source files in place — version them.

6. **Pattern recognition vs. apophenia is named explicitly.** The methodology is built on noticing patterns across domains, but every claim is interrogated for evidence. If you can't articulate the evidence chain, the claim doesn't go in.

---

## The Seven Sub-Methods

Each input triggers a subset of these. The triage step (Phase 1) decides which apply.

| # | Method | Trigger signals | Reference module |
|---|--------|-----------------|------------------|
| 1 | **Structural-parallel documenter** | Two concepts/processes/symbols across domains that may share underlying structure | `references/structural-parallels.md` |
| 2 | **Bridge-figure mapper** | Named individuals appearing in multiple institutional contexts; org charts; foundation directors; conference rosters | `references/bridge-figures.md` |
| 3 | **Government / institutional document parser** | SAM.gov solicitations, regulatory filings, court documents, foundation grant announcements, formal RFIs/RFPs | `references/document-parsing.md` |
| 4 | **Corporate-jurisdiction verifier** | Company names, ambiguous incorporation, footer text containing legal entity suffixes (Pte Ltd, GmbH, Pty Ltd, BV), shell or nominee patterns | `references/corporate-jurisdiction.md` |
| 5 | **Knowledge-graph version updater** | Any new confirmed finding that should join the project graph; always runs at the end if anything was found | `references/graph-integration.md` |
| 6 | **Inter-session handoff generator** | Always runs at the end of a complete investigation; preserves context for the next session | `references/handoff-generation.md` |
| 7 | **Visualization artifact generator** | Graph was updated, multi-entity network surfaced, reusable reference produced, or user requested "complete artifact" / atlas | `references/visualization-artifacts.md` |

Sub-methods 5, 6, and 7 always run if anything substantive was found. Sub-methods 1–4 are selected by triage.

---

## Phase 1: Intake and Triage

Read the input carefully before doing anything. The input may be:
- A URL (corporate site, news article, government doc, video)
- A document (uploaded PDF, transcript, screenshot, image)
- A named entity (person, company, programme, institution, paper)
- A research thread (an open question from a prior handoff or memory)
- A video Claude cannot access — in which case ask the user to describe contents before proceeding

### Step 1a: Ask for triggering context if absent

If the input arrives with no context — just a URL or a name and nothing else — **ask for context before launching the full pipeline**. One short question costs little and saves a full investigation pass when the target turns out to be peripheral, a test case, or different from what the methodology assumes.

The question to ask depends on the input type but should be framed to elicit:
- Why this surfaced for the user (where did it come from?)
- What outcome they want (deep dive, quick confirmation, integration with existing project, one-off lookup)
- Whether they have authoritative-source knowledge of the target (see Phase 2.5)

If the user supplies context proactively, skip this step and proceed.

### Step 1b: Check the project state

If a `/mnt/project/` directory is mounted with prior artifacts (knowledge graph, previous reports, existing skills):

1. View `/mnt/project/` to identify the current graph version and any reports relevant to the input
2. Mentally check `userMemories` (if available) for related prior findings — if the user has already established a fact, don't re-derive it
3. Run `conversation_search` if the input references prior work that may not be in current memories

### Step 1c: Decide which sub-methods apply

Be concrete — write a one-line triage statement before starting:

> **Triage:** Input is a government solicitation URL → document parser (3) + bridge-figure mapper (2, for the programme manager) + graph updater (5) + handoff (6). Skip 1 and 4.

If you find yourself wanting to apply all six methods to a thin input, that's a signal to narrow rather than broaden — pick the two most relevant.

---

## Phase 2: Parallel Sub-Investigations

Run the selected sub-methods. Where they don't depend on each other, fire the relevant tool calls in parallel. Where one depends on another (e.g., bridge-figure mapping depends on first identifying named individuals from document parsing), sequence them.

For each sub-method, **load the corresponding reference module** before running it. The reference modules contain the specific procedures, output schemas, and quality gates for that method. Do not improvise — the methodology has been calibrated through use.

Throughout, record findings to a working file at `/home/claude/<thread-name>/findings.md` with each claim tagged by tier. This becomes the source of truth for Phase 3.

When composing with existing skills:
- For website recon → check for `web-osint-reconnaissance` or analogous skill at `/mnt/skills/user/`
- For graph schema and intersection mapping → check for `cross-reference-osint` or analogous
- For ToS / corporate / monetisation deep dives → check for `deep-investigate` or analogous
- For domain-specific knowledge → check for any project-specific research skill

If a needed companion skill isn't present, run the methodology inline using the reference modules.

---

## Phase 2.5: Authoritative-Source Pathway

If the user has personal knowledge of the target (they are the target; the target is a family member, colleague, or someone they have direct contact with; they hold a role at the target organisation), the OSINT methodology shifts. For each candidate finding produced by Phase 2:

- Ask: "is this resolvable by the user's direct query rather than by further public-record evidence?"
- If yes, flag the finding as **resolvable-by-source** in the report and surface the question to the user
- Note the privacy boundary: information the user provides from personal knowledge sits outside the project's public-record-based discipline. Such information may be reflected in the report but **must not be auto-promoted to the project knowledge graph without the user's explicit consent**

The authoritative-source pathway turns OSINT-from-distance into hypothesis verification. It does not replace public-record investigation; it augments it. Public records remain the primary evidence base for the graph.

---

## Phase 3: Synthesis

Once the sub-investigations are complete, synthesise into the standard project deliverable bundle. Always produce the following — even if some sections are short:

### A. Updated knowledge graph (JSON)

- Copy the current graph file from `/mnt/project/` (or wherever the project source lives) to `/home/claude/<thread-name>/graph-vN.M.json` where `N.M` is the next version
- Add only `confirmed` and `high` confidence nodes/edges; route `medium` to the report's "candidate findings" section for user review before graph promotion
- Recompute `metadata.stats` programmatically (don't hand-edit counts)
- Validate that no node has `confidence: "speculative"` before saving
- See `references/graph-integration.md` for the full procedure

### B. Investigation report (Markdown)

Use this exact template — it is the project's standard format and consistency matters for downstream reading:

```
# Research Update: <Thread Name>
## <Date> — <Trigger Description>

**Triggered by:** <input description, including any context the user supplied or didn't>

**Sub-methods applied:** <which of the six were triggered by triage>

**Authoritative-source note:** <only if Phase 2.5 was activated — describe the user's relationship to the target and the privacy framing applied>

---

## THREAD <LETTER>: <Topic> — <One-line headline finding>

**Finding:** <Headline finding in one paragraph>

### <Subsection per investigation arm>
<Structured content with confidence tiers in [BRACKETS] inline>

### Significance
<Why this matters; what it changes; what it confirms or refutes; if an internal project graph exists, what it would update>

### Graph actions
<Bulleted list of exact node/edge additions or updates — or "none" if no graph-worthy findings>

---

## Candidate findings (medium tier — for user review)

<Bulleted list of medium-tier findings that did not enter graph; what would upgrade them>

## Investigations performed (negative findings)

<List of things searched that returned no useful result. Prevents future sessions from re-running blind.>

## Apophenia audit

<Checklist of the five audit checks; brief note on each>

## Next priorities

<Numbered list, ranked>
```

Save to `/home/claude/<thread-name>/research-update-<DD-month-YYYY>.md`.

### C. Comparison tables (only if structural-parallels method ran and produced a parallel)

If sub-method 1 produced a parallel that met the methodology bar, generate a formal comparison document:
- One section per parallel
- Side-by-side table: Domain A column | Domain B column | Structural element being compared | Citations
- Confidence tier per row
- Closing assessment: "novel / previously identified / partial overlap with [prior work] / refuted by prior work"
- A counter-position paragraph stating the strongest case against the parallel

Output as `.docx` using the `docx` skill (read `/mnt/skills/public/docx/SKILL.md` first). Save to `/mnt/user-data/outputs/`.

### D. Handoff document (Markdown)

Generated by sub-method 6. Always produced. Structure specified in `references/handoff-generation.md`. Save to `/mnt/user-data/outputs/`.

### E. Visualization artifacts (HTML / React / SVG)

Generated by sub-method 7. Produced whenever the investigation updated the graph, surfaced an entity network, produced reusable reference material, or the user asked for a "complete artifact." Standard patterns include the interactive D3.js knowledge graph, the React entity-network pinboard, dark-aesthetic HTML reference cards, and the comprehensive research atlas. Specified in `references/visualization-artifacts.md`. Save to `/mnt/user-data/outputs/`.

The visualization is what turns the JSON graph and Markdown report into something the user can navigate. It is not optional except in the explicit null-visualization case (narrative-only findings with no entity structure worth seeing).

---

## Phase 4: Delivery

1. Move final deliverables (graph JSON, report MD, visualizations, comparison docx if any, handoff MD) to `/mnt/user-data/outputs/`
2. Call `present_files` with the deliverables in this order:
   - Handoff (high-level summary)
   - Report (full findings)
   - Atlas HTML if produced (most navigable single artifact)
   - Knowledge graph HTML if produced separately
   - Pinboard JSX if produced
   - Reference card HTML if produced
   - Comparison docx if structural parallels were found
   - Graph JSON (machine-readable)
3. In the chat response: lead with the headline finding (one paragraph), then list what was produced and key actions the user should take next. Briefly note which visualization to open first based on what the user is most likely to want to explore.
4. Keep the chat response short — the artifacts carry the detail
5. If Phase 2.5 was activated and there are resolvable-by-source candidates, end the chat response with the targeted question(s) the user could answer to upgrade the candidates

---

## When NOT to Use This Skill

- **Single-point lookups**: "what year was Company X founded?" — answer directly
- **Clarifying existing findings**: Answer from memory or graph without re-running full pipeline
- **Purely creative/generative tasks**: Writing poems, building UI from scratch — not supported
- **Single-sub-method needs**: If only one method is needed (e.g., only document parsing), call that sub-method directly
- **Explicit scoping requests**: When user says "just X" or "no graph update needed" — respect constraints
- **Non-consented research**: Individuals who haven't consented to being researched, outside legitimate journalism/legal process/self-OSINT
- **Low-confidence triggers**: Vague queries like "tell me about X" without context — ask for clarification first
- **Peripheral targets**: When user provides only a name with no stated connection to their research goals
- **Time-sensitive decisions**: Real-time decisions requiring immediate response — methodology is for deep investigation

### Enhanced Conditions (v2.0+)
- **Avoid over-chaining**: Do not trigger all 6 sub-methods for simple queries
- **Respect privacy boundaries**: Personal knowledge (Phase 2.5) must not auto-promote to graph without explicit consent
- **No speculative graph updates**: Never add "medium" or "low" confidence nodes to the knowledge graph

---

## The Apophenia Audit

Before saving any artifact, run a quick internal audit pass:

1. **Tier check:** Is every claim tagged with a confidence level? Any untagged claims are speculative by default and must be removed or tagged.
2. **Bridge-figure check:** Did you look for named individuals? If the topic involves institutions and you found zero people, you probably missed something — search again.
3. **Chain check:** Does your strongest finding form a chain with prior graph nodes (or with itself coherently), or is it an isolated coincidence? Isolated findings are weaker; consider whether to log them.
4. **Counter-evidence check:** Did you actively search for evidence that would refute the finding? If not, do one targeted search before publishing.
5. **Novelty check:** For structural parallels, search for prior published identification before claiming novelty. If you find any prior work, downgrade the claim.

If any check fails, fix it before delivery. The credibility of these tiers is load-bearing — once an unreviewed speculative claim makes it into the graph, the whole graph's trust value drops.

---

## File Layout (canonical)

```
/mnt/project/                                 # Read-only project source (if mounted)
  <project>-knowledge-graph.json
  prior-research-update-*.md
  prior-handoff-*.md
  ...

/home/claude/<thread-name>/                   # Working scratch
  findings.md
  graph-v<N.M>.json
  research-update-<date>.md
  comparison-tables.md (pre-docx)
  handoff-draft.md

/mnt/user-data/outputs/                       # Final deliverables
  research-update-<date>.md
  graph-v<N.M>.json
  parallels-<topic>.docx (if any)
  handoff-<date>.md
```

---

## Reference modules

Load these on demand as the triage step indicates:

- `references/structural-parallels.md` — Cross-domain comparison tables and novelty assessment
- `references/bridge-figures.md` — Finding the named persons who connect institutions
- `references/document-parsing.md` — Government / institutional document extraction
- `references/corporate-jurisdiction.md` — Footer signal → registry confirmation
- `references/graph-integration.md` — Versioned JSON graph extension rules, holographic validation
- `references/handoff-generation.md` — Inter-session handoff document structure
- `references/visualization-artifacts.md` — Interactive HTML graphs, React pinboards, reference cards, atlases
- `references/epistemic-tiers.md` — Confidence tier definitions, promotion rules, tension formalism
- `references/s-class-taxonomy.md` — WFGY 3.0 structural parallel classification vocabulary

Each is short and self-contained. Read them when the corresponding sub-method runs.

### WFGY Framework Integration

The convergence methodology integrates validated enhancements from the WFGY (Wisdom Framework of the Great Year) theoretical framework:

| WFGY Concept | Enhancement | Reference |
|--------------|-------------|-----------|
| Asymmetric Self-Consistency | Role-context tension scoring for bridge-figures | `references/bridge-figures.md` |
| Semantic Entropy | Tension tier formalism for borderline claims | `references/epistemic-tiers.md` |
| Semantic Holography | Holographic validation audit for graph updates | `references/graph-integration.md` |
| 131 S-Class Set | Structural parallel taxonomy | `references/s-class-taxonomy.md` |

These enhancements formalize analyst intuition, provide quantitative prioritization scores, and enable cross-investigation pattern recognition. All are optional — the core methodology functions without them.

---

## Example walkthrough (synthetic)

A user supplies the URL of a small UK private limited company and an associated email address, with no further context.

**Phase 1a (ask for context):** Reply asking what brought this target into view — is it a counterparty in a transaction, a name from research, a self-OSINT exercise, etc.

**Phase 1c (triage):** Once context is supplied, decide: corporate-jurisdiction verifier (4) for the company, bridge-figure mapper (2) for the directors and PSCs, with graph integration (5) and handoff (6) on standby. Skip document parsing (3) and structural parallels (1) — no signal.

**Phase 2 (parallel investigation):** Fetch Companies House overview, officers, persons of significant control, and full director appointment history. Search for the directors' professional profiles and prior appointments. Cross-reference for any pattern (nominee directors, shell-hopping, mismatched parent/subsidiary).

**Phase 2.5 (authoritative source):** If the user has direct knowledge of the target (e.g., they are the director, or related to them), surface candidate findings as resolvable-by-source rather than treating them as needing more public-record evidence.

**Phase 3 (synthesis):** Produce the report following the template; produce a handoff. If no findings reached confirmed/high tier, the graph holds at its current version with candidates staged for user review.

**Phase 3.5 (WFGY enhancement):** Optional — apply validated WFGY framework enhancements:
- **Role-context tension scoring** for bridge-figures (see `references/bridge-figures.md`)
- **Holographic validation** audit before major graph updates (see `references/graph-integration.md`)
- **Tension tier formalism** for borderline claims (see `references/epistemic-tiers.md`)
- **S-class taxonomy** for structural parallels classification (see `references/s-class-taxonomy.md`)

These enhancements formalize analyst intuition, provide quantitative prioritization scores, and enable cross-investigation pattern recognition.

**Phase 4 (delivery):** Present the artifacts. Lead with the headline finding in chat, list the files, surface any authoritative-source questions for the user to consider.

The example above does not produce a graph update or a comparison docx — and that is the correct outcome when the input doesn't meet the bar. The discipline that returns "nothing met the bar" is harder than the discipline that returns "here's what I found." The skill is designed to do both correctly.
