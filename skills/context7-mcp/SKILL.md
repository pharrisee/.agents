---
name: context7-mcp
description: This skill should be used when the user asks about libraries, frameworks, API references, or needs code examples. Activates for setup questions, code generation involving libraries, or mentions of specific frameworks like React, Vue, Next.js, Prisma, Supabase, etc.
---

When the user asks about libraries, frameworks, or needs code examples, use Context7 to fetch current documentation instead of relying on training data.

## When to Use This Skill

Activate this skill when the user:

- Asks setup or configuration questions ("How do I configure Next.js middleware?")
- Requests code involving libraries ("Write a Prisma query for...")
- Needs API references ("What are the Supabase auth methods?")
- Mentions specific frameworks (React, Vue, Svelte, Express, Tailwind, etc.)

## When NOT to Use This Skill

- **Simple version lookups**: "What version of React is latest" — use package registry instead
- **Basic syntax questions**: Questions about JavaScript/TypeScript fundamentals — answer from knowledge
- **Single function docs**: If only one method/function is asked about and Context7 would return the same — direct answer is sufficient
- **No framework context**: When user asks about generic web dev concepts without specific library mentions
- **Out-of-scope tools**: Questions about non-documentation topics (deployment, debugging, general programming)

## How to Fetch Documentation

### Step 1: Resolve the Library ID

Call `resolve-library-id` with:

- `libraryName`: The library name extracted from the user's question
- `query`: The user's full question (improves relevance ranking)

### Step 2: Select the Best Match

From the resolution results, choose based on:

- Exact or closest name match to what the user asked for
- **Higher benchmark scores indicate better documentation quality**
- **If the user mentioned a version (e.g., "React 19"), prefer version-specific IDs**

### Step 3: Fetch the Documentation

Call `query-docs` with:

- `libraryId`: The selected Context7 library ID (e.g., `/vercel/next.js`)
- `query`: The user's specific question

### Step 4: Use the Documentation

Incorporate the fetched documentation into your response:

- Answer the user's question using current, accurate information
- Include relevant code examples from the docs
- Cite the library version when relevant

## Implementation Notes

This skill integrates with Context7's MCP server. The Context7 API key must be available as `CONTEXT7_API_KEY` in the environment before activation. For the devcontainer setup, forward this via `remoteEnv` in your MCP client configuration.