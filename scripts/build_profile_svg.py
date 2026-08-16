#!/usr/bin/env python3
from pathlib import Path
import base64, re, zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "scripts" / "profile_payload"
FULL_OUT = ROOT / "assets" / "profile" / "profile-code.svg"
HERO_OUT = ROOT / "assets" / "profile" / "profile-hero.svg"
order = ("part1.txt", "part1b.txt", "part2.txt", "part3.txt")
encoded = "".join((PARTS / name).read_text(encoding="utf-8").strip() for name in order)
svg = zlib.decompress(base64.b64decode(encoded)).decode("utf-8")

motion = r'''
<g aria-hidden="true" pointer-events="none">
  <circle cx="660" cy="173" r="120" fill="none" stroke="#e51f29" stroke-width="2" opacity="0">
    <animate attributeName="r" values="118;132;118" dur="4.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;.22;0" dur="4.8s" repeatCount="indefinite"/>
  </circle>
  <g opacity=".16">
    <path d="M744 28v44 M778 52v52 M814 22v58 M850 54v46 M882 35v52" stroke="#686868" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0 -24;0 38" dur="3.8s" repeatCount="indefinite"/>
    </path>
  </g>
  <g fill="#e51f29" opacity=".6">
    <circle cx="58" cy="94" r="2"><animate attributeName="opacity" values=".2;.9;.2" dur="2.3s" repeatCount="indefinite"/></circle>
    <circle cx="852" cy="410" r="2"><animate attributeName="opacity" values=".8;.15;.8" dur="3.1s" repeatCount="indefinite"/></circle>
  </g>
</g>
'''

if "</svg>" not in svg:
    raise SystemExit("invalid SVG template")
svg = svg.replace("</svg>", motion + "\n</svg>")
FULL_OUT.write_text(svg, encoding="utf-8")

# Keep only the visual hero/manifesto region in the README. The lower sections
# are native GitHub HTML so repositories and controls remain clickable.
hero = re.sub(r'(<svg\b[^>]*?)\sheight="[^"]+"', r'\1 height="620"', svg, count=1)
hero = re.sub(r'viewBox="0\s+0\s+(\d+(?:\.\d+)?)\s+\d+(?:\.\d+)?"', r'viewBox="0 0 \1 620"', hero, count=1)
HERO_OUT.write_text(hero, encoding="utf-8")

print(f"wrote {FULL_OUT} ({len(svg.encode('utf-8'))} bytes)")
print(f"wrote {HERO_OUT} ({len(hero.encode('utf-8'))} bytes)")
