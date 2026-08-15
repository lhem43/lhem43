#!/usr/bin/env python3
import json, os, urllib.request
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
    return date, c.get("html_url", repo["html_url"]), message


repos = api(f"/users/{OWNER}/repos?type=owner&sort=full_name&per_page=100")
items = []
for repo in repos:
    if repo["name"] == OWNER or repo.get("fork") or repo.get("archived") or repo.get("private"):
        continue
    latest = latest_commit(repo)
    if latest:
        items.append((latest[0], latest[1], latest[2], repo))

items.sort(key=lambda x: x[0], reverse=True)
lines = []
for date, commit_url, message, repo in items[:LIMIT]:
    day = datetime.fromisoformat(date.replace("Z", "+00:00")).strftime("%d %b %Y")
    lines.append(f"**[{repo['name']}]({repo['html_url']})**  ")
    lines.append(f"<sub>[{day}]({commit_url}) · {message}</sub>\n")

block = START + "\n" + ("\n".join(lines) if lines else "_No public work yet._") + "\n" + END
with open(README, encoding="utf-8") as f:
    text = f.read()
if START not in text or END not in text:
    raise SystemExit("README markers not found")
before = text.split(START, 1)[0]
after = text.split(END, 1)[1]
with open(README, "w", encoding="utf-8") as f:
    f.write(before + block + after)
