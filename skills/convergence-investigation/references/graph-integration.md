# Graph Integration — Versioned Updates with Epistemic Discipline

The knowledge graph is a project's primary durable artifact. Updating it well is a precision activity: every change is auditable, no version is overwritten, and the tier discipline (see `epistemic-tiers.md`) is non-negotiable.

## Versioning rules

- The current source-of-truth graph lives in `/mnt/project/<project-name>-knowledge-graph.json` (or wherever the project source files are mounted)
- That file is **read-only** from this skill's perspective — never edit it in place
- New work produces a versioned successor: `graph-v<major>.<minor>.json` in `/home/claude/<thread-name>/` first, then promoted to `/mnt/user-data/outputs/` on delivery
- The user will move the new version into `/mnt/project/` manually if approved
- Increment minor version for additions / refinements (v3.1 → v3.2)
- Increment major version for schema changes or large structural reworks (v3.x → v4.0)

If no project graph file exists yet (first-time use), create the initial graph from scratch using the schema documented in this file. Save as `graph-v1.0.json`.

## Standard graph schema

```json
{
  "metadata": {
    "target": "Brief description of the project's central question",
    "domain_a": "Description of the primary domain",
    "domain_b": "Description of the secondary domain (if cross-domain project)",
    "created": "ISO-8601 datetime",
    "last_updated": "ISO-8601 datetime",
    "analyst_notes": "Brief context on the methodology or current state",
    "stats": {
      "total_nodes": 0,
      "domain_a_nodes": 0,
      "domain_b_nodes": 0,
      "intersection_nodes": 0,
      "total_edges": 0,
      "confidence_distribution": {
        "confirmed": 0,
        "high": 0,
        "medium": 0,
        "speculative": 0
      }
    }
  },
  "nodes": [],
  "edges": [],
  "osint_outputs": {
    "predicted_urls": [],
    "search_dorks": [],
    "glossary": []
  }
}
```

For single-domain projects, omit `domain_b` and `intersection_nodes` from stats.

## The standard update procedure

### Step 1: Load and snapshot

```python
import json, copy

with open('/mnt/project/<project-name>-knowledge-graph.json') as f:
    graph = json.load(f)

# Working copy
new_graph = copy.deepcopy(graph)
```

### Step 2: Add nodes

For each new finding that meets `confirmed` or `high` tier, construct a node matching the existing schema exactly:

```python
new_node = {
    "id": "kebab-case-id",            # must be unique; check existing IDs
    "type": "concept",                # or "intersection" for cross-domain nodes
    "domain": "A",                    # "A" / "B" / "AB" for cross-domain projects
    "term": "Human-readable Term",
    "aliases": ["Alt name", "Abbrev"],
    "category": "category_string",    # existing categories preferred for consistency
    "properties": {
        "sequence_position": None,
        "url_pattern": None,
        "confidence": "confirmed",    # confirmed | high | medium (medium NOT added to graph)
        "source": "Specific citation or source description"
    }
}

# Conflict check
existing_ids = {n['id'] for n in new_graph['nodes']}
assert new_node['id'] not in existing_ids, f"Duplicate ID: {new_node['id']}"

new_graph['nodes'].append(new_node)
```

### Step 3: Add edges

Edges encode the structural relationships. Use existing edge types where possible to keep the graph queryable:

| Relationship | Meaning |
|--------------|---------|
| `co_occurs_with` | Two nodes appear in the same context (e.g., person attended conference) |
| `sequence_next` | Temporal sequence (institution A → successor institution B) |
| `contains` | Parent/child structural containment |
| `maps_to` | Used for cross-domain intersection nodes |
| `funds` | Financial relationship |
| `directs` | Person directs institution |
| `cites` | One work cites another |
| `bridges` | Person bridges two institutions (use sparingly, for high-value bridge figures) |
| `derives_from` | Intellectual or methodological lineage |

```python
new_edge = {
    "source": "node-id-1",
    "target": "node-id-2",
    "relationship": "bridges",
    "weight": 0.95,
    "evidence": "Specific citation or short evidence statement"
}
new_graph['edges'].append(new_edge)
```

Validate that source and target IDs exist in the node list before appending.

### Step 4: Recompute metadata stats

Never hand-edit the stats block. Recompute programmatically:

```python
from collections import Counter
from datetime import datetime, timezone

stats = {
    "total_nodes": len(new_graph['nodes']),
    "total_edges": len(new_graph['edges']),
    "confidence_distribution": dict(Counter(
        n.get('properties', {}).get('confidence', 'unknown')
        for n in new_graph['nodes']
    ))
}

# For cross-domain projects, also compute domain breakdown
if any(n.get('domain') in ('A', 'B', 'AB') for n in new_graph['nodes']):
    stats.update({
        "domain_a_nodes": sum(1 for n in new_graph['nodes'] if n.get('domain') == 'A'),
        "domain_b_nodes": sum(1 for n in new_graph['nodes'] if n.get('domain') == 'B'),
        "intersection_nodes": sum(1 for n in new_graph['nodes'] if n.get('domain') == 'AB'),
    })

new_graph['metadata']['stats'] = stats
new_graph['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
```

