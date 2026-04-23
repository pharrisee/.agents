---
name: guardrails-evaluation
description: Evaluates when and how to apply guardrails ("When NOT to Use" sections) across agent skills to prevent misuse. Includes decision matrices and evaluation rubrics.
---

# Guardrails Evaluation Skill

This skill captures the evaluation of when and how to apply guardrails ("When NOT to Use" sections) across agent skills to prevent misuse. Documents criteria for appropriate tool selection and prevents resource waste or privacy violations.

## Purpose

Document and evaluate the criteria for when each agent skill should and should not be activated. This prevents misuse and ensures appropriate tool selection while preserving powerful capabilities.

## When to Evaluate

Apply guardrails analysis **before**:
- Activating resource-intensive skills (convergence, autonomous agents)
- Processing sensitive/personal information
- Invoking tools with external API calls
- Chain-calling multiple skills
- Running long-duration tasks
- Accessing files outside working directory

## Evaluation Framework

### 1. Simplicity vs. Complexity Matrix

| Task Complexity | Simple Tools Available | Use Full Skill? |
|----------------|----------------------|----------------|
| **Low** (single fact, direct answer) | Yes (knowledge, basic search) | ❌ No — answer directly |
| **Low** (single fact, no tools) | No but trivial research | ❌ No — web search only |
| **Medium** (multi-step, clear scope) | Partial (need coordination) | ✅ Yes — with scope limits |
| **Medium** (multi-tool, 3-5 calls) | No integrated tool | ✅ Yes — standard use |
| **High** (complex coordination, >5 steps) | No automated solution | ✅ Yes — with checkpoints |
| **High** (expert judgment needed) | No, requires expertise | ⚠️ Yes — but flag limitations |

### 2. Resource Intensity Calculator

**Before invoking, estimate:**

| Resource | Low (<$0.01 / <1s) | Medium ($0.01-$0.50 / 1-30s) | High (>$0.50 / >30s) | Action |
|----------|-------------------|------------------------------|----------------------|--------|
| **API Cost** | ✅ Proceed | ⚠️ Get user confirmation | ❌ Require explicit approval |
| **Time** | ✅ Proceed | ⚠️ Warn user of delay | ❌ Background task only |
| **Tokens** (<1K) | ✅ Proceed | ⚠️ Summarize intermediate | ❌ Paginate/stream output |
| **Tokens** (1K-10K) | ⚠️ Confirm value | ⚠️ Check necessity | ❌ Chunk processing |
| **Tokens** (>10K) | ⚠️ Alternative approach | ❌ Batch with approval | ❌ Avoid unless critical |

### 3. Privacy & Safety Matrix

**Evaluate on two axes:**

#### A. Data Sensitivity

| Level | Description | Examples | Allowed? |
|-------|-------------|----------|----------|
| **Public** | Intended for public sharing | Blog posts, marketing | ✅ Full processing |
| **Internal** | Within organization | Work docs, policies | ⚠️ Process, don't store |
| **Confidential** | Restricted access | PII, financials, health | ❌ Redact first, get consent |
| **Restricted** | Legal/regulatory protection | SSN, passwords, trade secrets | ❌ Do not process |

#### B. User Consent

| Scenario | Status | Required Action |
|----------|--------|-----------------|
| Explicit permission given | ✅ | Proceed per scope |
| Implied by task context | ⚠️ | Confirm boundaries |
| No consent, unclear scope | ❌ | Ask before proceeding |
| Third-party data involved | ❌ | Must have explicit permission |

### 4. Scope Creep Risk Assessment

**Red Flags (any = stop and clarify):**

- [ ] Vague initial request that could expand indefinitely
- [ ] Multiple "related" tasks mentioned but not scoped
- [ ] No clear completion criteria defined
- [ ] User says "and while you're at it..." mid-task
- [ ] Open-ended exploration without focus
- [ ] Historical pattern: User tends to expand scope

**Mitigation Strategies:**

1. **Time-boxing**: "I'll work on this for [X time/iterations], then check in"
2. **Phase gates**: "Let's complete step 1 before discussing step 2"
3. **Explicit scope document**: Write down what's IN and OUT of scope
4. **Two-pizza rule**: If it can't be explained while eating pizza, it's too big

### 5. Appropriateness Checklist

For each skill activation, verify:

#### Task Appropriateness
- [ ] Matches skill's primary purpose
- [ ] Not trivially solvable without the skill
- [ ] Complexity justifies overhead
- [ ] Clear success criteria defined

#### Ethical Appropriateness  
- [ ] No privacy violations
- [ ] No potential for harm/misuse
- [ ] No terms of service violations
- [ ] Respects user intent, not just literal request

#### Resource Appropriateness
- [ ] Cost proportional to value
- [ ] Time investment reasonable
- [ ] Simpler alternatives considered
- [ ] User aware of resource usage

