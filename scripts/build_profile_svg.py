#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "profile" / "profile-hero.svg"
OUT.parent.mkdir(parents=True, exist_ok=True)

svg = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1149" height="540" viewBox="0 0 1149 540" role="img" aria-labelledby="title desc">
  <title id="title">leemanh — Data Engineer</title>
  <desc id="desc">Editorial profile hero drawn as SVG code, with a Vietnamese-star-inspired emblem and manifesto panel.</desc>
  <defs>
    <style>
      .sans{font-family:Inter,Segoe UI,Arial,sans-serif}
      .serif{font-family:Georgia,Times New Roman,serif}
      .mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
      .ink{fill:#111}.muted{fill:#6f6f6f}.soft{fill:#919191}.red{fill:#e3222a}.gold{fill:#f4c542}
      .cap{letter-spacing:4px;font-size:11px}
    </style>
    <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f8f7f4"/>
      <stop offset="1" stop-color="#f2f1ee"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-opacity="0.12"/></filter>
    <filter id="blur"><feGaussianBlur stdDeviation="7"/></filter>
    <pattern id="rain" width="18" height="60" patternUnits="userSpaceOnUse" patternTransform="rotate(5)">
      <line x1="2" y1="0" x2="2" y2="55" stroke="#bbbbbb" stroke-width="1" opacity="0.16"/>
    </pattern>
    <clipPath id="sunClip"><circle cx="856" cy="150" r="108"/></clipPath>
  </defs>

  <rect width="1149" height="540" fill="url(#paper)"/>
  <rect x="558" y="0" width="591" height="398" fill="url(#rain)" opacity="0.7"/>
  <path d="M559 0c102 34 178 5 300 23 111 17 184 8 290 6v45c-86 2-153 12-225 3-100-14-173 5-258-12-52-10-82-29-107-43z" fill="#d5d5d5" opacity="0.55"/>
  <path d="M1002 249c44 10 96 6 147-5v100c-45-7-84-5-122-3-27 2-52-6-74-23 27-17 43-41 49-69z" fill="#d7d7d7" opacity="0.45"/>

  <g transform="translate(34 35)">
    <g stroke="#e3222a" stroke-width="1.3" fill="none">
      <circle cx="13" cy="13" r="9"/>
      <line x1="13" y1="0" x2="13" y2="5"/><line x1="13" y1="21" x2="13" y2="26"/>
      <line x1="0" y1="13" x2="5" y2="13"/><line x1="21" y1="13" x2="26" y2="13"/>
      <line x1="4" y1="4" x2="7.5" y2="7.5"/><line x1="18.5" y1="18.5" x2="22" y2="22"/>
      <line x1="4" y1="22" x2="7.5" y2="18.5"/><line x1="18.5" y1="7.5" x2="22" y2="4"/>
    </g>
    <text x="38" y="18" class="sans red" font-size="18" font-weight="700">leemanh</text>
    <text x="118" y="18" class="mono soft" font-size="14">/ README.md</text>
  </g>

  <g transform="translate(72 104)">
    <g>
      <g stroke="#e3222a" stroke-width="1.4" fill="none" transform="translate(0 -6)">
        <circle cx="11" cy="10" r="7"/>
        <line x1="11" y1="0" x2="11" y2="4"/><line x1="11" y1="16" x2="11" y2="20"/>
        <line x1="1" y1="10" x2="5" y2="10"/><line x1="17" y1="10" x2="21" y2="10"/>
      </g>
      <text x="34" y="4" class="sans muted" font-size="15">Data is the blade. Truth is the path.</text>
      <line x1="354" y1="-6" x2="406" y2="-6" stroke="#e3222a" stroke-width="2"/>
    </g>
    <text x="0" y="108" class="serif ink" font-size="108" font-weight="700">leemanh</text>
    <line x1="0" y1="146" x2="32" y2="146" stroke="#e3222a" stroke-width="3"/>
    <text x="50" y="152" class="sans soft cap">DATA ENGINEER</text>
    <text x="0" y="214" class="serif ink" font-size="23">I build calm systems that turn moving data</text>
    <text x="0" y="250" class="serif ink" font-size="23">into <tspan fill="#e3222a" font-weight="700">clarity</tspan>, dependable flow, and</text>
    <text x="0" y="286" class="serif ink" font-size="23"><tspan fill="#e3222a" font-weight="700">decisions</tspan> people can stand on.</text>
  </g>

  <g>
    <circle cx="856" cy="150" r="114" fill="#f4c542" opacity="0.18" filter="url(#blur)"/>
    <circle cx="856" cy="150" r="108" fill="#e3222a"/>
    <path d="M856 83l24 48 53 8-38 37 9 53-48-25-48 25 9-53-38-37 53-8z" fill="#f4c542" filter="url(#shadow)"/>
    <g clip-path="url(#sunClip)" opacity="0.95">
      <path d="M744 101c38 11 70 9 108 7 58-2 109 8 145 22-62-4-111 2-163 0-27-1-57-6-90-16z" fill="#f7f4ed"/>
      <path d="M742 176c51-14 96-9 140-6 35 2 76 8 120 24-48-3-89 6-132 5-43-1-85-6-128-23z" fill="#f7f4ed" opacity="0.9"/>
    </g>

    <g class="sans muted" font-size="14">
      <text x="962" y="82">Burn like the sun.</text>
      <text x="962" y="108">Refine like the rain.</text>
      <text x="962" y="134">Cut like the blade.</text>
      <line x1="956" y1="58" x2="956" y2="150" stroke="#8d8d8d" stroke-width="1.8"/>
    </g>

    <path d="M777 211c19-22 40-33 63-33 14 0 26 4 39 14-11 1-22 6-31 14 27 4 48 13 62 26 18 16 28 37 31 64 2 25 1 53-5 85-7 40-16 73-27 100-47 2-91-5-134-21-10-24-13-57-9-99 4-44 11-84 21-119 10-14 6-7 18-31-16 13-32 33-48 62-6 11-11 22-17 35l-25-9c14-40 35-74 62-103z" fill="#111" opacity="0.96"/>
    <circle cx="845" cy="177" r="18" fill="#111"/>
    <path d="M824 170c7-7 16-10 27-10 9 0 17 3 24 10-13 1-23 3-30 7-8 3-16 10-23 20-2-10-1-19 2-27z" fill="#2f2f2f"/>
    <path d="M803 206c11 3 29 4 54 2 19-1 31-1 39 1-10 11-17 21-19 30 17 22 33 46 49 72-25-20-44-38-58-53-16-17-34-32-54-47 1-3 0-4-1-5-5-4-8-5-10 0z" fill="#f4f1ea" opacity="0.86"/>
    <path d="M859 246c24 18 40 28 48 31 8 2 18 2 29-2-9 14-19 24-30 30-11 6-23 8-37 8-15-16-29-40-40-72 10-1 20 1 30 5z" fill="#202020" opacity="0.75"/>
    <path d="M918 225l-62 161" stroke="#111" stroke-width="6.5" stroke-linecap="round"/>
    <path d="M774 382c-18 13-38 23-59 31-18 6-34 10-50 12 9-12 18-24 27-36-16 5-32 6-49 4 19-12 42-19 68-22 16-17 27-32 34-47 7 20 17 39 29 58z" fill="#111" opacity="0.95"/>
    <ellipse cx="846" cy="431" rx="144" ry="15" fill="#111" opacity="0.12"/>
    <path d="M982 386c22-4 48-4 77-2 38 3 67 0 90-8-14 10-31 18-52 24-29 8-66 10-111 6-14-1-29-8-43-20 12 1 25 1 39 0z" fill="#111" opacity="0.18"/>
  </g>

  <g transform="translate(63 397)" filter="url(#shadow)">
    <rect x="0" y="0" width="995" height="106" fill="#fbfaf7" stroke="#cfcfcf"/>
    <g transform="translate(38 22)" stroke="#e3222a" fill="none" stroke-width="4" stroke-linecap="round">
      <path d="M4 8h34"/><path d="M8 8v52"/><path d="M8 60h42"/><path d="M38 8c0 20-5 34-22 40"/>
    </g>
    <text x="145" y="40" class="sans ink" font-size="15" font-weight="700">A GOOD SYSTEM FEELS INEVITABLE.</text>
    <text x="145" y="66" class="sans ink" font-size="15" font-weight="700">IT TURNS NOISE INTO TRUSTED FLOW.</text>
    <text x="145" y="88" class="sans red" font-size="13" font-weight="700">TRUST. FLOW. PURPOSE.</text>
    <line x1="420" y1="18" x2="420" y2="88" stroke="#d4d4d4"/>
    <line x1="626" y1="18" x2="626" y2="88" stroke="#d4d4d4"/>
    <line x1="814" y1="18" x2="814" y2="88" stroke="#d4d4d4"/>

    <g transform="translate(440 18)">
      <g stroke="#e3222a" fill="none" stroke-width="1.8"><circle cx="18" cy="18" r="13"/><line x1="18" y1="1" x2="18" y2="7"/><line x1="18" y1="29" x2="18" y2="35"/><line x1="1" y1="18" x2="7" y2="18"/><line x1="29" y1="18" x2="35" y2="18"/></g>
      <text x="50" y="16" class="sans ink" font-size="12" font-weight="700">LIKE THE SUN</text>
      <text x="50" y="38" class="sans muted" font-size="12">Set direction first.</text>
      <text x="50" y="56" class="sans muted" font-size="12">Speed follows clarity.</text>
    </g>

    <g transform="translate(646 18)">
      <path d="M11 28h27c5 0 9-4 9-8 0-5-4-8-9-8-2-8-14-12-22-6-4 0-7 3-8 6-6 1-10 6-10 11 0 3 1 5 2 5h6" fill="none" stroke="#e3222a" stroke-width="1.8"/>
      <line x1="8" y1="38" x2="4" y2="46" stroke="#e3222a" stroke-width="1.6"/><line x1="21" y1="38" x2="17" y2="46" stroke="#e3222a" stroke-width="1.6"/><line x1="34" y1="38" x2="30" y2="46" stroke="#e3222a" stroke-width="1.6"/>
      <text x="58" y="16" class="sans ink" font-size="12" font-weight="700">LIKE THE RAIN</text>
      <text x="58" y="38" class="sans muted" font-size="12">Improve in silence.</text>
      <text x="58" y="56" class="sans muted" font-size="12">Let consistency speak.</text>
    </g>

    <g transform="translate(834 18)">
      <path d="M0 34l23-23 8-1-1 8-23 23z" fill="none" stroke="#e3222a" stroke-width="1.8"/>
      <path d="M16 17l8 8" stroke="#e3222a" stroke-width="1.8"/>
      <text x="44" y="16" class="sans ink" font-size="12" font-weight="700">LIKE A SWORD</text>
      <text x="44" y="38" class="sans muted" font-size="12">Remove what blurs truth.</text>
      <text x="44" y="56" class="sans muted" font-size="12">Keep the edge.</text>
    </g>
  </g>

  <g opacity="0.8" pointer-events="none">
    <circle cx="856" cy="150" r="118" fill="none" stroke="#e3222a" stroke-width="2" opacity="0">
      <animate attributeName="r" values="112;124;112" dur="4.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;.16;0" dur="4.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="675" cy="389" r="2.4" fill="#111"><animate attributeName="opacity" values=".75;.18;.75" dur="3.2s" repeatCount="indefinite"/></circle>
    <circle cx="1034" cy="432" r="2.4" fill="#e3222a"><animate attributeName="opacity" values=".2;.8;.2" dur="2.8s" repeatCount="indefinite"/></circle>
  </g>
</svg>
'''

OUT.write_text(svg, encoding="utf-8")
print(f"wrote {OUT} ({len(svg.encode('utf-8'))} bytes)")
