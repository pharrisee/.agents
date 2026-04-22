---
name: gh-wiki-fact-checker
description: Fact-check content in GitHub wiki (gh-wiki) against original sources, verify claims, identify unsupported assertions, and maintain accuracy in knowledge bases.
tags:
  - fact-checking
  - verification
  - gh-wiki
  - knowledge-base
  - accuracy
  - sources
  - citations
author: goose
version: 1.0.0
---

# GitHub Wiki Fact Checker Skill

Use this skill when the user wants to fact-check content in a GitHub wiki (gh-wiki) against original sources, verify claims, identify unsupported assertions, and maintain accuracy in the knowledge base.

## Core Purpose

This skill provides systematic methods to:
1. **Verify claims** against original sources
2. **Identify unsupported assertions** in wiki pages
3. **Check source citations** for accuracy and completeness
4. **Detect contradictions** between different wiki pages
5. **Maintain provenance** and traceability of information

## When to Use This Skill

- **Before integrating new sources**: Verify accuracy of claims before adding to canonical pages
- **During wiki audits**: Systematic fact-checking as part of health checks
- **When contradictions are detected**: Verify which claims are supported by evidence
- **When confidence is low**: Check questionable claims against original sources
- **Periodic maintenance**: Regular verification of key claims in important pages

## Non-Negotiable Rules

1. **Always trace to original sources** - Never accept wiki claims without verifying against source material
2. **Distinguish between facts and interpretations** - Clearly mark which claims are direct facts vs. interpretations/synthesis
3. **Preserve uncertainty** - When evidence is ambiguous or conflicting, document this clearly
4. **Update wiki pages** - Fact-checking results should be reflected in the wiki (with appropriate caveats)
5. **Maintain audit trail** - Keep records of what was checked, when, and the outcome

## Startup Protocol

When this skill activates:

1. **Identify the wiki location** - Check for gh-wiki in current directory or default location
2. **Determine scope** - What pages or claims need checking?
3. **Gather source materials** - Ensure access to original sources referenced in the wiki
4. **Establish verification criteria** - What constitutes sufficient evidence?

## Workflows

### 1. Single Claim Verification
For checking a specific claim in a wiki page:
1. Locate the claim in the wiki page
2. Identify cited sources (if any)
3. Retrieve original source material
4. Verify claim against source
5. Document verification result
6. Update wiki page with verification status

### 2. Page-Wide Fact Check
For comprehensive checking of a wiki page:
1. Extract all factual claims from the page
2. For each claim, verify against cited sources
3. Identify unsupported claims
4. Check for internal consistency within the page
5. Generate verification report
6. Update page with verification annotations

### 3. Cross-Page Consistency Check
For checking consistency across multiple wiki pages:
1. Identify related pages (by topic, entity, or concept)
2. Extract claims about the same subject from different pages
3. Compare claims for consistency
4. Identify contradictions
5. Trace contradictions to source material
6. Resolve or document contradictions

### 4. Source Citation Audit
For checking the quality of citations:
1. Extract all citations from target pages
2. Verify each citation points to valid source
3. Check citation accuracy (correct page numbers, timestamps, etc.)
4. Identify missing citations for factual claims
5. Generate citation quality report

## Verification Methods

### Direct Verification
- **Textual match**: Claim directly supported by source text
- **Numerical verification**: Numbers match source data
- **Date verification**: Dates/timestamps are accurate
- **Quote verification**: Quotations are accurate and in context

### Indirect Verification
- **Logical inference**: Claim logically follows from source
- **Expert consensus**: Claim aligns with established knowledge
- **Multiple source corroboration**: Claim supported by multiple independent sources

### Negative Verification
- **Contradiction detection**: Claim contradicts reliable sources
- **Lack of evidence**: No supporting evidence found
- **Outdated information**: Source has been superseded

## Tool Usage Patterns

### Extracting Claims from Wiki Pages
```bash
# Read wiki page
cat path=sources/SRC-2026-04-14-001.md

# Extract factual claims (manual or pattern-based)
# Look for:
# - Statements without qualifiers ("is", "are", "has")
# - Numerical claims
# - Date claims
# - Causal claims ("causes", "leads to", "results in")
```

