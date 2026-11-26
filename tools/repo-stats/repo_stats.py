#!/usr/bin/env python3
"""Show public stats for a GitHub repository, no token needed.

Usage:
    python3 repo_stats.py owner/repo

Uses the public GitHub API (https://api.github.com). Needs internet.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

API = "https://api.github.com/repos/{}"


def fetch(repo):
    """Fetch the repo record from the public GitHub API."""
    request = urllib.request.Request(
        API.format(repo), headers={"User-Agent": "repo-stats"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo",
                        help="repository as owner/name, e.g. ahfarhan001-dot/dev-ai-tools")
    args = parser.parse_args(argv)

    if args.repo.count("/") != 1 or args.repo.startswith("/") or args.repo.endswith("/"):
        print("Error: use the form owner/repo, e.g. ahfarhan001-dot/dev-ai-tools",
              file=sys.stderr)
        return 1

    try:
        data = fetch(args.repo)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: repository '{args.repo}' not found.", file=sys.stderr)
        elif e.code == 403:
            print("Error: GitHub API rate limit reached. Try again later.",
                  file=sys.stderr)
        else:
            print(f"Error: GitHub API returned HTTP {e.code}.", file=sys.stderr)
        return 1
    except urllib.error.URLError:
        print("Error: could not reach api.github.com. Check your internet connection.",
              file=sys.stderr)
        return 1

    license_info = data.get("license") or {}
    print(f"Repository: {data.get('full_name')}")
    print(f"Description: {data.get('description') or '(none)'}")
    print(f"URL: {data.get('html_url')}")
    print(f"Stars: {data.get('stargazers_count')}")
    print(f"Forks: {data.get('forks_count')}")
    print(f"Open issues: {data.get('open_issues_count')}")
    print(f"Language: {data.get('language') or '(none)'}")
    print(f"License: {license_info.get('name') or '(none)'}")
    print(f"Created: {data.get('created_at')}")
    print(f"Updated: {data.get('updated_at')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
