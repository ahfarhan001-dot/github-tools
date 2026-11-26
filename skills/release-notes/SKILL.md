---
name: release-notes
description: Draft release notes from a git log — what changed, breaking changes, and contributors — in a clean format. Use when the user asks for release notes, or before tagging a new version.
---

# Release Notes

Turn a git log into release notes a user can actually read. Short, honest, and grouped by what changed.

## How to work

1. **Read the log** between the last release tag and now (`git log <last-tag>..HEAD`). If there is no tag yet, use the whole log.
2. **Group the changes:**
   - **New** — features and additions
   - **Fixed** — bug fixes
   - **Changed** — behaviour that is different now, including breaking changes
   - **Docs** — documentation only
3. **Flag breaking changes clearly.** If a change needs users to do something different, put it at the top of its group and say exactly what changes for them.
4. **Credit contributors.** List everyone who committed in the range, once each, with their commit count.

## Output format

```
## v1.1.0 — 2026-11-26

### New
- Added git-stats: repo stats from git log

### Fixed
- Fixed crash when scanning an empty folder

### Breaking changes
- None

### Contributors
- AH Farhan (4 commits)
```

- One line per change, starting with a verb, no full stop at the end.
- Keep the whole note under one screen of text. If it doesn't fit, the version did too much at once — say so.

## Rules

- Only list changes that are really in the log. Never invent features or fixes.
- If a commit message is unclear, read the diff before describing it — don't guess what it did.
- If there is nothing to release, say so instead of writing empty notes.
