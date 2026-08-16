#!/usr/bin/env python3
from pathlib import Path
import base64, zlib

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "scripts" / "profile_payload"
out = ROOT / "assets" / "profile" / "profile-code.svg"
order = ("part1.txt", "part1b.txt", "part2.txt", "part3.txt")
encoded = "".join((PARTS / name).read_text(encoding="utf-8").strip() for name in order)
svg = zlib.decompress(base64.b64decode(encoded)).decode("utf-8")

# GitHub READMEs do not run JavaScript. These are SVG-native SMIL effects so the
# artwork still works as a normal image if GitHub strips an animation element.
motion = r'''
<g aria-hidden="true" pointer-events="none">
  <circle cx="770" cy="205" r="126" fill="none" stroke="#e3202a" stroke-width="2" opacity="0">
    <animate attributeName="r" values="122;136;122" dur="4.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;.22;0" dur="4.8s" repeatCount="indefinite"/>
  </circle>
  <g opacity=".16">
    <path d="M886 50v45 M918 72v52 M953 39v58 M989 67v47 M1027 45v55 M1064 72v43" stroke="#686868" stroke-width="1">
      <animateTransform attributeName="transform" type="translate" values="0 -28;0 42" dur="3.8s" repeatCount="indefinite"/>
    </path>
  </g>
  <g fill="#e3202a" opacity=".6">
    <circle cx="64" cy="116" r="2"><animate attributeName="opacity" values=".2;.9;.2" dur="2.3s" repeatCount="indefinite"/></circle>
    <circle cx="1066" cy="512" r="2"><animate attributeName="opacity" values=".8;.15;.8" dur="3.1s" repeatCount="indefinite"/></circle>
  </g>
</g>
'''

if "</svg>" not in svg:
    raise SystemExit("invalid SVG template")
svg = svg.replace("</svg>", motion + "\n</svg>")
out.write_text(svg, encoding="utf-8")
print(f"wrote {out} ({len(svg.encode('utf-8'))} bytes)")
