#!/usr/bin/env python3
from pathlib import Path
import base64, zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "scripts" / "profile_payload"
out = ROOT / "assets" / "profile" / "profile-code.svg"
order = ("part1.txt", "part1b.txt", "part2.txt", "part3.txt")
encoded = "".join((PARTS / name).read_text(encoding="utf-8").strip() for name in order)
svg = zlib.decompress(base64.b64decode(encoded))
out.write_bytes(svg)
print(f"wrote {out} ({len(svg)} bytes)")
