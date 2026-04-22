"""
holographic_validation.py
WFGY Semantic Holography Implementation Template

Validates that local subgraph patterns reflect global graph structure.
Inspired by WFGY principle: local patterns encode global structure.
"""

import json
from typing import Dict, List, Tuple
from collections import Counter


def holographic_completeness(
    subgraph: Dict,
    fullgraph: Dict,
    threshold: float = 0.3
) -> Tuple[float, List[Dict]]:
    """
    Calculate holographic completeness score and identify anomalies.
    
    Args:
        subgraph: Dictionary with 'nodes' and 'edges' keys
        fullgraph: Dictionary with 'nodes' and 'edges' keys
        threshold: Deviation threshold for flagging anomalies (default 0.3)
    
    Returns:
        completeness_score: float (0.0-1.0)
        anomalies: List of flagged deviations
    """
    
    metrics = {}
    anomalies = []
    
    # Metric 1: Edge density ratio
    sub_density = _calculate_edge_density(subgraph)
    full_density = _calculate_edge_density(fullgraph)
    metrics['edge_density_ratio'] = sub_density / full_density if full_density > 0 else 0
    
    if abs(metrics['edge_density_ratio'] - 1.0) > threshold:
        anomalies.append({
            'metric': 'edge_density_ratio',
            'value': metrics['edge_density_ratio'],
            'expected': 1.0,
            'deviation': abs(metrics['edge_density_ratio'] - 1.0),
            'severity': 'medium' if abs(metrics['edge_density_ratio'] - 1.0) < 0.5 else 'high'
        })
    
    # Metric 2: Bridge figure presence
    sub_bridges = _count_bridge_figures(subgraph)
    sub_nodes = len(subgraph.get('nodes', []))
    full_bridges = _count_bridge_figures(fullgraph)
    full_nodes = len(fullgraph.get('nodes', []))
    
    metrics['bridge_presence_ratio'] = (sub_bridges / sub_nodes) / (full_bridges / full_nodes) if full_bridges > 0 else 0
    
    if abs(metrics['bridge_presence_ratio'] - 1.0) > threshold:
        anomalies.append({
            'metric': 'bridge_presence_ratio',
            'value': metrics['bridge_presence_ratio'],
            'expected': 1.0,
            'deviation': abs(metrics['bridge_presence_ratio'] - 1.0),
            'severity': 'low'
        })
    
    # Metric 3: Confidence distribution similarity
    sub_tiers = _extract_tiers(subgraph)
    full_tiers = _extract_tiers(fullgraph)
    metrics['tier_distribution_similarity'] = _compare_distributions(sub_tiers, full_tiers)
    
    if metrics['tier_distribution_similarity'] < (1.0 - threshold):
        anomalies.append({
            'metric': 'tier_distribution_similarity',
            'value': metrics['tier_distribution_similarity'],
            'expected': 1.0,
            'deviation': 1.0 - metrics['tier_distribution_similarity'],
            'severity': 'medium'
        })
    
    # Metric 4: Cross-domain (AB) node ratio
    sub_ab_ratio = _count_ab_nodes(subgraph) / sub_nodes if sub_nodes > 0 else 0
    full_ab_ratio = _count_ab_nodes(fullgraph) / full_nodes if full_nodes > 0 else 0
    metrics['cross_domain_ratio'] = sub_ab_ratio / full_ab_ratio if full_ab_ratio > 0 else 0
    
    if abs(metrics['cross_domain_ratio'] - 1.0) > threshold:
        anomalies.append({
            'metric': 'cross_domain_ratio',
            'value': metrics['cross_domain_ratio'],
            'expected': 1.0,
            'deviation': abs(metrics['cross_domain_ratio'] - 1.0),
            'severity': 'low'
        })
    
    # Calculate weighted completeness score
    weights = {
        'edge_density_ratio': 0.35,
        'bridge_presence_ratio': 0.25,
        'tier_distribution_similarity': 0.25,
        'cross_domain_ratio': 0.15
    }
    
    completeness = sum(
        min(metrics.get(k, 0), 2.0) * weights[k]  # cap at 2.0 to handle edge cases
        for k in weights.keys()
    )
    
    # Normalize: perfect match = 1.0, complete mismatch approaches 0.0
    completeness = min(completeness, 1.0)
    
    return completeness, anomalies


