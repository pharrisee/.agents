# Verification Report Template

## Report Metadata
- **Wiki**: [wiki name or path]
- **Page Verified**: [page-name.md]
- **Verification Date**: [YYYY-MM-DD]
- **Verifier**: [name or identifier]
- **Verification Scope**: [brief description of what was verified]
- **Report ID**: [optional unique identifier]

## Executive Summary

### Verification Overview
- **Purpose**: Why this verification was performed
- **Scope**: What claims/pages were checked
- **Method**: How verification was conducted
- **Key Findings**: Most important results

### Quick Statistics
| Metric | Count |
|--------|-------|
| Total Claims Checked | [N] |
| ✅ Supported | [X] |
| ⚠️ Partially Supported | [Y] |
| ❌ Unsupported | [Z] |
| ❓ Cannot Verify | [W] |
| Overall Confidence | [High/Medium/Low] |

### Overall Assessment
[Brief overall assessment of page accuracy and reliability]

## Detailed Results

### Claim-by-Claim Verification

#### Claim 1: [Claim text]
- **Location**: [Section/paragraph in page]
- **Claim Type**: [Factual/Interpretive/Other]
- **Cited Source(s)**: [SRC-IDs or "none"]
- **Verification Method**: [Direct/Indirect/Corroboration]
- **Result**: ✅ Supported / ⚠️ Partially Supported / ❌ Unsupported / ❓ Cannot Verify
- **Confidence**: High/Medium/Low
- **Evidence**: [Relevant excerpt from source or explanation]
- **Notes**: [Additional context, limitations, or qualifications]

#### Claim 2: [Claim text]
[Same structure as above]

[Continue for all claims...]

### Summary Tables

#### Verification Results by Claim Type
| Claim Type | Total | ✅ Supported | ⚠️ Partial | ❌ Unsupported | ❓ Cannot Verify |
|------------|-------|--------------|-------------|----------------|------------------|
| Numerical | [N1] | [X1] | [Y1] | [Z1] | [W1] |
| Date/Time | [N2] | [X2] | [Y2] | [Z2] | [W2] |
| Event | [N3] | [X3] | [Y3] | [Z3] | [W3] |
| Causal | [N4] | [X4] | [Y4] | [Z4] | [W4] |
| Definitional | [N5] | [X5] | [Y5] | [Z5] | [W5] |
| **Total** | **[N]** | **[X]** | **[Y]** | **[Z]** | **[W]** |

#### Source Quality Assessment
| Source ID | Reliability | Recency | Citation Accuracy | Notes |
|-----------|-------------|---------|-------------------|-------|
| [SRC-...] | High/Med/Low | [year] | ✅ Good / ⚠️ Issues / ❌ Poor | [notes] |
| [SRC-...] | High/Med/Low | [year] | ✅ Good / ⚠️ Issues / ❌ Poor | [notes] |

## Issues Identified

