#!/usr/bin/env python3
import html
import json
import os
import urllib.request
from datetime import datetime

OWNER = os.getenv("PROFILE_OWNER", "lhem43")
LIMIT = int(os.getenv("PROJECT_LIMIT", "4"))
TOKEN = os.getenv("GITHUB_TOKEN", "")
README = "README.md"
START = "<!-- recent-projects:start -->"
END = "<!-- recent-projects:end -->"


def api(path):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{OWNER}-profile",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def latest_commit(repo):
    branch = repo.get("default_branch")
    if not branch:
        return None
    try:
        commits = api(f"/repos/{OWNER}/{repo['name']}/commits?sha={branch}&per_page=1")
    except Exception:
        return None
    if not commits:
        return None
    c = commits[0]
    meta = c.get("commit", {})
    who = meta.get("committer") or meta.get("author") or {}
    date = who.get("date")
    message = (meta.get("message") or "").splitlines()[0].strip()
    if not date:
        return None
    return {
        "date": date,
        "url": c.get("html_url", repo["html_url"]),
        "sha": (c.get("sha") or "")[:7],
        "message": message,
    }


def esc(value):
    return html.escape(str(value or ""), quote=True)


repos = api(f"/users/{OWNER}/repos?type=owner&sort=full_name&per_page=100")
items = []
for repo in repos:
    if repo["name"] == OWNER or repo.get("fork") or repo.get("archived") or repo.get("private"):
        continue
    latest = latest_commit(repo)
    if latest:
        items.append((latest["date"], repo, latest))

items.sort(key=lambda x: x[0], reverse=True)

rows = []
for _, repo, commit in items[:LIMIT]:
    day = datetime.fromisoformat(commit["date"].replace("Z", "+00:00")).strftime("%d %b %Y")
    repo_url = repo.get("html_url") or f"https://github.com/{OWNER}/{repo['name']}"
    language = repo.get("language") or "—"
    stars = repo.get("stargazers_count", 0)
    description = repo.get("description") or "Public repository"
    rows.append(
        "<tr>"
        f"<td><a href=\"{esc(repo_url)}\"><b>{esc(repo['name'])}</b></a><br>"
        f"<sub>{esc(description)}</sub></td>"
        f"<td><code>{esc(language)}</code></td>"
        f"<td>★ {stars}</td>"
        f"<td><a href=\"{esc(commit['url'])}\"><code>{esc(commit['sha'])}</code></a><br>"
        f"<sub>{esc(commit['message'])}</sub></td>"
        f"<td><sub>{esc(day)}</sub></td>"
        "</tr>"
    )

if rows:
    content = (
        "<h3>⚡ Recent public work</h3>\n"
        "<table>\n"
        "<thead><tr><th>Repository</th><th>Language</th><th>Stars</th><th>Latest commit</th><th>Updated</th></tr></thead>\n"
        "<tbody>\n" + "\n".join(rows) + "\n</tbody>\n</table>\n"
        "<sub>Auto-generated from public repositories by GitHub Actions.</sub>"
    )
else:
    content = "<h3>⚡ Recent public work</h3>\n<p><i>No public repository activity found yet.</i></p>"

block = START + "\n" + content + "\n" + END

with open(README, encoding="utf-8") as f:
    text = f.read()
if START not in text or END not in text:
    raise SystemExit("README markers not found")
before = text.split(START, 1)[0]
after = text.split(END, 1)[1]
with open(README, "w", encoding="utf-8") as f:
    f.write(before + block + after)
