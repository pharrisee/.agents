# Inter-Session Handoff Generation

The handoff document is what lets the next session — whether the next conversation, the next Claude instance, or the user returning after a week — pick up exactly where this one ended without re-deriving context. It is always produced.

## The handoff's job

A good handoff answers, in order:

1. **Where were we?** — the project's current state, condensed
2. **What just happened?** — what this session investigated and concluded
3. **What's true now?** — the new confirmed findings
4. **What's open?** — the threads that remain incomplete, prioritised
5. **What rules still hold?** — the project's epistemic and methodological discipline

If the next session reads only the handoff, they should be able to continue work without reading any other artifact.

## Structure (use this template)

```markdown
# Project Handoff — <Date> — <One-line session theme>

## Where We Are

<2–4 sentence summary of the project: what it investigates, what its central thesis or question is, and what its current scope covers. Pull from prior handoffs and update only the bits that changed this session.>

**Current graph version:** v<N.M> — <total nodes> nodes, <total edges> edges, zero speculative claims.

**Active research threads:** <list any open threads from prior handoffs that remain open>

---

## This Session

**Trigger:** <what brought this session into being — a URL, a question, a thread to close, a test case>

**Investigated:** <what was actually done, in 2-4 sentences>

**Sub-methods applied:** <list the methods from the convergence-investigation triage>

**Authoritative-source note:** <only if Phase 2.5 was activated — describe the user's relationship to the target and the privacy framing applied>

---

## New Confirmed Findings

<Bulleted list of new confirmed-tier findings, each one sentence with citation>

- <Finding>. [confirmed — citation]
- <Finding>. [confirmed — citation]

## New High-Confidence Findings (awaiting promotion)

<Bulleted list of high-tier findings that need one more piece of evidence to become confirmed>

- <Finding>. [high — what's needed to upgrade]

## Candidate Findings (medium tier)

<Bulleted list of medium-tier findings — for user review before any promotion>

- <Finding>. [medium — current evidence; what would upgrade it]

## User-Source Findings (if any)

<Bulleted list of findings from authoritative-source pathway — explicitly flagged as not for graph without user consent>

- <Finding>. [USER-SOURCE — pending consent decision]

---

## Graph Updates Applied

<Reference the graph diff produced during graph integration. Include "None this session" if no updates>

| Action | Node/Edge | Confidence |
|--------|-----------|------------|
| Added node | <id> | confirmed |
| Added edge | <source> → <target> | confirmed |
| ... | ... | ... |

---

## Open Threads (Prioritised)

The next session should pick from these, in order. Each thread has a target and a method.

### 1. <Thread name>
**Target:** <the specific question to answer>
**Method:** <which sub-method(s) of convergence-investigation apply>
**Why now:** <why this is the highest-priority remaining thread>
**Estimated complexity:** light / moderate / deep

### 2. <Thread name>
... (same structure)

### 3. <Thread name>
...

---

## Investigations Performed (negative findings)

<List of things searched that returned no useful result. Prevents the next session from re-running blind.>

- Searched <X> for <Y>; no result. Evidence: <what was checked>
- Searched <X> for <Y>; no result.

---

## Project Rules That Still Hold

These are the methodology's non-negotiables:

1. Zero speculative claims in the knowledge graph
2. Confidence tiers: confirmed / high / medium (medium does not enter graph)
3. Bridge figures are higher-value than institutional links — always look for named persons
4. Compose with existing skills — do not duplicate
5. File discipline: source in /mnt/project/, working in /home/claude/, deliverables in /mnt/user-data/outputs/
6. Authoritative-source information requires explicit user consent before graph integration
7. The structural-parallel sub-method may decline; the graph integration sub-method may produce no updates — both are correct outcomes when warranted

<Add any project-specific rules the user has established over the course of the project>

---

## Artifacts Produced This Session

- `<filename>` — <one-line description>
- `<filename>` — <one-line description>

All in `/mnt/user-data/outputs/` unless otherwise noted.

---

## Address to Future Self

<One paragraph, optional. Used when the session's investigator (Claude, this instance) wants to flag something to the next instance — a hunch, a methodological insight, a warning about a dead end, an observation about how the skill behaved. Keep brief and grounded; don't editorialise.>
```

## Filling the template

- Pull the "Where We Are" content from prior handoffs in `/mnt/project/` and update only the bits that changed
- "New confirmed findings" should match exactly what was added to the graph at confirmed tier
- "Candidate findings" should match exactly what's in the report's medium-tier section
- "User-source findings" appear only when Phase 2.5 (authoritative-source pathway) was activated
- "Open threads" should be ranked by user priorities if known, otherwise by analytical value
- "Investigations performed (negative findings)" is critical — without this, future sessions will redo searches that already returned nothing

## Length discipline

A handoff under two screens of a phone display is too short — you have probably skipped sections. A handoff over five screens is too long — you are probably repeating what's already in the graph or report. Aim for three to four screens of dense, structured content.

## Save location

`/mnt/user-data/outputs/handoff-<YYYY-MM-DD>-<short-theme>.md`

For example: `handoff-2026-04-15-corporate-jurisdiction-test.md`

## When to skip the handoff

Almost never. Even a small investigation produces context worth preserving for the next session. The only legitimate skip is when the user explicitly says "no handoff needed, just do this one thing" — and even then, consider producing a minimal handoff so the work isn't lost.