### Critical Issues (Require Immediate Attention)
1. **[Issue description]**
   - **Impact**: [Why it's critical]
   - **Location**: [Where in page]
   - **Recommended Action**: [Specific fix]
   - **Priority**: High

2. **[Issue description]**
   [Same structure]

### Moderate Issues (Should Be Addressed)
1. **[Issue description]**
   - **Impact**: [Why it matters]
   - **Location**: [Where in page]
   - **Recommended Action**: [Specific fix]
   - **Priority**: Medium

2. **[Issue description]**
   [Same structure]

### Minor Issues (Could Be Addressed)
1. **[Issue description]**
   - **Impact**: [Minor concern]
   - **Location**: [Where in page]
   - **Recommended Action**: [Optional fix]
   - **Priority**: Low

2. **[Issue description]**
   [Same structure]

## Recommendations

### Immediate Actions (High Priority)
1. **Fix unsupported claims**: [Specific claims to correct or remove]
2. **Add missing citations**: [Claims needing source citations]
3. **Correct inaccuracies**: [Specific corrections needed]
4. **Add caveats**: [Where qualifications are needed]

### Medium-Term Improvements
1. **Improve source quality**: [Suggest better sources for weak claims]
2. **Clarify ambiguous claims**: [Claims needing clearer wording]
3. **Add verification annotations**: [Where to add verification status]
4. **Cross-reference**: [Links to add to related pages]

### Long-Term Enhancements
1. **Regular verification schedule**: [Suggested frequency for this page]
2. **Source diversification**: [Types of sources to add]
3. **Expert review**: [Suggest getting domain expert review]
4. **Monitoring**: [What to watch for in future updates]

## Wiki Update Instructions

### Annotations to Add
```markdown
<!-- Verification Summary -->
<!-- Last Verified: [date] -->
<!-- Overall Confidence: [High/Medium/Low] -->
<!-- Verified Claims: [X]/[N] -->
<!-- Next Verification Due: [date] -->
```

### Specific Page Edits
1. **Line [number]**: [Current text] → [Suggested new text]
   - **Reason**: [Why change is needed]
   - **Source**: [Supporting source if applicable]

2. **Line [number]**: [Current text] → [Suggested new text]
   [Same structure]

### New Sections to Add
```markdown
## Verification Status

### Last Verified
[date] by [verifier]

### Summary
- Total claims: [N]
- Supported: [X]
- Partially supported: [Y]
- Unsupported: [Z]
- Cannot verify: [W]

### Notes
[Any important qualifications or context]

### Next Verification Due
[date]
```

## Confidence Assessment

### Factors Contributing to Confidence
1. **Source quality**: [Assessment of source reliability]
2. **Claim clarity**: [How clearly claims are stated]
3. **Evidence strength**: [Strength of supporting evidence]
4. **Corroboration**: [Multiple independent sources]
5. **Expert consensus**: [Alignment with field consensus]

### Confidence Limitations
1. **Access limitations**: [Sources not fully accessible]
2. **Technical complexity**: [Claims requiring expert knowledge]
3. **Ambiguity**: [Unclear or ambiguous claims]
4. **Evolving field**: [Rapidly changing information]

### Overall Confidence Justification
[Explanation of why overall confidence is High/Medium/Low]

## Appendices

### Appendix A: Source Details
#### Source: [SRC-ID]
- **Title**: [Source title]
- **Type**: [Article/Paper/Book/Website/etc.]
- **Author**: [Author(s)]
- **Date**: [Publication date]
- **Reliability**: High/Medium/Low
- **Access**: [How accessed/limitations]
- **Relevance**: [How relevant to claims]
- **Notes**: [Additional information]

[Repeat for each source...]

### Appendix B: Verification Methodology
#### Methods Used
1. **Direct text comparison**: [Description]
2. **Numerical verification**: [Description]
3. **Context analysis**: [Description]
4. **Corroboration checking**: [Description]
5. **Expert consultation**: [If applicable]

#### Tools Used
- [Tool 1]: [Purpose]
- [Tool 2]: [Purpose]
- [Tool 3]: [Purpose]

#### Time Spent
- **Total time**: [hours]
- **Breakdown**: [Time per activity]

### Appendix C: Raw Data
#### Claim Extraction
```json
[
  {
    "claim_id": "1",
    "text": "[exact claim text]",
    "location": "[page section]",
    "type": "[claim type]",
    "sources": ["SRC-ID1", "SRC-ID2"],
    "verification_result": "supported",
    "confidence": "high",
    "evidence": "[evidence text]",
    "notes": "[any notes]"
  },
  // ... more claims
]
```

#### Source Analysis
```json
[
  {
    "source_id": "SRC-2026-04-14-001",
    "reliability": "high",
    "recency": "2026",
    "accessibility": "full",
    "relevance_score": 0.9,
    "notes": "[source notes]"
  },
  // ... more sources
]
```

## Next Steps

### Immediate (Within 1 Week)
1. [ ] Review this report with page owner
2. [ ] Implement critical fixes
3. [ ] Add verification annotations to page
4. [ ] Update wiki metadata

### Short-Term (Within 1 Month)
1. [ ] Implement moderate priority fixes
2. [ ] Schedule next verification
3. [ ] Share findings with relevant wiki contributors
4. [ ] Update verification procedures if needed

### Ongoing
1. [ ] Monitor page for new claims
2. [ ] Track implementation of recommendations
3. [ ] Update verification schedule based on page importance
4. [ ] Incorporate lessons into future verifications

## Contact Information

- **Verifier**: [name/contact]
- **Report Generated**: [date]
- **Report Version**: [version number]
- **Questions/Feedback**: [how to contact]

---

*This verification report follows the gh-wiki-fact-checker skill guidelines. For questions about the verification process or to request verification of other pages, refer to the skill documentation.*