#!/usr/bin/env python3
from pathlib import Path
import base64
import hashlib

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD_DIR = ROOT / "scripts" / "hero_payload_final"
OUT = ROOT / "assets" / "profile" / "profile-hero.webp"
EXPECTED_SIZE = 63394
EXPECTED_SHA256 = "2b49fb25f0cc06f06a43927d2f901f48bd14f9425889765575978881b1abf602"

parts = sorted(PAYLOAD_DIR.glob("part*.txt"))
if len(parts) != 11:
    raise SystemExit(f"expected 11 hero payload parts, found {len(parts)}")

encoded = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
try:
    data = base64.b64decode(encoded, validate=True)
except Exception as exc:
    raise SystemExit(f"invalid hero payload: {exc}") from exc

actual_size = len(data)
actual_sha = hashlib.sha256(data).hexdigest()
if actual_size != EXPECTED_SIZE:
    raise SystemExit(f"hero size mismatch: {actual_size} != {EXPECTED_SIZE}")
if actual_sha != EXPECTED_SHA256:
    raise SystemExit(f"hero checksum mismatch: {actual_sha} != {EXPECTED_SHA256}")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_bytes(data)
print(f"wrote {OUT} ({actual_size} bytes, sha256={actual_sha})")
