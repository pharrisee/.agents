#!/usr/bin/env python3
"""
Extract claims from gh-wiki markdown files for fact-checking.

This script helps identify factual claims in wiki pages that may need verification.
It uses simple pattern matching to find potential claims, which should then
be reviewed and verified manually.

Usage:
    python3 extract-claims.py [markdown-file] [--output=output.json]
"""

import re
import json
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any

def extract_claims_from_markdown(content: str) -> List[Dict[str, Any]]:
    """
    Extract potential factual claims from markdown content.
    
    Args:
        content: Markdown text
        
    Returns:
        List of claim dictionaries with text, location, and metadata
    """
    claims = []
    
    # Split content into lines for location tracking
    lines = content.split('\n')
    
    # Patterns for different types of claims
    patterns = {
        'numerical': [
            r'\b\d+[\d,\.]*\s*(?:percent|%|dollars|\$|years|months|days|hours|minutes|seconds)\b',
            r'\b(?:over|more than|less than|approximately|about|around)\s+\d+[\d,\.]*\b',
            r'\b\d+[\d,\.]*\s*(?:times|×|x)\b',
        ],
        'date_time': [
            r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s*\d{4}\b',
            r'\b\d{4}(?:-\d{2}){0,2}\b',  # YYYY, YYYY-MM, YYYY-MM-DD
            r'\b(?:in|on|during|by)\s+\d{4}\b',
        ],
        'definitive': [
            r'\b(?:is|are|was|were)\s+(?:not\s+)?(?:the|a|an)\s+[A-Za-z]+\b',
            r'\b(?:has|have|had)\s+(?:not\s+)?(?:been|always)\s+[A-Za-z]+\b',
            r'\b(?:means|refers to|defines|is defined as)\s+',
        ],
        'causal': [
            r'\b(?:causes|caused|leads to|results in|produces|creates)\s+',
            r'\b(?:because|due to|as a result of|owing to)\s+',
            r'\b(?:if|when)\s+[A-Za-z]+\s+then\s+',
        ],
        'comparative': [
            r'\b(?:better|worse|faster|slower|larger|smaller|more|less)\s+than\b',
            r'\b(?:the same as|similar to|different from|unlike)\s+',
            r'\b(?:compared to|in comparison with|relative to)\s+',
        ]
    }
    
    # Also look for sentences that might contain claims
    # Simple sentence splitting (not perfect but helpful)
    sentences = re.split(r'[.!?]+', content)
    sentence_start_positions = []
    pos = 0
    for sentence in sentences:
        if sentence.strip():
            sentence_start_positions.append((pos, sentence.strip()))
            pos += len(sentence) + 1  # +1 for the punctuation
    
    # Process each sentence for potential claims
    for pos, sentence in sentence_start_positions:
        if len(sentence.split()) < 3:  # Skip very short sentences
            continue
            
        claim_types = []
        
        # Check for claim indicators
        if any(word in sentence.lower() for word in ['according to', 'studies show', 'research indicates', 'evidence suggests']):
            claim_types.append('research_based')
        
        # Check for citation patterns
        if re.search(r'\[[^\]]+\]\([^)]+\)', sentence) or re.search(r'\[SRC-[^\]]+\]', sentence):
            claim_types.append('cited')
        
        # Check for numerical patterns
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in patterns['numerical']):
            claim_types.append('numerical')
        
        # Check for date patterns
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in patterns['date_time']):
            claim_types.append('date_time')
        
        # Check for definitive statements
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in patterns['definitive']):
            claim_types.append('definitive')
        
        # Check for causal statements
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in patterns['causal']):
            claim_types.append('causal')
        
        # Check for comparative statements
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in patterns['comparative']):
            claim_types.append('comparative')
        
        # If we found any claim indicators, add it
        if claim_types:
            # Find line number (approximate)
            line_num = content[:pos].count('\n') + 1
            
            claims.append({
                'text': sentence,
                'position': pos,
                'line': line_num,
                'types': claim_types,
                'has_citation': 'cited' in claim_types,
                'confidence': 'medium' if claim_types else 'low'
            })
    
    return claims

def find_citations_in_text(text: str) -> List[Dict[str, str]]:
    """Extract citations from markdown text."""
    citations = []
    
    # Find markdown links
    md_links = re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text)
    for match in md_links:
        citations.append({
            'text': match.group(1),
            'link': match.group(2),
            'type': 'markdown_link'
        })
    
    # Find SRC references
    src_refs = re.finditer(r'\[(SRC-[^\]]+)\]', text)
    for match in src_refs:
        citations.append({
            'text': match.group(1),
            'link': f'sources/{match.group(1)}.md',
            'type': 'src_reference'
        })
    
    return citations

def main():
    parser = argparse.ArgumentParser(description='Extract claims from gh-wiki markdown files')
    parser.add_argument('input_file', help='Markdown file to analyze')
    parser.add_argument('--output', '-o', help='Output JSON file (default: stdout)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Read input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract claims
    claims = extract_claims_from_markdown(content)
    
    # Extract citations
    citations = find_citations_in_text(content)
    
    # Prepare result
    result = {
        'file': str(input_path),
        'total_claims': len(claims),
        'total_citations': len(citations),
        'claims': claims,
        'citations': citations,
        'analysis': {
            'claim_types': {
                'numerical': sum(1 for c in claims if 'numerical' in c['types']),
                'date_time': sum(1 for c in claims if 'date_time' in c['types']),
                'definitive': sum(1 for c in claims if 'definitive' in c['types']),
                'causal': sum(1 for c in claims if 'causal' in c['types']),
                'comparative': sum(1 for c in claims if 'comparative' in c['types']),
                'research_based': sum(1 for c in claims if 'research_based' in c['types']),
                'cited': sum(1 for c in claims if c['has_citation']),
            }
        }
    }
    
    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Results written to {args.output}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Verbose output
    if args.verbose:
        print("\n=== CLAIM SUMMARY ===", file=sys.stderr)
        print(f"Total claims found: {len(claims)}", file=sys.stderr)
        print(f"Total citations: {len(citations)}", file=sys.stderr)
        print("\nClaim types:", file=sys.stderr)
        for claim_type, count in result['analysis']['claim_types'].items():
            print(f"  {claim_type}: {count}", file=sys.stderr)
        
        print("\n=== SAMPLE CLAIMS ===", file=sys.stderr)
        for i, claim in enumerate(claims[:5]):  # Show first 5
            print(f"\nClaim {i+1} (line {claim['line']}):", file=sys.stderr)
            print(f"  Text: {claim['text'][:100]}...", file=sys.stderr)
            print(f"  Types: {', '.join(claim['types'])}", file=sys.stderr)
            print(f"  Has citation: {claim['has_citation']}", file=sys.stderr)

if __name__ == '__main__':
    main()