def _calculate_edge_density(graph: Dict) -> float:
    """Calculate edge density: edges / (nodes * (nodes-1) / 2)"""
    nodes = len(graph.get('nodes', []))
    edges = len(graph.get('edges', []))
    
    if nodes < 2:
        return 0.0
    
    max_edges = nodes * (nodes - 1) / 2
    return edges / max_edges if max_edges > 0 else 0.0


def _count_bridge_figures(graph: Dict) -> int:
    """Count nodes categorized as bridge_figure."""
    return sum(
        1 for n in graph.get('nodes', [])
        if n.get('category') == 'bridge_figure'
    )


def _extract_tiers(graph: Dict) -> Counter:
    """Extract confidence tier distribution from nodes."""
    return Counter(
        n.get('properties', {}).get('confidence', 'unknown')
        for n in graph.get('nodes', [])
    )


def _compare_distributions(sub: Counter, full: Counter) -> float:
    """Compare two tier distributions, return similarity 0.0-1.0."""
    all_tiers = set(sub.keys()) | set(full.keys())
    
    if not all_tiers:
        return 1.0
    
    sub_total = sum(sub.values())
    full_total = sum(full.values())
    
    if sub_total == 0 or full_total == 0:
        return 0.0
    
    # Calculate cosine similarity of distributions
    dot_product = sum(
        (sub.get(t, 0) / sub_total) * (full.get(t, 0) / full_total)
        for t in all_tiers
    )
    
    return dot_product


def _count_ab_nodes(graph: Dict) -> int:
    """Count nodes with domain 'AB' (cross-domain intersection)."""
    return sum(
        1 for n in graph.get('nodes', [])
        if n.get('domain') == 'AB'
    )


def interpret_completeness(score: float) -> str:
    """Return human-readable interpretation of completeness score."""
    if score >= 0.90:
        return "High completeness — local patterns strongly reflect global structure"
    elif score >= 0.70:
        return "Medium completeness — minor deviations acceptable"
    elif score >= 0.50:
        return "Low completeness — review before committing graph update"
    else:
        return "Critical deviation — subgraph anomalous, investigate before commit"


def audit_gate_report(
    subgraph_label: str,
    completeness: float,
    anomalies: List[Dict]
) -> str:
    """Generate audit gate report for analyst review."""
    lines = [
        f"=== Holographic Validation Audit: {subgraph_label} ===",
        f"Completeness Score: {completeness:.2f}",
        f"Interpretation: {interpret_completeness(completeness)}",
        "",
        f"Anomalies Detected: {len(anomalies)}",
    ]
    
    if anomalies:
        lines.append("")
        for a in anomalies:
            lines.append(f"  • {a['metric']}: {a['value']:.2f} (expected {a['expected']:.2f}) [{a['severity']}]")
    
    lines.append("")
    
    # Recommendation
    if completeness >= 0.70:
        lines.append("✓ APPROVED: Proceed with graph update")
    elif completeness >= 0.50:
        lines.append("⚠ WARNING: Review anomalies; consider investigation expansion")
    else:
        lines.append("✗ BLOCKED: Major structural anomaly; do not commit without analysis")
    
    return "\n".join(lines)


# Example usage (for illustration)
if __name__ == "__main__":
    # This would load actual graph JSON in practice
    example_subgraph = {
        "nodes": [
            {"id": "n1", "category": "bridge_figure", "domain": "AB", "properties": {"confidence": "confirmed"}},
            {"id": "n2", "category": "subject", "domain": "A", "properties": {"confidence": "confirmed"}},
            {"id": "n3", "category": "institution", "domain": "B", "properties": {"confidence": "confirmed"}}
        ],
        "edges": [
            {"source": "n1", "target": "n2"},
            {"source": "n1", "target": "n3"}
        ]
    }
    
    example_fullgraph = {
        "nodes": [
            {"id": "n1", "category": "bridge_figure", "domain": "AB", "properties": {"confidence": "confirmed"}},
            {"id": "n2", "category": "subject", "domain": "A", "properties": {"confidence": "confirmed"}},
            {"id": "n3", "category": "institution", "domain": "B", "properties": {"confidence": "confirmed"}},
            {"id": "n4", "category": "person", "domain": "A", "properties": {"confidence": "high"}}
        ],
        "edges": [
            {"source": "n1", "target": "n2"},
            {"source": "n1", "target": "n3"},
            {"source": "n2", "target": "n4"}
        ]
    }
    
    completeness, anomalies = holographic_completeness(example_subgraph, example_fullgraph)
    print(audit_gate_report("Example Subgraph", completeness, anomalies))
