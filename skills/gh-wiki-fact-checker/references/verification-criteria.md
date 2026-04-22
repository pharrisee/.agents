# Verification Criteria Reference

This document outlines the criteria used for fact-checking claims in gh-wiki pages.

## Claim Classification

### Factual Claims (Verifiable)
- **Numerical claims**: Numbers, statistics, measurements
- **Date/time claims**: Specific dates, durations, timestamps
- **Event claims**: Occurrences, happenings, incidents
- **Property claims**: Attributes, characteristics, features
- **Relationship claims**: Connections, correlations, causations
- **Definitional claims**: Meanings, classifications, categorizations

### Interpretive Claims (Context-dependent)
- **Analyses**: Interpretations of data or events
- **Inferences**: Conclusions drawn from evidence
- **Predictions**: Forecasts of future events
- **Evaluations**: Assessments of quality or importance

### Non-Verifiable Claims
- **Opinions**: Personal views, preferences
- **Value judgments**: Moral, ethical, aesthetic assessments
- **Subjective experiences**: Personal feelings, perceptions

## Verification Levels

### Level 1: Direct Verification (Highest Confidence)
**Criteria**: Claim directly matches source text
**Examples**:
- Exact quote from source
- Numerical value matches source data
- Date matches source timestamp
**Status**: ✅ Supported

### Level 2: Indirect Verification (Medium Confidence)
**Criteria**: Claim logically follows from source
**Examples**:
- Inference from source data
- Summary of source content
- Implication of source statements
**Status**: ⚠️ Partially Supported (with explanation)

### Level 3: Corroboration (Variable Confidence)
**Criteria**: Multiple independent sources support claim
**Examples**:
- Same claim in 2+ reliable sources
- Consensus across multiple studies
- Independent verification
**Status**: ✅ Supported (with source count)

### Level 4: Contradiction (Requires Resolution)
**Criteria**: Sources contradict the claim
**Examples**:
- Direct contradiction in reliable source
- Evidence against claim
- Superseded information
**Status**: ❌ Unsupported

### Level 5: Cannot Verify (Insufficient Evidence)
**Criteria**: Insufficient evidence to verify
**Examples**:
- No source provided
- Source inaccessible
- Ambiguous claim
- Insufficient data in source
**Status**: ❓ Cannot Verify

## Source Reliability Assessment

### High Reliability Sources
- Peer-reviewed academic publications
- Official government documents
- Reputable news organizations with fact-checking
- Primary research data
- Technical documentation from authoritative sources

### Medium Reliability Sources
- Industry reports
- Expert blogs (domain experts)
- Conference proceedings
- Pre-prints (not yet peer-reviewed)
- Company white papers

### Low Reliability Sources
- Personal blogs without expertise
- Social media posts
- Unverified user-generated content
- Marketing materials
- Anonymous sources

### Source Recency Considerations
- **Current topics** (< 2 years): Recent sources preferred
- **Established knowledge** (2-10 years): Multiple sources across time
- **Historical topics** (> 10 years): Primary historical sources
- **Rapidly changing fields**: Very recent sources required (< 1 year)

## Claim-Specific Verification Guidelines

### Numerical Claims
1. **Check units**: Ensure consistent units
2. **Check context**: Numbers in proper context
3. **Check calculations**: Verify any derived numbers
4. **Check rounding**: Appropriate precision level
5. **Check source**: Original data source vs. interpretation

### Date/Time Claims
1. **Check format**: Consistent date formatting
2. **Check timezone**: If relevant
3. **Check sequence**: Temporal relationships
4. **Check duration**: Time spans accurate
5. **Check historical context**: Contemporary vs. modern dating

### Event Claims
1. **Check participants**: Who was involved
2. **Check location**: Where it happened
3. **Check timing**: When it happened
4. **Check sequence**: Order of events
5. **Check consequences**: Outcomes and impacts

### Causal Claims
1. **Check evidence**: Direct evidence of causation
2. **Check correlation vs causation**: Distinguish properly
3. **Check alternative explanations**: Considered and ruled out
4. **Check mechanism**: Underlying mechanism identified
5. **Check strength**: Strong vs. weak causation

### Definitional Claims
1. **Check authority**: Who defines the term
2. **Check consistency**: Consistent usage
3. **Check context**: Definition appropriate for context
4. **Check evolution**: Historical changes in meaning
5. **Check disputes**: Alternative definitions acknowledged

