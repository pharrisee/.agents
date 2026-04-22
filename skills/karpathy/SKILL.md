---
name: karpathy
description: "Guidelines to reduce common LLM coding mistakes, derived from Karpathy's observations. Emphasizes thinking before coding, simplicity first, surgical changes, and goal-driven execution."
---

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks (simple typo fixes, obvious one-liners), use judgment — not every change needs the full rigor.

## When to Use This Skill

- Complex coding tasks requiring systematic planning
- Debugging intricate issues needing structured approach
- Architecture decisions with multiple trade-offs
- Code review and improvement scenarios
- Learning new patterns or paradigms

## When NOT to Use This Skill

- **Simple typo fixes**: Obvious corrections (spelling, syntax errors)
- **One-liner solutions**: Single-line fixes or straightforward implementations
- **Already-working code**: No need for analysis if code is functioning correctly
- **Trivial refactors**: Renaming variables without logic changes
- **Copy-paste tasks**: Repetitive code with no customization needed
- **Time-critical debugging**: Production incidents requiring immediate fixes
- **Opinion-based preferences**: Style debates without technical impact
- **Documentation-only changes**: Non-code modifications (comments, README)

## Core Guidelines

### 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

## Implementation Notes

These guidelines are heuristics, not rules. Use professional judgment. The bias toward caution prevents common but hard-to-debug errors, but should not paralyze action on clear, simple tasks.

## Quality Checks

Before implementing, ask:
1. Can this be solved with existing code?
2. What are the assumptions I'm making?
3. What's the simplest solution that works?
4. What edge cases actually matter?
5. Can I verify this with a test?

## Related Context

These guidelines complement the broader agent framework but should not override domain-specific best practices or project conventions.