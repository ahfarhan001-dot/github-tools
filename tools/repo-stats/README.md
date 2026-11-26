# repo-stats

Show public stats for any public GitHub repository — stars, forks, open issues, language, created and updated dates, and license. Uses the public GitHub API, so no token or sign-in is needed.

## Usage

```bash
# Check a repository
python3 repo_stats.py ahfarhan001-dot/dev-ai-tools

# Any other public repository
python3 repo_stats.py torvalds/linux
```

Requires Python 3.8 or newer and an internet connection. No extra packages.

## Example output

```
Repository: ahfarhan001-dot/dev-ai-tools
Description: Open-source AI tools and reusable development skills for developers.
URL: https://github.com/ahfarhan001-dot/dev-ai-tools
Stars: 0
Forks: 0
Open issues: 0
Language: Python
License: MIT License
Created: 2026-11-26T15:54:00Z
Updated: 2026-11-26T15:58:00Z
```

## Notes

- The repository must be public. Private repos need a token, which this tool does not use.
- A repo that does not exist prints an error and stops.
- The public API has a rate limit (60 requests per hour without a token). If the limit is reached, wait and try again later.
- If there is no internet connection, it prints an error instead of crashing.
