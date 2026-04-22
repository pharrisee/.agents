# Visualization Artifact Generation

Findings that live only in JSON graphs and Markdown reports are hard to navigate. The methodology has consistently produced one or more visual artifacts per investigation — interactive knowledge graphs, entity-network pinboards, reference cards, dashboards, atlases — that turn the research into something the user can actually explore.

This module specifies the standard visualization patterns, when to use each, and the technical conventions that make them consistent across investigations.

## When this method applies

Always run if the investigation produced any of:
- A graph update (visualize the new state, even if just the diff)
- A multi-entity network finding (anything with 5+ named entities and connections between them)
- A dataset that has structure worth seeing (timelines, hierarchies, geographic distributions)
- A reference set the user will return to (glossaries, protocol cards, lookup tables)

Skip if the investigation produced only prose findings with no entity graph or structured data — a Markdown report serves better in that case.

## The standard artifact catalogue

The methodology has converged on five recurring visualization patterns. Pick whichever fits the data; combine if more than one applies.

### 1. Interactive knowledge graph (D3.js force-directed)

**When to use:** the investigation updated the project graph, or the new findings form a network of 10+ nodes with explicit relationships.

**Standard form:** a single self-contained HTML file with embedded D3.js (CDN-linked), force-directed layout, domain-based color coding, hover tooltips, click-for-detail panels, and filter controls (by domain, confidence tier, node category).

**Color discipline (carry across investigations for visual continuity):**
- Domain A nodes: cyan family (`#53d8fb`, `#7fdbca`)
- Domain B nodes: gold/amber family (`#e9b44c`, `#f0d060`)
- Intersection / cross-domain nodes: warm rose / coral (`#e94560`, `#ff6b6b`)
- Person nodes: muted purple (`#9b72cf`)
- Institution nodes: green (`#5fa55a`)
- Background: near-black (`#0a0a12`)
- Grid lines: very dark grey (`#111118`)

**Confidence visualization:** node opacity scales with tier — `confirmed` 1.0, `high` 0.7, `medium` 0.4 (only if surfacing candidates explicitly). Edge thickness scales with weight.

### WFGY-Enhanced Tier Visualization

**Integration:** Following case-study validation, tier opacity is formally specified:

- **Confirmed (100%):** Full opacity, solid stroke — established fact
- **High (70%):** Semi-transparent, solid stroke — "awaiting promotion" visual cue  
- **Medium (40%):** Heavily transparent, dashed stroke — report-only, never in graph

**Rationale:** High-tier nodes at 70% opacity visually communicate uncertainty without requiring text labels. This is especially valuable for:
- Prioritizing investigation (high-opacity nodes become priority targets)
- Communicating epistemic status in stakeholder presentations
- Preventing false confidence in graph navigation

**Implementation (D3.js):**
```javascript
const opacityScale = {
  "confirmed": 1.0,
  "high": 0.7, 
  "medium": 0.4
};

node.style("opacity", d => opacityScale[d.properties.confidence] || 0.5);
```

See also: `bridge-figures.md` for role-context tension scoring.

**Standard interactions:**
- Drag nodes to reposition
- Scroll to zoom; click-drag background to pan
- Click node → detail panel with full properties + connected-edge buttons
- Hover node → highlight node + connected edges + connected nodes; dim everything else
- Filter buttons in header → toggle visibility by category

**Save as:** `/mnt/user-data/outputs/<thread-name>-knowledge-graph.html`

### 2. Entity-network pinboard (React)

**When to use:** the investigation surfaced an organizational network — companies, institutions, people, agencies and their funding/collaboration/ownership ties — that benefits from manual layout rather than algorithmic force-direction.

The pinboard differs from the D3 graph: nodes are pre-positioned by type into spatial regions (military top, companies middle, persons left, intelligence right, etc.), making the typology legible at a glance. Use when categorical clustering matters more than network topology.

**Standard form:** React component (`.jsx` artifact), single file, manual node positioning with drag-to-reposition, type-based color coding matching the D3 palette, edge labels visible on hover, filter buttons by node type, detail panel pinned to bottom on selection.

**Save as:** an artifact via the React artifact channel, AND a backup `.jsx` file at `/mnt/user-data/outputs/<thread-name>-pinboard.jsx`.

### 3. Dark-aesthetic reference card (HTML)

**When to use:** the investigation produced a protocol, checklist, glossary, or quick-lookup table the user will return to repeatedly.

**Standard form:** single self-contained HTML file, dark background, monospace font (`'JetBrains Mono', 'Fira Code', monospace`), section headers with accent color, dense tabular data, no external dependencies.

**Structural conventions:**
- Header bar with title + subtitle + accent dot
- 3–6 sections separated by horizontal rules
- Each section has a small all-caps label
- Dense information; avoid white space inflation
- Print-friendly (works at A4/Letter when printed)

**Save as:** `/mnt/user-data/outputs/<thread-name>-reference.html`

### 4. Comprehensive research atlas (HTML)

