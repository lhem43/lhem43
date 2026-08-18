#!/usr/bin/env python3
from pathlib import Path
import base64
import hashlib
import struct

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD_DIR = ROOT / "scripts" / "hero_payload_final"
OUT = ROOT / "assets" / "profile" / "profile-hero.webp"

parts = sorted(PAYLOAD_DIR.glob("part*.txt"))
if not parts:
    raise SystemExit("no hero payload parts found")

encoded = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
try:
    data = base64.b64decode(encoded, validate=True)
except Exception as exc:
    raise SystemExit(f"invalid hero payload base64: {exc}") from exc

# Validate the WebP container itself. This catches exactly the failure we had:
# a file with a RIFF/WEBP header whose bytes were truncated during upload.
if len(data) < 20:
    raise SystemExit(f"hero payload is implausibly small: {len(data)} bytes")
if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
    raise SystemExit("hero payload is not a RIFF WebP file")

declared_size = struct.unpack("<I", data[4:8])[0] + 8
if declared_size != len(data):
    raise SystemExit(
        f"truncated/corrupt WebP: RIFF declares {declared_size} bytes, got {len(data)}"
    )

# Walk RIFF chunks to ensure every chunk is fully present.
pos = 12
while pos < len(data):
    if pos + 8 > len(data):
        raise SystemExit(f"truncated WebP chunk header at byte {pos}")
    chunk_size = struct.unpack("<I", data[pos + 4:pos + 8])[0]
    end = pos + 8 + chunk_size
    if end > len(data):
        raise SystemExit(
            f"truncated WebP chunk at byte {pos}: needs {end}, file has {len(data)}"
        )
    pos = end + (chunk_size & 1)

if pos != len(data):
    raise SystemExit(f"invalid WebP chunk alignment: ended at {pos}, size is {len(data)}")

actual_sha = hashlib.sha256(data).hexdigest()
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_bytes(data)
print(f"wrote {OUT} ({len(data)} bytes, sha256={actual_sha})")
