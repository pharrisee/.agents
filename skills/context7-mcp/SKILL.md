---
name: context7-mcp
description: "Context7 MCP integration for fetching current library documentation. Use when the user asks about libraries, frameworks, API references, or needs code examples. Activates for setup questions, code generation involving libraries, or mentions of specific frameworks like React, Vue, Next.js, Prisma, Supabase, etc."
---

# Context7 MCP Documentation Fetching

## When to Use This Skill

Activate this skill automatically when the user:

- Asks setup or configuration questions ("How do I configure Next.js middleware?")
- Requests code involving libraries ("Write a Prisma query for...")
- Needs API references ("What are the Supabase auth methods?")
- Mentions specific frameworks (React, Vue, Svelte, Express, Tailwind, etc.)
- Asks about library versions or features ("What's new in React 19?")
- Needs code examples for specific library use cases

## When NOT to Use This Skill

- **Simple version lookups**: "What version of React is latest" — use package registry or general knowledge instead
- **Basic syntax questions**: Questions about JavaScript/TypeScript fundamentals — answer from general knowledge
- **Single function docs**: If only one method/function is asked about and Context7 would return the same — direct answer is sufficient
- **No framework context**: When user asks about generic web dev concepts without specific library mentions
- **Out-of-scope tools**: Questions about non-documentation topics (deployment, debugging, general programming)
- **Highly opinionated topics**: "Best framework" debates — use general knowledge and reasoning

## How to Fetch Documentation

### Step 1: Resolve the Library ID

Call `resolve-library-id` with:

```json
{
  "libraryName": "The library name from user question",
  "query": "The user's full question (improves relevance ranking)"
}
```

**Examples:**
- User: "How do I use Prisma with Next.js?"
  - `libraryName`: "prisma" (or "next.js" depending on focus)
  - `query`: "How do I use Prisma with Next.js?"

### Step 2: Select the Best Match

From the resolution results, choose based on:

1. **Exact or closest name match** to what the user asked for
2. **Higher benchmark scores** indicate better documentation quality
3. **Version-specific IDs** if user mentioned a version (e.g., "React 19")
4. **Official packages** over community forks when possible

**Selection Priority:**
- Exact name match + high benchmark score → Best choice
- Close name match + good score → Acceptable if official
- Multiple similar options → Pick highest benchmark or ask user

### Step 3: Fetch the Documentation

Call `query-docs` with:

```json
{
  "libraryId": "Selected Context7 library ID (e.g., '/vercel/next.js')",
  "query": "The user's specific question or topic"
}
```

**Query tips:**
- Be specific: "middleware authentication" vs "middleware"
- Include context: "Next.js 14 App Router middleware authentication"
- Use user's exact terms when possible

### Step 4: Use the Documentation

Once you receive results:

1. **Extract relevant code snippets** and API usage patterns
2. **Verify recency** — Context7 should provide current docs, but note if outdated
3. **Adapt to user's context** — adjust examples for their specific setup
4. **Provide complete examples** — don't just link, show full working code
5. **Note version differences** if applicable

## Example Workflows

### Workflow 1: Setup Question

**User:** "I'm setting up Next.js middleware for authentication. How do I check if a user is logged in?"

**Steps:**

1. Call `resolve-library-id`:
   ```json
   {
     "libraryName": "next.js",
     "query": "Next.js middleware authentication check if user logged in"
   }
   ```

2. Get results, select best match (e.g., `/vercel/next.js` with score 95)

3. Call `query-docs`:
   ```json
   {
     "libraryId": "/vercel/next.js",
     "query": "middleware authentication check user logged in"
   }
   ```

4. Receive documentation with code examples

5. Provide response with complete middleware example:
   ```typescript
   import { NextResponse } from 'next/server'
   import type { NextRequest } from 'next/server'
   
   export function middleware(request: NextRequest) {
     const token = request.cookies.get('auth-token')?.value
     
     if (!token) {
       return NextResponse.redirect(new URL('/login', request.url))
     }
     
     // Optionally verify token and add user to request
     return NextResponse.next()
   }
   
   export const config = {
     matcher: ['/dashboard/:path*', '/profile/:path*'],
   }
   ```

### Workflow 2: Library Comparison

**User:** "How does Prisma handle relations compared to TypeORM?"

**Steps:**

1. Call `resolve-library-id` for Prisma:
   ```json
   {"libraryName": "prisma", "query": "Prisma relations ORM"}
   ```

2. Select best Prisma match

3. Call `query-docs` for Prisma relations:
   ```json
   {"libraryId": "/prisma/prisma", "query": "relations one-to-many many-to-many"}
   ```

4. Call `resolve-library-id` for TypeORM:
   ```json
   {"libraryName": "typeorm", "query": "TypeORM relations ORM"}
   ```

