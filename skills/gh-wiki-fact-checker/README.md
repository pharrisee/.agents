# GitHub Wiki Fact Checker Skill

A skill for systematically fact-checking content in GitHub wiki (gh-wiki) knowledge bases.

## Purpose

This skill provides tools and methodologies for:
- Verifying claims against original sources
- Identifying unsupported assertions
- Checking citation accuracy and completeness
- Detecting contradictions between wiki pages
- Maintaining accuracy and provenance in knowledge bases

## Installation

The skill is automatically available when loaded. To use it:

1. Ensure you have the `gh-wiki` skill loaded (this skill builds on it)
2. Load this skill: `load_skill(name: "gh-wiki-fact-checker")`
3. Follow the skill guidelines for fact-checking workflows

## Quick Start

### Basic Verification
```markdown
1. Load the skill: `load_skill(name: "gh-wiki-fact-checker")`
2. Identify a page to check: `cat concepts/transformer-scaling-laws.md`
3. Extract claims: Use the claim extraction script or manual review
4. Verify each claim against cited sources
5. Document verification results
6. Update the wiki page with verification status
```

### Using the Claim Extraction Script
```bash
# Extract claims from a wiki page
python3 scripts/extract-claims.py concepts/transformer-scaling-laws.md --output=claims.json

# View extracted claims
cat claims.json | jq '.claims[] | {text, line, types}'
```

## Key Features

### 1. Systematic Verification
- Direct verification against source material
- Confidence level assessment
- Clear documentation standards
- Audit trail maintenance

### 2. Claim Classification
- Numerical claims (statistics, measurements)
- Date/time claims
- Event claims
- Causal claims
- Definitional claims
- Comparative claims

### 3. Verification Levels
- ✅ Supported (direct evidence)
- ⚠️ Partially supported (indirect evidence)
- ❌ Unsupported (contradicted or no evidence)
- ❓ Cannot verify (insufficient information)

### 4. Comprehensive Reporting
- Detailed verification reports
- Issue prioritization
- Specific recommendations
- Wiki update instructions

## Directory Structure

```
gh-wiki-fact-checker/
├── SKILL.md                    # Main skill documentation
├── README.md                   # This file
├── references/
│   └── verification-criteria.md  # Detailed verification criteria
├── templates/
│   └── verification-report.md    # Report template
└── scripts/
    └── extract-claims.py        # Claim extraction utility
```

## Integration with gh-wiki

This skill complements the gh-wiki skill:

- **Before integration**: Fact-check new sources
- **During audits**: Include in regular health checks
- **After contradictions**: Use to resolve conflicts
- **Quality assurance**: Regular verification of important pages

## Example Workflows

### Example 1: Single Page Verification
```markdown
User: "Fact-check the claims in concepts/attention-mechanism.md"

1. Load gh-wiki-fact-checker skill
2. Read the target page
3. Extract all factual claims
4. For each claim:
   - Identify cited sources
   - Retrieve source material
   - Verify against source
   - Document result
5. Generate verification report
6. Update page with verification annotations
```

### Example 2: Cross-Page Consistency Check
```markdown
User: "Check if page1.md and page2.md have consistent claims about X"

1. Load skill
2. Extract claims about X from both pages
3. Compare claims for consistency
4. Identify contradictions
5. Trace contradictions to sources
6. Generate consistency report
7. Suggest resolutions
```

### Example 3: Source Citation Audit
```markdown
User: "Audit all citations in the wiki"

1. Load skill
2. Identify all pages with citations
3. For each citation:
   - Check if source exists
   - Verify citation accuracy
   - Assess source reliability
4. Generate citation quality report
5. Recommend fixes for broken/missing citations
```

## Best Practices

1. **Start with high-impact pages**: Focus on frequently referenced or critical content
2. **Verify against primary sources**: Prefer original research over secondary summaries
3. **Document everything**: Keep complete records of verification process
4. **Update the wiki**: Fact-checking should result in wiki improvements
5. **Be transparent**: Clearly indicate verification status and confidence
6. **Regular maintenance**: Schedule periodic verification of important content

## Limitations

- Cannot verify claims requiring original research
- Cannot replace domain expert judgment
- Cannot verify subjective claims or opinions
- Requires access to source materials
- Manual verification can be time-consuming

## Contributing

To extend this skill:

1. Add new verification methods to `references/verification-criteria.md`
2. Create new report templates in `templates/`
3. Add utility scripts to `scripts/`
4. Update `SKILL.md` with new workflows or features

## License

This skill is part of the goose agent skills collection and follows the same licensing terms.

## Support

For issues or questions:
1. Check the skill documentation in `SKILL.md`
2. Review verification criteria in `references/`
3. Use the provided templates and scripts
4. Refer to integration examples with gh-wiki skill