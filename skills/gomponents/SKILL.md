---
name: gomponents
description: Guide for working with gomponents, a pure Go HTML component library. Use this skill when reading or writing gomponents code, or when building HTML views in Go applications.
license: MIT
---

# gomponents

## Overview

gomponents is a pure Go HTML component library that treats HTML elements as composable Go values. Everything is built on the `Node` interface, making HTML construction type-safe and composable.

## When to Use This Skill

Use this skill when:
- Reading or writing gomponents code
- Building server-side HTML views in Go applications
- Creating reusable HTML components in Go

## When NOT to Use This Skill

- **Non-Go projects**: Projects not written in or targeting Go
- **Simple HTML**: Static HTML without Go component needs
- **Frontend frameworks**: React, Vue, Angular, Svelte, etc. — use their respective tools
- **Non-component patterns**: When standard Go templates or string concatenation suffice
- **Testing-only changes**: Pure test file modifications without component logic changes

## Core Interface

Everything in gomponents implements the `Node` interface:

```go
type Node interface {
    Render(w io.Writer) error
}
```

## Non-Negotiable Rules

1. **Type safety first**: Prefer typed components over string concatenation
2. **Component composition**: Build complex UIs from simple, composable pieces
3. **Render discipline**: Always handle `error` returns from `Render()`
4. **No runtime HTML parsing**: Build structure at compile time, not runtime

## Implementation Notes

This skill focuses on server-side Go HTML generation. Use standard Go tooling (go mod, go test) alongside gomponents development.