5. Select best TypeORM match

6. Call `query-docs` for TypeORM relations:
   ```json
   {"libraryId": "/typeorm/typeorm", "query": "relations one-to-many many-to-many"}
   ```

7. Synthesize comparison based on both docs

**Note:** When comparing multiple libraries, fetch docs for each separately then synthesize.

### Workflow 3: API Reference Lookup

**User:** "What methods does Supabase auth have for signing in?"

**Steps:**

1. Call `resolve-library-id`:
   ```json
   {"libraryName": "supabase", "query": "Supabase auth sign in methods"}
   ```

2. Select best match (likely `/supabase/supabase`)

3. Call `query-docs`:
   ```json
   {"libraryId": "/supabase/supabase", "query": "auth sign in methods login"}
   ```

4. Provide organized list of methods with brief descriptions:
   - `signInWithPassword()` - Email/password sign in
   - `signInWithOAuth()` - OAuth provider sign in
   - `signInWithIdToken()` - Sign in with ID token
   - etc.

### Workflow 4: Code Example Generation

**User:** "Show me how to upload files to S3 using the AWS SDK in Node.js"

**Steps:**

1. Call `resolve-library-id`:
   ```json
   {"libraryName": "aws-sdk", "query": "AWS SDK S3 upload files Node.js"}
   ```

2. Select best match (likely `/aws/aws-sdk-js-v3`)

3. Call `query-docs`:
   ```json
   {"libraryId": "/aws/aws-sdk-js-v3", "query": "S3 upload file putObject"}
   ```

4. Provide complete working example with:
   - Setup/configuration
   - Error handling
   - Best practices (streaming for large files)
   - Required permissions

## Troubleshooting Common Issues

### Issue 1: Poor Relevance in Results

**Symptoms:** Documentation returned doesn't match the question

**Solutions:**

1. **Refine the query**:
   - More specific keywords
   - Include version numbers
   - Use exact error messages or method names

2. **Try different library ID**:
   - If multiple IDs returned, try the next highest-scored one
   - Some libraries have separate docs for different versions

3. **Break into smaller queries**:
   - Instead of "setup auth with middleware", try:
     - "Next.js middleware basics"
     - "Next.js auth patterns"
     - Then synthesize

### Issue 2: Library Not Found

**Symptoms:** `resolve-library-id` returns no results or poor matches

**Solutions:**

1. **Try variations of the name**:
   - "react" vs "reactjs"
   - "aws-sdk" vs "aws-sdk-js-v3"
   - Check npm package name

2. **Check if it's in the Context7 index**:
   - Some smaller/newer libraries may not be indexed
   - Check library's documentation site directly

3. **Use general knowledge**:
   - If library not in Context7, answer from general knowledge
   - Note that docs may be less current

4. **Suggest alternatives**:
   - "This library isn't in my documentation search. Similar libraries with docs available include..."

### Issue 3: Outdated Documentation

**Symptoms:** Code examples use deprecated APIs or old patterns

**Solutions:**

1. **Specify version in query**:
   ```json
   {"libraryId": "/vercel/next.js", "query": "Next.js 14 middleware"}
   ```

2. **Check version-specific IDs**:
   - Some libraries have version-specific entries
   - Look for IDs with version numbers

3. **Note the limitation**:
   - "The docs show v12 patterns. In v14, this has changed to..."
   - Cross-reference with recent changelog if available

4. **Use general knowledge**:
   - For very recent changes, Context7 may lag
   - Supplement with latest patterns you know

### Issue 4: Too Much or Irrelevant Information

**Symptoms:** Documentation returns hundreds of lines, most not relevant

**Solutions:**

1. **Make query more specific**:
   - Add more keywords
   - Include exact function names or file paths
   - Use error messages verbatim

2. **Filter the results**:
   - Focus on code blocks
   - Look for specific sections mentioned in the query
   - Extract only what's needed for the answer

3. **Multiple targeted queries**:
   - Instead of one broad query, make several focused ones
   - Combine the most relevant parts

### Issue 5: No Code Examples

**Symptoms:** Documentation is mostly conceptual, no code snippets

**Solutions:**

1. **Broaden the query**:
   - Try more general terms
   - Look for "getting started" or "examples" sections

2. **Check related topics**:
   - Query related functions or features
   - Look at similar libraries for patterns

3. **Generate examples**:
   - Use the conceptual docs to create working examples
   - Apply general patterns from the documentation
   - Note when examples are synthesized vs. from docs

### Issue 6: Rate Limiting or Errors

**Symptoms:** MCP tool calls fail or timeout

**Solutions:**

1. **Retry with backoff**:
   - Wait a few seconds and try again
   - Simplify the query if repeated failures