### Retrieving Source Material
```bash
# For URL sources
curl -s [URL] | extract-text

# For file sources
cat path=raw/sources/SRC-2026-04-14-001/extracted.md

# For PDF sources
pdftotext raw/sources/SRC-2026-04-14-001/original.pdf -
```

### Comparing Claims to Sources
```bash
# Search for claim keywords in source
grep -i "keyword" path=raw/sources/SRC-2026-04-14-001/extracted.md

# Check numerical values
# Extract numbers from claim and source, compare
```

### Documenting Verification Results
```markdown
## Verification Results

### Claim: "Transformer models scale with compute according to power laws"
- **Source**: SRC-2026-04-14-001
- **Verification**: ✅ Supported
- **Evidence**: Source states "We find that model performance scales as a power law with compute"
- **Confidence**: High
- **Notes**: Direct textual match

### Claim: "Chinchilla scaling laws apply to all transformer architectures"
- **Source**: SRC-2026-04-14-001
- **Verification**: ⚠️ Partially supported
- **Evidence**: Source only tested specific architectures, generalization not proven
- **Confidence**: Medium
- **Notes**: Requires additional sources for broader claim
```

## Response Templates

### After Single Claim Verification
```
## Claim Verification

**Claim**: [exact claim text]

**Source**: [SRC-...](sources/SRC-....md)

**Verification Status**: ✅ Supported / ⚠️ Partially Supported / ❌ Unsupported / ❓ Cannot Verify

**Evidence**: [Direct quote or summary from source]

**Confidence**: High/Medium/Low

**Notes**: [Additional context, limitations, or recommendations]

**Wiki Update**: [Suggested changes to wiki page]
```

### After Page-Wide Fact Check
```
## Page Fact Check Report: [page-name.md]

### Summary
- Total claims checked: [N]
- ✅ Supported: [X]
- ⚠️ Partially supported: [Y]
- ❌ Unsupported: [Z]
- ❓ Cannot verify: [W]

### Key Findings
1. **Well-supported claims**: [list]
2. **Problematic claims**: [list with issues]
3. **Missing citations**: [claims without sources]
4. **Confidence concerns**: [claims with weak evidence]

### Recommended Actions
1. [Action 1: update specific claims]
2. [Action 2: add citations]
3. [Action 3: add caveats]
4. [Action 4: remove unsupported claims]

### Detailed Results
[Table or list of all claims with verification status]
```

### After Cross-Page Consistency Check
```
## Cross-Page Consistency Report

### Pages Compared
- [page1.md]
- [page2.md]
- [page3.md]

### Consistency Summary
- ✅ Consistent claims: [N]
- ⚠️ Minor discrepancies: [M]
- ❌ Contradictions: [K]

### Contradictions Found
1. **Subject**: [what]
   - Page1 claims: [claim]
   - Page2 claims: [contradictory claim]
   - Sources: [SRC-...] vs [SRC-...]
   - Resolution: [suggested approach]

### Recommendations
1. [Resolve contradiction by...]
2. [Update pages to reflect...]
3. [Create synthesis page documenting...]
```

### After Source Citation Audit
```
## Citation Quality Report

### Pages Audited
- [page1.md]
- [page2.md]

### Citation Summary
- Total citations: [N]
- ✅ Valid citations: [X]
- ⚠️ Problematic citations: [Y]
- ❌ Broken citations: [Z]
- Missing citations for claims: [W]

### Issues Found
1. **Broken links**: [list]
2. **Inaccurate references**: [wrong page numbers, timestamps]
3. **Missing citations**: [claims without sources]
4. **Over-citation**: [multiple citations for same claim where one suffices]

### Recommendations
1. Fix broken links: [specific fixes]
2. Add missing citations: [which claims need sources]
3. Clean up citations: [remove redundant citations]
```

## Integration with gh-wiki Skill

This skill works alongside the gh-wiki skill:

1. **Before integration**: Fact-check new sources before adding to canonical pages
2. **During audits**: Include fact-checking in regular wiki health checks
3. **After contradictions**: Use fact-checking to resolve conflicts
4. **Quality assurance**: Regular fact-checking of high-importance pages

## Quality Indicators

### Good Signs
- Claims have clear citations to original sources
- Numerical claims match source data exactly
- Dates and names are accurate
- Uncertainties and limitations are documented
- Contradictions are acknowledged and addressed