**When to use:** at major project milestones — when multiple threads converge into a unified picture, or when the user explicitly asks for "a complete artifact" or "everything in one place."

**Standard form:** single large self-contained HTML file (typically 50–100 KB) combining:
- Header with project metric cards (node count, edge count, sub-investigations performed, confidence distribution)
- Embedded D3.js force-directed graph (as in pattern 1)
- Section-by-section findings prose
- Expandable glossary cards
- Methodology documentation
- Curated source list with confidence tiers

The atlas is the "everything you need to understand the current state" artifact. Build it from the existing graph, report, and handoff rather than from scratch.

**Save as:** `/mnt/user-data/outputs/<project-name>-atlas-<date>.html`

### 5. Specific-purpose visualization (timeline, map, comparison chart)

**When to use:** when the data has a strongly time-based, geographic, or comparative structure that the general patterns don't serve.

**Common variants:**
- Vertical or horizontal timeline (events with dates → use HTML/CSS or a small D3 script)
- Geographic map with markers (events with coordinates → use the `places_map_display_v0` tool)
- Side-by-side comparison chart (use the `chart_display_v0` tool for quick statistical comparisons; build a custom HTML/SVG for richer comparisons)

Pick the simplest tool that serves the data. The methodology favours self-contained HTML over complex interactive frameworks unless interactivity adds genuine analytical value.

## Procedure

### Step 1: Decide which artifacts apply

Look at the synthesis output (graph diff, report findings, candidate list) and ask:
- Did the graph change? → pattern 1 (D3 graph) at minimum
- Are the new findings an organizational network with clear typology? → pattern 2 (pinboard) in addition
- Did the investigation produce a reusable lookup? → pattern 3 (reference card)
- Is this a project milestone or "give me everything" request? → pattern 4 (atlas)
- Is there time-series, geographic, or comparative structure? → pattern 5 (specific-purpose)

Multiple patterns can apply. Don't force a single artifact when two complement each other.

### Step 2: Check for the frontend-design skill

Before building any visualization, check whether `/mnt/skills/user/frontend-design/SKILL.md` (or `/mnt/skills/public/frontend-design/SKILL.md`) is present. If so, read it first — it contains the design tokens, component patterns, and styling constraints calibrated for this environment.

If frontend-design is not present, fall back to the conventions in this module.

### Step 3: Build the artifact(s)

Use the `create_file` tool to build the HTML/JSX/SVG file directly. For HTML artifacts, prefer:
- Single file with everything inlined or CDN-loaded
- D3.js v7 from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`
- No build step, no bundler, no npm dependencies
- Works offline once loaded (except CDN-loaded libs)

For React artifacts (pinboards), use the artifact channel (`.jsx` files in outputs render in the artifact viewer).

### Step 4: Pull data from the existing graph

The visualization should read the graph JSON the investigation just produced, not a hand-rewritten copy. Embed the JSON directly into the HTML as a `<script>` block:

```html
<script>
const GRAPH_DATA = { /* ...inlined JSON from /home/claude/<thread>/graph-vN.M.json... */ };
</script>
```

This guarantees the visualization stays in sync with the graph and survives offline distribution.

### Step 5: Add the visualization to the delivery bundle

In Phase 4 (Delivery), the visualization artifacts ship alongside the report, graph, and handoff. Order in `present_files`:

1. Handoff (high-level summary)
2. Report (full findings)
3. Atlas (if produced — most navigable single artifact)
4. Knowledge graph HTML (if produced separately from atlas)
5. Pinboard (if produced)
6. Reference card (if produced)
7. Comparison docx (if structural parallels were found)
8. Graph JSON (machine-readable)

In the chat response after `present_files`, briefly note which visualization to open first based on what the user is most likely to want to explore.

## Standard interaction patterns

For interactive HTML artifacts, the methodology has settled on these conventions to keep the user's mental model consistent across sessions:

- **Click** = select / show detail panel
- **Hover** = highlight + show contextual info; non-destructive
- **Drag** = reposition (nodes) or pan (background)
- **Scroll wheel** = zoom
- **ESC key** = clear selection
- **Filter buttons** in a header bar; clicking a filter that's already active deactivates it

Document interaction patterns in a small legend (corner of the visualization) so first-time users don't have to discover them.

## What disqualifies an artifact

- Visualizations that exceed 5 MB (consider splitting; the user can't easily share a giant single file)
- React artifacts that require build steps (use only what runs as a standalone JSX in the artifact channel)
- Anything requiring user authentication to render (a federated chart pulling from a private API will break for the next session)
- Visualizations of untiered or speculative data without explicit tier labels (violates the discipline; if it's in the visualization, it has to be tiered)

## The null-visualization pathway

If the investigation produced only narrative findings — no graph update, no entity network, no protocol — skip the visualization step entirely and document in the report's "Artifacts produced" section: "No visualization generated — findings are narrative-only and best served by the report itself." This matches the discipline of the null-update pathway in graph-integration: not every investigation needs every output.
