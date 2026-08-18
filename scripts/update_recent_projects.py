#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime
from pathlib import Path

OWNER = os.environ.get("PROFILE_OWNER", "lhem43")
README_PATH = Path("README.md")
START = "<!-- recent-projects:start -->"
END = "<!-- recent-projects:end -->"
HEADERS = {"User-Agent": f"{OWNER}-profile-readme-updater"}


def request_json(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fmt_date(iso_text: str) -> str:
    dt = datetime.fromisoformat(iso_text.replace("Z", "+00:00"))
    return dt.strftime("%d %b %Y")


def fetch_recent_repos(owner: str, limit: int = 5):
    repos = request_json(f"https://api.github.com/users/{owner}/repos?per_page=100&sort=updated")
    repos = [r for r in repos if not r.get("fork") and r["name"] != owner]
    repos.sort(key=lambda r: r.get("pushed_at") or "", reverse=True)
    return repos[:limit]


def fetch_latest_commit(owner: str, repo: str, default_branch: str):
    commits = request_json(f"https://api.github.com/repos/{owner}/{repo}/commits?sha={default_branch}&per_page=1")
    if not commits:
        return None
    c = commits[0]
    return {
        "sha": c["sha"][:7],
        "url": c["html_url"],
        "message": c["commit"]["message"].splitlines()[0][:80],
    }


def build_section(owner: str) -> str:
    rows = []
    for repo in fetch_recent_repos(owner):
        commit = fetch_latest_commit(owner, repo["name"], repo["default_branch"])
        language = repo.get("language") or "-"
        stars = repo.get("stargazers_count", 0)
        updated = fmt_date(repo["pushed_at"])
        latest_commit = "<sub>No commits found</sub>"
        if commit:
            latest_commit = (
                f'<a href="{commit["url"]}"><code>{commit["sha"]}</code></a>'
                f'<br><sub>{commit["message"]}</sub>'
            )
        rows.append(
            "<tr>"
            f'<td><a href="{repo["html_url"]}"><b>{repo["name"]}</b></a><br><sub>{repo.get("description") or "Public repository"}</sub></td>'
            f'<td><code>{language}</code></td>'
            f'<td>{stars}</td>'
            f'<td>{latest_commit}</td>'
            f'<td><sub>{updated}</sub></td>'
            "</tr>"
        )

    return (
        f"{START}\n"
        "<h3>Recent public work</h3>\n"
        "<table>\n"
        "<thead><tr><th>Repository</th><th>Language</th><th>Stars</th><th>Latest commit</th><th>Updated</th></tr></thead>\n"
        "<tbody>\n" + "\n".join(rows) + "\n</tbody>\n"
        "</table>\n"
        "<sub>Auto-generated from public repositories by GitHub Actions.</sub>\n"
        f"{END}"
    )


def main() -> None:
    content = README_PATH.read_text(encoding="utf-8")
    start = content.index(START)
    end = content.index(END) + len(END)
    README_PATH.write_text(content[:start] + build_section(OWNER) + content[end:], encoding="utf-8")


if __name__ == "__main__":
    main()
