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

## Implementation Notes

These guidelines are heuristics, not rules. Use professional judgment. The bias toward caution prevents common but hard-to-debug errors, but should not paralyze action on clear, simple tasks.

### Pre-Implementation Checklist

Before writing any code, run through this quick checklist:

- [ ] **Requirements clarity**: Can I state the problem in one sentence?
- [ ] **Existing solutions**: Have I searched for similar code in the codebase?
- [ ] **Testability**: How will I verify this works?
- [ ] **Edge cases**: What are the 2-3 most likely failure modes?
- [ ] **Dependencies**: What does this depend on? What depends on this?
- [ ] **Reversibility**: Can this change be easily undone if wrong?

### Surgical Change Protocol

For modifying existing code:

1. **Identify the minimal touch surface** — What's the smallest set of lines that need to change?
2. **Preserve behavior** — Ensure existing functionality remains intact
3. **One concern at a time** — Don't mix refactoring with feature changes
4. **Follow the existing patterns** — Match the codebase style, not your preferences
5. **Document the why, not the what** — Comments should explain reasoning, not restate code

### Code Review Lens

When reviewing PRs or code changes, apply these filters:

- **Assumption surfacing**: Are hidden assumptions being made?
- **Scope creep**: Is the change doing more than intended?
- **Complexity justification**: Is the added complexity necessary?
- **Alternative consideration**: Were simpler options considered and rejected (with reason)?
- **Test coverage**: Are edge cases actually tested, not just happy path?

## Common Anti-Patterns

### LLM-Specific Coding Mistakes

- **Hallucinated APIs**: Using library functions that don't exist — verify with docs
- **Over-engineering**: Creating abstractions for single-use cases
- **Pattern matching without understanding**: Copying code structure without grasping intent
- **Silent error swallowing**: Catching exceptions without handling or logging
- **Type confusion**: Mixing data types without clear boundaries
- **Magic values**: Hardcoding values that should be parameters or constants
- **Temporal coupling**: Assuming order of operations without enforcing it

### Red Flags

- "This should work" — indicates lack of verification
- Multiple nested conditionals (>3 levels) — indicates missing abstraction
- Comments explaining what code does (not why) — indicates unclear code
- Functions >50 lines — indicates missing decomposition
- Duplicate logic — indicates missing extraction

## Workflow Integration

### Combine With These Skills

**Use karpathy guidelines BEFORE:**
- `test-driven-development` — Write tests first, then minimal code
- `systematic-debugging` — Understand the problem before fixing
- `writing-plans` — Plan complex changes thoroughly
- `requesting-code-review` — Ensure quality before review

**Use karpathy guidelines AFTER:**
- `subagent-driven-development` — Review generated code for over-engineering
- `claude-code` / `opencode` / `codex` — Verify autonomous agent output

### Verification Steps

After implementing:

1. **The 5-Minute Rule**: Can you explain what this does and why in 5 minutes?
2. **The Deletion Test**: If you removed half the code, would it still work?
3. **The Onboarding Test**: Could a new team member understand this in 10 minutes?
4. **The Change Test**: If requirements shift slightly, how hard is this to modify?

## Quality Checks

Before implementing, ask:
1. Can this be solved with existing code?
2. What are the assumptions I'm making?
3. What's the simplest solution that works?
4. What edge cases actually matter?
5. Can I verify this with a test?

## Related Context

These guidelines complement the broader agent framework but should not override domain-specific best practices or project conventions.

### When to Override

- **Performance-critical paths**: Sometimes complexity is necessary for speed
- **Security requirements**: Additional validation/abstraction may be needed
- **External API constraints**: May require non-idiomatic code
- **Legacy system integration**: Working within existing constraints

Always document why you're deviating from these guidelines.