## Verification Documentation Standards

### Required Information for Each Verified Claim
1. **Claim text**: Exact wording from wiki
2. **Source reference**: Which source(s) were checked
3. **Verification method**: How verification was done
4. **Result**: Supported/Partially supported/Unsupported/Cannot verify
5. **Evidence excerpt**: Relevant text from source
6. **Confidence level**: High/Medium/Low
7. **Notes**: Any qualifications, limitations, or context

### Annotation Format for Wiki Pages
```markdown
<!-- Verification: [status] -->
<!-- Source: [SRC-ID] -->
<!-- Verified: [date] -->
<!-- Confidence: [level] -->
<!-- Notes: [brief note] -->
```

### Report Format
```markdown
## Verification Report

### Metadata
- **Page**: [page-name.md]
- **Date**: [verification date]
- **Verifier**: [who performed verification]
- **Scope**: [what was verified]

### Summary
- Total claims: [N]
- ✅ Supported: [X]
- ⚠️ Partially supported: [Y] 
- ❌ Unsupported: [Z]
- ❓ Cannot verify: [W]
- Overall confidence: [High/Medium/Low]

### Detailed Results
[Table or list of claims with verification details]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Notes
[Any additional context or limitations]
```

## Common Verification Patterns

### Pattern 1: Direct Quote Verification
**Claim**: "As Karpathy states, 'Transformers scale with compute according to power laws'"
**Verification**: Find quote in source, check accuracy, check context
**Result**: ✅ Supported if exact match in proper context

### Pattern 2: Numerical Claim Verification  
**Claim**: "The model has 175 billion parameters"
**Verification**: Check source for parameter count, check units
**Result**: ✅ Supported if number matches source

### Pattern 3: Date Claim Verification
**Claim**: "The paper was published in 2023"
**Verification**: Check publication date in source
**Result**: ✅ Supported if date matches

### Pattern 4: Causal Claim Verification
**Claim**: "Increasing model size improves performance"
**Verification**: Check for experimental evidence in source
**Result**: ⚠️ Partially supported if correlation shown, ❌ Unsupported if no evidence

### Pattern 5: Definition Verification
**Claim**: "Attention is a mechanism that allows models to focus on relevant parts of the input"
**Verification**: Check authoritative definitions, check consistency with field
**Result**: ✅ Supported if matches standard definition

## Quality Control Checks

### Pre-Verification Checks
1. **Claim clarity**: Is the claim clearly stated?
2. **Source availability**: Are sources accessible?
3. **Scope definition**: What exactly needs verification?
4. **Criteria alignment**: Appropriate verification criteria selected?

### During Verification Checks
1. **Method consistency**: Using same method for similar claims
2. **Bias awareness**: Checking for confirmation bias
3. **Context consideration**: Claims in proper context
4. **Evidence sufficiency**: Enough evidence for confidence level

### Post-Verification Checks
1. **Documentation completeness**: All required information recorded
2. **Result consistency**: Results make sense collectively
3. **Wiki updates**: Verification reflected in wiki
4. **Report clarity**: Report understandable to users

## Special Cases

### Claims Based on Multiple Sources
- Verify against each source
- Note if all sources agree
- Document any discrepancies
- Use lowest common confidence level

### Evolving Claims
- Check most recent sources
- Note if claim has changed over time
- Document evolution if relevant
- Mark with recency indicator

### Technical/Expert Claims
- May require domain knowledge
- Consider expert consensus
- Note technical assumptions
- Flag for expert review if uncertain

### Controversial Claims
- Document all perspectives
- Note level of consensus/disagreement
- Avoid taking sides in report
- Present evidence for all sides

## Continuous Improvement

### Learning from Verification
1. **Track accuracy**: How often are initial verifications correct?
2. **Identify patterns**: Common types of errors or misunderstandings
3. **Refine criteria**: Adjust based on experience
4. **Update guidelines**: Incorporate lessons learned

### Feedback Mechanisms
1. **User feedback**: How useful are verification reports?
2. **Expert review**: Periodic review by domain experts
3. **Peer verification**: Multiple verifiers on same claims
4. **Outcome tracking**: Follow-up on verification impact

### Tool Development
1. **Automation opportunities**: Identify repetitive tasks
2. **Template improvements**: Better report formats
3. **Integration enhancements**: Better workflow with gh-wiki
4. **Quality metrics**: Quantitative measures of verification quality