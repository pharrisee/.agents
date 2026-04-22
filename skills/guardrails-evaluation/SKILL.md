---
name: guardrails-evaluation
description: Evaluates when and how to apply guardrails ("When NOT to Use" sections) across agent skills to prevent misuse.
---

# Guardrails Evaluation Skill

This skill captures the evaluation of when and how to apply guardrails ("When NOT to Use" sections) across agent skills.

## Purpose

Document and evaluate the criteria for when each agent skill should and should not be activated. This prevents misuse and ensures appropriate tool selection.

## Evaluation Criteria

For each skill, evaluate:

1. **Simplicity vs. Complexity**: Does the task genuinely need this skill's full machinery, or would a simpler approach suffice?
2. **Resource Intensity**: Does invoking this skill consume significant time/compute vs. a direct answer?
3. **Privacy/Safety**: Does the task involve sensitive information where the full pipeline might over-collect data?
4. **Scope Creep Risk**: Could a vague query trigger unnecessary sub-methods or investigations?
5. **Consent Requirements**: Does the methodology require explicit user consent (e.g., researching individuals)?

## "When NOT to Use" Pattern

Each skill should include a "When NOT to Use This Skill" section documenting:

- **Simple queries** that can be answered directly
- **Single-method needs** where a sub-skill would suffice  
- **Non-appropriate contexts** (creative tasks, legal matters, etc.)
- **Privacy-sensitive scenarios** requiring explicit consent
- **Resource-wasting triggers** (bulk operations, unnecessary iterations)

## Usage Guidelines

- Be specific about conditions, not just general statements
- Prioritize user safety and privacy over feature usage
- Consider edge cases where the skill might be misapplied
- Reference relevant policies or ethical guidelines when applicable

## Examples

### Simple Query (Don't Use Full Pipeline)
❌ Don't: Invoke full `convergence-investigation` for "When was Python invented?"
✅ Do: Answer directly from knowledge

### Privacy-Sensitive (Need Consent)
❌ Don't: Research personal acquaintances without explicit permission
✅ Do: Ask user for consent or clarify relationship

### Resource-Intensive (Use Simpler Tool)
❌ Don't: Run `gh-wiki` for a single URL capture without integration needs
✅ Do: Use basic capture or answer directly

## Review Process

When evaluating a skill for guardrails:
1. Check if a "When NOT" section exists
2. Verify conditions are specific and actionable
3. Test edge cases against the documented restrictions
4. Update when new misuse patterns are discovered