## "When NOT to Use" Pattern Templates

### Template for All Skills

Every skill should include these sections:

```markdown
## When NOT to Use This Skill

### Simple Queries
- [Example 1]: Direct answers available
- [Example 2]: Trivial lookups

### Resource-Wasting Triggers  
- [Scenario] that consumes significant resources
- [Alternative] lighter approach

### Privacy-Sensitive Scenarios
- [Data type]: Requires explicit consent
- [Data type]: Do not process without approval

### Inappropriate Contexts
- [Context] where skill is misapplied
- [Alternative]: Better tool or approach
```

### Specific Skill Templates

#### Research Skills (convergence, llm-wiki)
**Do NOT use for:**
- Single quick lookups (use browser search)
- Personal research on non-consenting individuals
- Real-time breaking news (incomplete/incorrect)
- Highly specialized academic topics (use specialized tools)

#### Autonomous Agents (claude-code, opencode, codex)
**Do NOT use for:**
- Simple one-line fixes
- Tasks requiring human judgment/nuance
- Code review of sensitive security code
- Quick edits in production systems

#### Wiki/Knowledge Skills
**Do NOT use for:**
- Personal scratch notes
- Already-indexed content
- Format conversion only (use dedicated tools)
- Bulk automated capture without curation

## Decision Tree

```
Start: User requests tool use
  |
  v
Is task trivial? --Yes--> Answer directly (no tool)
  |
  No
  |
  v
Check privacy level
  |
  +-- Restricted? --Yes--> Stop, request consent
  |
  +-- Confidential? --Yes--> Redact, limit scope
  |
  +-- Public/Internal? --Yes--> Proceed (with care)
  |
  v
Estimate resource cost
  |
  +-- High? --Yes--> User approval required
  |
  +-- Medium? --Yes--> Warn user
  |
  +-- Low? --Yes--> Proceed
  |
  v
Scope clear & bounded?
  |
  +-- No? --Yes--> Clarify before proceeding
  |
  +-- Yes? --Yes--> Activate tool
  |
  v
Monitor during execution
  |
  +-- Scope creep? --Yes--> Pause, re-confirm
  |
  +-- Unexpected cost? --Yes--> Stop, inform user
  |
  v
Complete & document
```

## Usage Guidelines

### Be Specific, Not General

❌ **Bad:** "Don't use for complex tasks"  
✅ **Good:** "Don't use for tasks requiring >3 API calls or >500 tokens"

❌ **Bad:** "Don't violate privacy"  
✅ **Good:** "Don't process any PII without explicit written consent"

### Prioritize User Safety Over Feature Usage

- When in doubt, ask
- When uncertain, choose the safer option
- Explain WHY a tool shouldn't be used, not just that it shouldn't

### Consider Edge Cases

Think through:
1. What if the user is asking about a third party?
2. What if the task expands unexpectedly?
3. What if the tool produces incorrect results?
4. What if resources/time exceed estimates?

### Reference Policies

When applicable, cite:
- Platform terms of service
- Data protection regulations (GDPR, CCPA)
- Ethical AI principles
- Organizational policies

## Examples

### Simple Query (Don't Use Full Pipeline)

❌ **Don't:** Invoke `convergence-investigation` for "What's the capital of France?"

✅ **Do:** Answer directly: "Paris"

**Rationale:** Single fact, no research coordination needed, trivial knowledge.

---

### Privacy-Sensitive (Need Consent)

❌ **Don't:** Research personal background of someone mentioned without permission

✅ **Do:** Ask: "I can research public information about this person. Is that okay? Note that I can only access public sources."

**Rationale:** Potential PII, third-party individual, requires consent.

---

### Resource-Wasting (Overkill)

❌ **Don't:** Use autonomous code agent to change a variable name

✅ **Do:** Make the edit directly or use simple search/replace

**Rationale:** Simple edit (<10 seconds) doesn't justify agent overhead (setup + minutes).

---

### Scope Creep Risk

❌ **Don't:** Start multi-hour research without defined boundaries

✅ **Do:** "I can research this topic for 30 minutes focusing on [specific aspect]. Should I proceed, or would you like to narrow the scope first?"

**Rationale:** Prevents unbounded time investment on vaguely defined work.

---

## Review Process

### Before Adding/Modifying Guardrails

1. **Check existing patterns**: Is this covered by another skill's guardrails?
2. **Assess risk level**: What's the worst case if misused?
3. **Estimate frequency**: How often will this skill be called?
4. **Test the guardrail**: Try to create scenarios that would bypass it

### Audit Checklist (Quarterly)

- [ ] All skills have "When NOT to Use" sections
- [ ] No skills missing privacy considerations
- [ ] Resource estimates still accurate (prices may change)
- [ ] New capabilities haven't created new risks
- [ ] Real usage patterns match guardrail assumptions
- [ ] User feedback on guardrails reviewed

