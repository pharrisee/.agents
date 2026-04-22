# Epistemic Tiers — Confidence Discipline

The credibility of any investigation that uses this methodology depends on these tiers being applied consistently. This is not bureaucratic — when a claim labelled `confirmed` actually is verifiable, the whole graph and report system retains its trust value. When it isn't, the system collapses.

## The four tiers

### `confirmed`
Direct primary-source evidence. The claim is verifiable by anyone who follows the citation. Examples of confirmation-grade evidence:
- A name appears in an official corporate registry record (Companies House, SEC EDGAR, ACRA, etc.)
- A paper is on arXiv, in a peer-reviewed journal, or on a publisher's official site with the stated authorship
- A government document is published on an official agency site with the stated parameters
- A statute appears verbatim in an official legislative database
- A named individual appears on the official roster of an institution with the stated role

For `confirmed`, the citation must be a primary source, or a reputable secondary source that itself cites the primary and that you have verified. Wikipedia is acceptable for `confirmed` *if* the Wikipedia claim itself has a citation that you have verified, OR for facts that are uncontroversial and well-attested across multiple sources.

### `high`
Strong inference from multiple independent sources, or a single very-strong indirect indicator. Examples:
- "Company X is incorporated in Country Y" based on a website footer reading `© Company X <Country-specific entity suffix>` — `high` until the country's corporate registry confirms, then upgrade to `confirmed`
- A bridge figure connection where the individual is documented in both contexts but no source explicitly states the bridging role
- A funding relationship inferred from coincident timing and mutual mention but not explicitly disclosed in public records

`high` is the working tier for inferences you would defend in argument but have not formally verified.

### `medium`
Single-source claim, pattern match without direct corroboration, or a reasonable inference from circumstantial evidence. Examples:
- A surname match suggesting a family connection
- A URL pattern guess based on platform conventions
- A claim from a single non-authoritative source
- Geographic adjacency suggesting institutional relationship

`medium` claims **do not enter the knowledge graph** — they go in the report's "candidate findings" section and stay there until they are either upgraded with new evidence or dropped. Medium claims are valuable working hypotheses; they are not findings.

### excluded (formerly called `speculative`)
Claims that would require the analyst's interpretation to be persuasive. Conjecture, "wouldn't it be interesting if," patterns visible only after the fact, theories that fit the available facts but are not entailed by them. These do not appear in graph or report unless explicitly framed as "open question for future investigation" in the report's open-threads section.

## The promotion ladder

A claim moves up tiers as evidence accumulates:
- `medium` → `high` when a second independent source corroborates
- `high` → `confirmed` when a primary source verifies the specific claim, not just the surrounding context

Downgrades happen too: if a counter-source emerges, the claim's tier drops or the claim is removed. Graph nodes that get downgraded should be moved to the report's "retracted findings" section so the audit trail is preserved.

## Tagging in artifacts

In the graph JSON: `"confidence": "confirmed"` (etc.) on each node and edge.

In Markdown reports: tag inline in square brackets at the end of the sentence:

> Company X appears to be incorporated in Country Y based on the legal entity suffix in its website footer. [HIGH — based on website footer; needs registry confirmation to upgrade]

In the handoff document: maintain a "candidate findings" list of all `medium` claims awaiting promotion.

## The audit gate

Before any graph save, run a quick check that no speculative material is in the graph:

```python
import json

with open('graph-vN.M.json') as f:
    g = json.load(f)

bad_tiers = ('speculative', 'low', None, 'unknown', '')
spec = [n['id'] for n in g['nodes']
        if n.get('properties', {}).get('confidence') in bad_tiers]

assert not spec, f'Speculative or untagged nodes found: {spec}'
print(f'Audit OK — {len(g["nodes"])} nodes all tier-tagged')
```

If this fails, the graph is not ready for save. Fix the offending nodes and re-run.

## Enhancement: Tension Tier Formalism

**Purpose:** Map discrete epistemic tiers to continuous "tension" scores using WFGY framework, providing granularity for borderline cases.

**Tension Theory:**
Tension represents epistemic stress — how much a claim resists confident tier assignment.

| Tier | Tension Range | Description |
|------|---------------|-------------|
| `confirmed` | 0.00-0.20 | No epistemic stress. Direct evidence. |
| `high` | 0.20-0.40 | Low tension. Strong inference, promotion likely. |
| `medium` | 0.40-0.60 | Elevated tension. Single source, needs corroboration. |
| `excluded` | 0.60-1.00 | High tension. Conjecture/speculation. |

**Application:** For borderline claims (e.g., a high-tier finding at 0.35 tension — nearly promotable to `confirmed`), tension scores guide investigation prioritization.

**Implementation:**
```json
{
  "id": "finding-example",
  "properties": {
    "tier": "high",
    "tension_score": 0.35,
    "promotion_path": "Primary source citation needed"
  }
}
```

**Benefit:** Formalizes analyst intuition about "how close" a claim is to tier promotion.

**Note:** Tension is supplementary to tier, not replacement. Discrete tiers remain primary.

**See also:** `bridge-figures.md` for role-context tension scoring methodology.

## Authoritative-source information

When the user has direct knowledge of a target and shares it (e.g., personal recollection, internal documents not in public record, family knowledge), this information sits **outside** the public-record-based tier system. Such information:

- May be reflected in the report with explicit attribution to user-source
- Should be tagged `[USER-SOURCE — not for graph]` in the report
- Must not be auto-promoted to the project knowledge graph without the user's explicit consent
- Triggers a privacy framing: even with consent, consider whether the third party (if any) would expect this information to be made part of a persistent research artifact

This is the discipline that keeps the graph defensible to outside readers while still letting investigations benefit from inside knowledge during analysis.