2. **Use cached knowledge**:
   - Fall back on general knowledge for that library
   - Note that real-time docs aren't available

3. **Alternative approach**:
   - Use web search instead if available
   - Check local cached documentation

## Best Practices

### Query Construction

**Good queries:**
- "Next.js 14 App Router dynamic routes"
- "Prisma transaction rollback error handling"
- "React Server Components fetch data pattern"
- "Supabase real-time subscribe to channel"

**Poor queries:**
- "Next.js stuff" (too vague)
- "How do I code?" (no library focus)
- "React" (no topic specified)

### Multiple Libraries

When question involves multiple libraries:

1. **Fetch docs for each library separately**
2. **Take notes on key points from each**
3. **Synthesize at the end with full context**

Example for "Next.js with Prisma":
- Fetch Next.js docs for API routes/server components
- Fetch Prisma docs for database queries
- Combine with appropriate connection patterns

### Version Management

- Always note if user specifies a version
- Use version-specific IDs when available
- Mention if docs seem outdated for latest version
- Warn about breaking changes between versions

### Code Example Quality

When providing examples from Context7:

1. **Include all necessary imports**
2. **Show complete functions/components**
3. **Add error handling where docs show it**
4. **Note any required configuration**
5. **Mention environment/dependency requirements**

## Integration with Other Skills

### With `karpathy` Skill

After fetching documentation, apply Karpathy guidelines:
- Keep code examples minimal and focused
- Avoid over-engineering based on complex examples
- Extract the simplest working pattern

### With `systematic-debugging` Skill

When docs don't solve the problem:
- Fetch docs first to understand correct usage
- Then systematically debug if still issues
- Check if implementation matches docs exactly

### With `test-driven-development` Skill

After getting docs:
- Use examples to write failing tests first
- Implement based on documented patterns
- Verify tests pass with documented approach

## Decision Tree: Use Context7 or Not?

```
User asks about library/framework/API?
  |
  +-- No --> Don't use Context7, answer from general knowledge
  |
  Yes
  |
  +-- Question about general programming concepts? --Yes--> Don't use Context7
  |                                                          (e.g., "What is MVC?")
  |
  No
  |
  +-- Specific library mentioned? --No--> Don't use Context7
  |                                           (e.g., "How do I parse JSON?")
  |
  Yes (e.g., "How do I parse JSON in Express?")
  |
  +-- Version-specific question? --Yes--> Include version in query
  |
  No
  |
  +-- Single function lookup? --Yes--> Consider if docs needed or if general knowledge suffices
  |
  No (needs examples/patterns)
  |
  +--> USE CONTEXT7
       
       After fetching:
       +-- Examples clear? --Yes--> Provide to user with context
       |                                  
       No                                  
       |
       +-- Try refined query
       |
       +-- Still unclear? --> Supplement with general knowledge and note limitations
```

## Quick Reference

### Library ID Examples

| Library | Context7 ID | Notes |
|---------|------------|-------|
| Next.js | `/vercel/next.js` | High quality |
| React | `/websites/react_dev` | Official docs |
| Prisma | `/prisma/prisma` | Complete |
| Supabase | `/supabase/supabase` | Good examples |
| Express | `/expressjs/express` | Core docs |
| Tailwind | `/websites/tailwindcss` | Comprehensive |
| Vue | `/vuejs/docs` | Official |

### Query Patterns

| Question Type | Query Pattern |
|--------------|---------------|
| Setup/Config | `"[library] setup configuration"` |
| API Methods | `"[library] [feature] methods"` |
| Code Example | `"[library] [use case] example"` |
| Best Practices | `"[library] [feature] best practices"` |
| Error/Issue | `"[library] [error message]"` |
| Pattern/Architecture | `"[library] [pattern] architecture"` |

### Red Flags (Don't Use Context7)

- Question is about general programming theory
- No specific library or framework mentioned
- Asking for opinion/recommendations
- Simple syntax questions (e.g., "how to write a for loop")
- Pure algorithm questions
- Language fundamentals (not library features)

### Green Flags (Definitely Use Context7)

- Specific library + version mentioned
- Setup/configuration question
- "How to use [X] with [Y]" patterns
- API reference lookups
- Error messages from library
- Code examples requested for specific library features
- Recent syntax or patterns (Context7 should be current)

## Quality Checklist

Before finalizing response with Context7 results:

- [ ] Library ID selection justified (best match based on name and score)
- [ ] Query was specific enough to get relevant results
- [ ] Code examples are complete (imports, setup, error handling)
- [ ] Dependencies/configuration requirements noted
- [ ] Version differences called out if relevant
- [ ] Examples adapted to user's specific context
- [ ] Multiple sources combined coherently (if applicable)
- [ ] Compared against general knowledge for major discrepancies
- [ ] Noted when examples might be from older versions