### Warning Signs
- Claims without citations
- Vague or ambiguous wording
- Overgeneralization from limited evidence
- Outdated information
- Internal contradictions
- Circular citations (wiki pages citing other wiki pages without original sources)

## Common Challenges and Solutions

### Challenge: Source Not Accessible
**Solution**: 
- Note limitation in verification report
- Mark claim as "cannot verify"
- Suggest alternative sources if available
- Add caveat to wiki page

### Challenge: Ambiguous Claim
**Solution**:
- Clarify claim with user
- Break into testable sub-claims
- Verify what can be verified
- Document ambiguity

### Challenge: Conflicting Sources
**Solution**:
- Document all sources
- Note the conflict
- Assess source reliability
- Present balanced view in wiki
- Create synthesis page if needed

### Challenge: Technical Jargon
**Solution**:
- Verify with domain experts if possible
- Check against authoritative references
- Document assumptions
- Add explanatory notes

## Best Practices

1. **Start with high-impact pages**: Focus on pages that are frequently referenced or contain critical information
2. **Check primary sources**: Whenever possible, verify against original research/primary sources
3. **Document everything**: Keep records of verification process and decisions
4. **Update the wiki**: Fact-checking without updating the wiki is incomplete
5. **Be transparent**: Clearly indicate verification status and confidence levels
6. **Regular maintenance**: Schedule periodic fact-checking of important content
7. **Collaborative verification**: When possible, have multiple people verify important claims

## Limitations

### What This Skill Cannot Do
1. **Original research**: Cannot verify claims that require new research
2. **Expert judgment**: Cannot replace domain expert evaluation
3. **Subjective claims**: Cannot verify opinions, preferences, or value judgments
4. **Future predictions**: Cannot verify claims about future events
5. **Private information**: Cannot verify claims based on non-public information

### Scope Boundaries
| In Scope | Out of Scope |
|----------|--------------|
| Verifying factual claims | Creating new knowledge |
| Checking source accuracy | Evaluating source quality |
| Identifying contradictions | Resolving philosophical disputes |
| Maintaining provenance | Managing access controls |
| Documenting verification | Enforcing verification |

## Example Workflows

### Example 1: Verifying a Technical Claim
**User**: "Verify the claim about transformer scaling laws in concepts/transformer-scaling-laws.md"

1. **Locate claim**: Find the specific claim in the concept page
2. **Trace sources**: Identify cited source (SRC-2026-04-14-001)
3. **Retrieve source**: Read raw/sources/SRC-2026-04-14-001/extracted.md
4. **Verify**: Check if source contains supporting evidence
5. **Document**: Add verification annotation to concept page
6. **Report**: Provide verification summary to user

### Example 2: Comprehensive Page Check
**User**: "Fact-check the entire concepts/attention-mechanism.md page"

1. **Extract claims**: Identify all factual claims in the page
2. **Map citations**: Link each claim to its cited sources
3. **Verify each**: Check each claim against its sources
4. **Identify gaps**: Find claims without citations
5. **Generate report**: Create detailed verification report
6. **Update page**: Add verification status markers

### Example 3: Resolving Contradiction
**User**: "Page1 says X, Page2 says not-X. Which is correct?"

1. **Identify claims**: Extract contradictory claims from both pages
2. **Trace sources**: Find sources for each claim
3. **Assess sources**: Evaluate source reliability and recency
4. **Verify claims**: Check each claim against its source
5. **Resolve**: Determine which claim is better supported
6. **Update**: Correct inaccurate page, add note to both pages
7. **Document**: Create synthesis page if contradiction represents genuine debate

## Supporting Files

This skill may include:
- `templates/verification-report.md` - Template for verification reports
- `scripts/extract-claims.py` - Script to extract claims from markdown
- `references/verification-criteria.md` - Detailed verification criteria
- `examples/` - Example verification reports

## Integration Points

- **gh-wiki skill**: For accessing wiki structure and pages
- **websearch skill**: For finding additional sources when needed
- **codesearch skill**: For verifying technical/code-related claims
- **planning skill**: For complex multi-page verification workflows

## Continuous Improvement

1. **Learn from mistakes**: When verification errors are found, update procedures
2. **Refine criteria**: Adjust verification criteria based on experience
3. **Build patterns**: Develop patterns for common claim types
4. **Automate where possible**: Create scripts for repetitive verification tasks
5. **Share knowledge**: Document verification insights in the wiki itself