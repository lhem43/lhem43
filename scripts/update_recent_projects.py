#!/usr/bin/env python3

import html
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

OWNER = os.getenv("PROFILE_OWNER", "lhem43")
PROFILE_REPO = os.getenv("PROFILE_REPO", OWNER)
LIMIT = int(os.getenv("PROJECT_LIMIT", "4"))
README = os.getenv("README_PATH", "README.md")
TOKEN = os.getenv("GITHUB_TOKEN", "")

START = "<!-- recent-projects:start -->"
END = "<!-- recent