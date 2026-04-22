# Structural Parallels — Building the Comparison Tables

This methodology produces structured, defensible cross-domain comparisons rather than apophenic free-association. The bar is high: most candidate parallels do not survive the procedure, and that is a feature, not a bug.

## When this method applies

A structural parallel is a claim that two processes, symbols, or concepts from different domains share the same underlying *structure* — not merely surface-level vocabulary or thematic resonance. The pattern must:

1. **Map element-by-element** (A1 ↔ B1, A2 ↔ B2, A3 ↔ B3) with at least three corresponding elements
2. **Preserve the relational structure** — if A1 *causes* A2, then B1 should *cause* B2; if A1 *is contained in* A2, then B1 should *be contained in* B2
3. **Be articulable independently in both domains** — neither domain requires the other's framing to make sense; an outside reader familiar with only one domain would still recognise the elements

If you can only get one or two corresponding elements, it is resonance, not parallel. Note it in the open-threads section but do not formalise it.

## Procedure

### Step 1: State the candidate parallel in one sentence

> "Process X in Domain 1 is structurally parallel to Process Y in Domain 2."

If you cannot say it in one sentence, the parallel is not crisp enough yet. Refine before proceeding.

### Step 2: Decompose each side into its structural elements

For each domain, list the elements of the process or symbol — the discrete steps, components, or phases. Keep them at the same level of abstraction (do not list "the entire molecular cascade" on one side and "step 1 of the ritual" on the other).

| Process X (Domain 1) | Process Y (Domain 2) |
|----------------------|----------------------|
| Element X.1 | Element Y.1 |
| Element X.2 | Element Y.2 |
| Element X.3 | Element Y.3 |
| Element X.4 | Element Y.4 |

If you can fill the table with three or more rows where each row has a defensible correspondence, proceed. If you can only fill two rows, abandon.

### Step 3: Identify the structural relation

What is the underlying invariant? Articulate it in domain-neutral terms — i.e. without using either domain's vocabulary.

> *Pattern: A bounded, ritualised intervention transitions an entity from a constrained state into a less-constrained state from which broader future trajectories become available.*

The domain-neutral statement is the parallel's actual claim. If you can write it without losing meaning, the parallel has substance. If the domain-neutral phrasing sounds vacuous or could describe almost anything, the parallel is too weak.

### Step 4: Build the formal comparison table

Use this exact schema for the deliverable:

| Element | Domain 1 instance | Domain 2 instance | Citation 1 | Citation 2 | Tier |
|---------|-------------------|-------------------|------------|------------|------|
| Initial state | <name + brief description> | <name + brief description> | [primary source] | [primary source] | confirmed |
| Intervention | <name + brief description> | <name + brief description> | [primary source] | [primary source] | confirmed |
| Outcome | <name + brief description> | <name + brief description> | [primary source] | [primary source] | high |
| ... | ... | ... | ... | ... | ... |

Each row is a tier-tagged claim. **The whole parallel inherits the lowest tier of any row.** If any row is `medium`, the whole parallel is `medium`. If any row is excluded, the whole parallel collapses.

### Step 5: Novelty assessment

Before claiming the parallel is novel, search:
- Google Scholar for any paper that has identified this parallel
- Domain-specific journals or magazines for prior discussion
- General web search using both domains' technical vocabulary together

Mark the parallel as one of:
- **Novel** — no prior identification found in any source
- **Partial overlap** — prior work identifies a related but not identical parallel
- **Previously identified** — prior work makes substantially the same claim
- **Refuted** — prior work has considered and rejected this parallel

Document what you searched and what you found, even if nothing. This protects against re-discovery later, and against overclaiming novelty when prior work exists.

### Step 6: Counter-position

Write one paragraph stating the strongest case *against* the parallel. What disanalogies exist? What would a skeptic point to? Include this in the comparison document — it is how the work earns trust.

A common failure mode: the analyst convinces themselves of a parallel and then writes a counter-position that is too weak. If the counter-position is genuinely weak, the parallel is genuinely strong; the test is whether you can articulate a good-faith objection.

## Output format

Use the `docx` skill (`view /mnt/skills/public/docx/SKILL.md` first) to produce a `.docx` titled `parallels-<topic>.docx`. Structure:

1. **Executive summary** — one paragraph per parallel
2. **Per-parallel section:**
   - One-sentence statement
   - Decomposition tables (both domains)
   - Domain-neutral structural invariant statement
   - Formal comparison table with citations and tiers
   - Novelty assessment with searches performed
   - Counter-position
3. **References** — full citations for all primary sources

Save to `/mnt/user-data/outputs/parallels-<topic>.docx`.

## What disqualifies a parallel

- **Surface vocabulary overlap only** — both domains using the word "architecture" is not a structural parallel; it's shared metaphor at most
- **One- or two-element matches dressed up as multi-element** by inflating elements (e.g., splitting one element into three sub-elements just to fill the table)
- **Parallels that require both domains to be read through a third interpretive frame** (e.g., "both X and Y can be read as instances of the universal Z principle, therefore X and Y are parallel")
- **Parallels where the Domain 2 side is itself contested or interpretive** — if the basic facts about Domain 2 are disputed, building a parallel on top of them is unsound
- **Parallels where the relational structure is not preserved** — e.g., the elements correspond, but in Domain 1 the relation is causal succession and in Domain 2 it is mere temporal sequence

## When the method declines

It is acceptable — and often correct — for the structural-parallel sub-method to attempt a candidate and reject it. The methodology produces a clear "no parallel meets the bar" outcome, which is a valuable finding in its own right. Record the attempt and the reasoning in the report under "structural-parallel sub-method (declined)" so the next session does not re-attempt the same comparison.

The discipline that returns "the parallel does not hold" is harder than the discipline that returns "here is a parallel." Both are needed.