### When Guardrails Fail

If a skill is misused despite guardrails:

1. **Document**: What happened, how it bypassed guardrails
2. **Analyze**: Why guardrail didn't catch it
3. **Fix**: Update guardrail language or add new criteria
4. **Test**: Try similar misuse attempts against updated guardrail
5. **Notify**: Inform users of guardrail change if significant

---

## Quick Reference Cards

### Red Light Cards (STOP)

| Card | Trigger | Action |
|------|---------|--------|
| 🔴 **Privacy** | PII, confidential data | Get explicit consent or stop |
| 🔴 **Legal** | Terms of service violation | Stop, suggest alternative |
| 🔴 **Safety** | Potential for harm | Stop, escalate if needed |
| 🔴 **Scope** | Open-ended, undefined | Clarify before proceeding |

### Yellow Light Cards (CAUTION)

| Card | Trigger | Action |
|------|---------|--------|
| 🟡 **Cost** | >$0.50 estimated | Warn user, get approval |
| 🟡 **Time** | >30s estimated | Warn of delay, offer async |
| 🟡 **Complexity** | Multiple systems | Confirm understanding |
| 🟡 **Novelty** | First-time use | Extra monitoring, checkpoints |

### Green Light Cards (PROCEED)

| Card | Trigger | Action |
|------|---------|--------|
| 🟢 **Clear** | Well-scoped task | Proceed as planned |
| 🟢 **Simple** | Low-resource, accurate | Execute confidently |
| 🟢 **Appropriate** | Perfect skill match | Full capability use |
| 🟢 **Routine** | Standard pattern | Efficient execution |

---

## Integration with Other Skills

### How Guardrails Apply to Common Skills

| Skill | Key Guardrail | Common Misuse |
|-------|--------------|---------------|
| `convergence` | Don't research individuals without consent | Digging into personal connections |
| `claude-code`/`opencode` | Don't for trivial edits | Changing single characters |
| `llm-wiki` | Don't use as scratchpad | Temporary notes, drafts |
| `context7-mcp` | Don't for simple syntax | Basic language features |
| `autonomous-agents` | Don't cascade agents unnecessarily | Agent calling agent loops |
| `systematic-debugging` | Don't for obvious fixes | Typos, simple syntax errors |

### Skill Interaction Matrix

| Primary Skill | Safe to Chain With | Requires Caution With | Avoid Combining With |
|--------------|-------------------|----------------------|---------------------|
| `convergence` | `llm-wiki` (write up) | `autonomous-agents` (scope creep) | Multiple research agents |
| `claude-code` | `systematic-debugging` | `convergence` (distraction) | Other code agents simultaneously |
| `llm-wiki` | `guardrails-evaluation` (check) | `autonomous-agents` (auto-writing) | Scraping/crawling tools |
| `context7-mcp` | Any (read-only) | N/A | None |

---

## Templates for Guardrail Messages

### When Stopping

> "I need to stop here because [reason]. This appears to fall under [guardrail category]. 
> 
> Options:
> 1. Provide [specific approval/consent] to proceed
> 2. Narrow the scope to [specific alternative]
> 3. Use a different approach that doesn't require this capability"

### When Warning

> "I can proceed, but note that [concern]. This involves [resource/risk].
> 
> Alternatives to consider:
> - [Simpler option]
> - [Manual approach]
> - [Partial execution]
> 
> Shall I continue or would you prefer an alternative?"

### When Clarifying Scope

> "To make sure I use the right tool and don't over-invest, can you clarify:
> 1. What's the specific goal you want to achieve?
> 2. How will you know when it's done?
> 3. What's NOT part of this request?
> 4. Any constraints on time/cost/privacy?"

---

## Metrics & Improvement

### Track These Metrics

- **Guardrail triggers**: How often each guardrail catches issues
- **User overrides**: How often users explicitly approve flagged actions
- **False positives**: Cases where guardrails were too restrictive
- **Time saved**: Avoided wasted effort on inappropriate tool use
- **Privacy incidents**: Near-misses caught by guardrails

### Continuous Improvement

- Monthly review of guardrail effectiveness
- User feedback on guardrail helpfulness vs. friction
- Update based on new capabilities and risks
- Share learnings across skill developers

---

## Summary Checklist

Before activating ANY skill, verify:

- [ ] **Necessity**: Is this tool actually needed?
- [ ] **Appropriateness**: Is this the right tool for this task?
- [ ] **Privacy**: No sensitive data without consent?
- [ ] **Resources**: Costs/time understood and acceptable?
- [ ] **Scope**: Clear boundaries and completion criteria?
- [ ] **Alternatives**: Simpler options considered?
- [ ] **Safety**: No potential for misuse or harm?
- [ ] **Policies**: Complies with all relevant guidelines?

**If any check fails → STOP and address before proceeding**