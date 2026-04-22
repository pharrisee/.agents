# AGENTS.md

This folder is a workspace for global agent skills and related metadata.

See https://agentskills.io/home for more information on agent skills and related resources.

## What Lives Here

- `skills/` contains the skill packages used by this workspace.
- `README.md` provides a short overview of the repository.
- `.skill-lock.json` tracks installed skill sources and versions.

## Verification

- There is no repo-wide build or test harness here.
- Verify changes with the relevant skill-local scripts or checks.
- Prefer the Python metadata rebuild path when a skill offers both Python and shell variants.

## Working Rules

- Treat each skill folder as self-contained.
- Prefer minimal, targeted edits.
- Do not add secrets, credentials, or personal data.
- Preserve the existing workspace structure unless a change is explicitly requested.
- Keep each skill folder self-contained and update only the relevant skill area.

## Editing Guidance

- Check the current file contents before modifying existing files.
- Use the smallest change that satisfies the request.
- Keep documentation clear and concise.

## Primary Entry Points

- [README.md](README.md)
- [skills/](skills/)
- [skills/gh-wiki/SKILL.md](skills/gh-wiki/SKILL.md)
- [skills/llm-wiki/SKILL.md](skills/llm-wiki/SKILL.md)
- [skills/gh-wiki-fact-checker/README.md](skills/gh-wiki-fact-checker/README.md)