# github-tools

Open-source tools and reusable skills for working with GitHub repositories. Small, practical things that help you check a repo at a glance and write clean release notes — built in the open, free for everyone to use.

## What's inside

### Skills (`skills/`)

Reusable skill packs you can drop into your AI coding setup. Each skill is a single folder with a `SKILL.md` that tells the AI exactly how to do one job well.

| Skill | What it does |
| --- | --- |
| [release-notes](skills/release-notes/) | Drafts release notes from a git log — what changed, breaking changes, and contributors — in a clean format. |

### Tools (`tools/`)

Small command-line tools you can run right away. No setup, no dependencies beyond Python 3.

| Tool | What it does |
| --- | --- |
| [repo-stats](tools/repo-stats/) | Fetches the public GitHub API for any public repo and prints stars, forks, open issues, language, dates, and license — no token needed. |

## Quick start

```bash
git clone https://github.com/ahfarhan001-dot/github-tools.git
cd github-tools

# Check a public repository
python3 tools/repo-stats/repo_stats.py ahfarhan001-dot/dev-ai-tools
```

Skills are plain Markdown — copy a skill folder into your AI tool's skills directory and it just works.

## About this project

This is a new project, started in November 2026. It is small and growing — there are no download counts or user numbers to show yet, and none are claimed here.

## Roadmap

- More skills: changelog-writer, issue-triage
- More tools: contributor list, stale-repo checker
- Every addition stays small, documented, and dependency-free where possible

## Contributing

Found a bug or want to add a skill or tool? Open an issue or a pull request on GitHub. Keep it small, keep it documented, keep it working.

## License

MIT — see [LICENSE](LICENSE).