### Step 5: Audit before save

Run the discipline gate from `epistemic-tiers.md`:

```python
# Zero speculative tolerance
bad_tiers = ('speculative', 'low', None, 'unknown', '')
spec_nodes = [n['id'] for n in new_graph['nodes']
              if n.get('properties', {}).get('confidence') in bad_tiers]
assert not spec_nodes, f"Speculative or untagged nodes: {spec_nodes}"

# Edge integrity
node_ids = {n['id'] for n in new_graph['nodes']}
orphan_edges = [(e['source'], e['target']) for e in new_graph['edges']
                if e['source'] not in node_ids or e['target'] not in node_ids]
assert not orphan_edges, f"Edges reference missing nodes: {orphan_edges}"

# No duplicate IDs
ids = [n['id'] for n in new_graph['nodes']]
assert len(ids) == len(set(ids)), f"Duplicate node IDs: {[i for i in ids if ids.count(i) > 1]}"

print("Audit OK")
```

### Step 6: Save versioned

```python
# Determine new version number based on existing
current_version = "v3.1"  # read from metadata or filename
new_version = "v3.2"      # increment minor for additions

out_path = f'/home/claude/<thread-name>/graph-{new_version}.json'

with open(out_path, 'w') as f:
    json.dump(new_graph, f, indent=2, ensure_ascii=False)

print(f"Saved {out_path} — {stats['total_nodes']} nodes, {stats['total_edges']} edges")
```

### Step 7: Diff for the report

Generate a human-readable diff for the report:

```python
old_ids = {n['id'] for n in graph['nodes']}
new_ids = {n['id'] for n in new_graph['nodes']}
added = sorted(new_ids - old_ids)

old_edges = {(e['source'], e['target'], e['relationship']) for e in graph['edges']}
new_edges = {(e['source'], e['target'], e['relationship']) for e in new_graph['edges']}
added_edges = sorted(new_edges - old_edges)

print(f"Added {len(added)} nodes, {len(added_edges)} edges")
for nid in added:
    n = next(x for x in new_graph['nodes'] if x['id'] == nid)
    print(f"  + {nid}: {n['term']} [{n['properties']['confidence']}]")
```

Drop this diff into the report's "Graph Updates" section.

## What does NOT go in the graph

- Anything tier `medium` or below — goes in report's "candidate findings" instead
- Sub-method working data (raw search results, intermediate inferences)
- The analyst's hypotheses about what a finding means — record those as report prose
- User-source information (provided from personal knowledge by an authoritative-source user) — requires explicit user consent before graph integration; even then, treat with care

## The null-update pathway

It is acceptable — and often correct — for an investigation run to produce no graph updates. If no findings reached confirmed or high tier:

- Skip the version increment
- Note in the report's "Graph actions" section: "None — graph remains at vN.M; candidate findings staged in report for user review"
- Still produce the handoff document and any other deliverables

This is the discipline that prevents graph drift. An investigation that runs but adds nothing to the graph is not a failed investigation; it is a successful one that correctly held the bar.

## What if the graph schema needs to change?

Schema changes mean a major version bump. Before changing the schema:

1. Document the proposed change in a `schema-change-proposal.md` in the working directory
2. Identify which existing nodes/edges need migration
3. Write a migration script that produces a v(N+1).0 from vN.x
4. Surface this to the user before saving — don't unilaterally change schema

Schema additions (a new optional field) can usually be done without a major bump. Renames or removals require it.

## Enhancement: Holographic Validation Protocol

**Purpose:** Verify that local subgraph patterns reflect global graph structure. Inspired by WFGY Semantic Holography — local patterns should encode global structure.

**When to run:** Before major graph updates (vN.M → vN.(M+1)) or when adding >10 nodes.

**Completeness Check Formula:**
```python
def holographic_completeness(subgraph, fullgraph):
    """
    Returns completeness_score (0.0-1.0) and anomalies list
    """
    metrics = {
        'edge_density_ratio': subgraph_edge_density / fullgraph_edge_density,
        'bridge_figure_presence': subgraph_bridges / subgraph_total_nodes,
        'confidence_distribution': compare_tier_dists(subgraph, fullgraph),
        'cross_domain_ratio': subgraph_AB_nodes / subgraph_total_nodes
    }
    
    # Weighted average of pattern matches
    completeness = weighted_average(metrics)
    anomalies = identify_deviations(metrics, threshold=0.3)
    
    return completeness, anomalies
```

**Interpretation:**
- 0.90-1.00: High completeness — local patterns match global
- 0.70-0.89: Medium — minor deviations acceptable
- 0.50-0.69: Low — review before commit
- <0.50: Reject — subgraph anomalous, investigate

**Example Application:**
Comparing two superficially similar subgraphs (e.g., two distinct routes by which a common central actor was introduced to separate institutional networks) can return a *partial* holographic match even when top-level topology looks alike — because the underlying access mechanism differs (e.g., fiduciary-bridge entry vs transactional-access entry). Record such findings as pattern variants, not errors.

**Usage:** Optional audit. Failures don't block graph updates but flag for analyst review.

**See:** `holographic_validation.py` for implementation template.
**Source:** WFGY Semantic Holography.
