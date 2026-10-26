#!/usr/bin/env python3
"""Build assets/preview.svg, an animated slideshow that shows ONE screenshot at a time.

Put your screenshots here:
    assets/screenshots/Main.png
    assets/screenshots/Edit.png
    assets/screenshots/Add.png

Then run from the repo root:
    python tools/make_slideshow.py

No dependencies. A missing screenshot is replaced by a drawn mock, so the README never breaks.
"""
import base64
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "assets" / "screenshots"
OUT = ROOT / "assets" / "preview.svg"

SLIDES = [
    ("Main.png", "main", "Main dashboard", ["Every AI tool in one place.", "No signup required."]),
    ("Edit.png", "edit", "Edit mode", ["Add or remove links", "right from the popup."]),
    ("Add.png", "add", "Add custom links", ["Name it, paste a link,", "and your new button is ready."]),
]
TOOLS = ["Claude", "ChatGPT", "Gemini", "Perplexity", "Copilot", "Grok", "DeepSeek",
         "Mistral", "Meta AI", "Poe", "NotebookLM", "Midjourney"]

W, H = 1000, 560
FX, FY, FW, FH = 560, 50, 380, 460
SLIDE_SECONDS = 4
CYCLE = SLIDE_SECONDS * len(SLIDES)


def png_size(path):
    head = path.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path.name} is not a PNG file")
    return struct.unpack(">II", head[16:24])


def mock(kind):
    """Drawn stand-in for a screenshot (used only when the PNG is missing)."""
    w = 372
    panel = 0 if kind == "main" else 150
    h = 70 + 328 + panel + 64
    p = [f'<rect width="{w}" height="{h}" rx="10" fill="#0b0618" stroke="#7a3cff" stroke-opacity="0.6"/>',
         '<text x="16" y="38" font-family="Consolas,Courier New,monospace" font-size="24" font-weight="800" fill="#00e5ff">AI<tspan fill="#ff2bd6">Buddy</tspan></text>',
         '<text x="16" y="55" font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#a392c9">Your AI tools, one click away</text>']
    editing = kind != "main"
    p.append(f'<rect x="{w-76}" y="20" width="60" height="28" rx="6" fill="{"#00e5ff" if editing else "none"}" stroke="#00e5ff"/>')
    p.append(f'<text x="{w-46}" y="39" text-anchor="middle" font-family="Consolas,monospace" font-size="13" font-weight="700" fill="{"#02121a" if editing else "#00e5ff"}">{"Done" if editing else "Edit"}</text>')
    for i, name in enumerate(TOOLS):
        r, c = divmod(i, 3)
        x, y = 14 + c * 118, 70 + r * 82
        col = "#ff2bd6" if i % 2 == 0 else "#00e5ff"
        p.append(f'<rect x="{x}" y="{y}" width="108" height="72" rx="8" fill="#1a0f33" stroke="{col}" stroke-opacity="0.65"/>')
        p.append(f'<rect x="{x+39}" y="{y+10}" width="30" height="30" rx="7" fill="url(#ico)"/>')
        p.append(f'<text x="{x+54}" y="{y+62}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="600" fill="#f1e9ff">{name}</text>')
        if editing:
            p.append(f'<circle cx="{x+96}" cy="{y+12}" r="9" fill="#1a0610" stroke="#ff3b6b"/>')
            p.append(f'<text x="{x+96}" y="{y+17}" text-anchor="middle" font-family="Consolas,monospace" font-size="14" font-weight="700" fill="#ff3b6b">x</text>')
    if editing:
        py = 70 + 328 + 6
        filled = kind == "add"
        p.append(f'<rect x="14" y="{py}" width="344" height="138" rx="10" fill="#120a24" stroke="#00e5ff" stroke-opacity="0.5"/>')
        p.append(f'<text x="28" y="{py+26}" font-family="Consolas,monospace" font-size="13" font-weight="700" fill="#00e5ff">Add a custom link</text>')
        p.append(f'<rect x="28" y="{py+38}" width="120" height="30" rx="6" fill="#0b0618" stroke="{"#ff2bd6" if filled else "#7a3cff"}"/>')
        p.append(f'<rect x="156" y="{py+38}" width="188" height="30" rx="6" fill="#0b0618" stroke="#7a3cff"/>')
        p.append(f'<text x="38" y="{py+58}" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="{"#f1e9ff" if filled else "#6f5f99"}">{"Suno" if filled else "Name (e.g. Suno)"}</text>')
        p.append(f'<text x="166" y="{py+58}" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="{"#f1e9ff" if filled else "#6f5f99"}">{"suno.com" if filled else "URL (e.g. suno.com)"}</text>')
        p.append(f'<rect x="28" y="{py+78}" width="150" height="30" rx="6" fill="#ff2bd6"/>')
        p.append(f'<text x="103" y="{py+98}" text-anchor="middle" font-family="Consolas,monospace" font-size="12" font-weight="700" fill="#1c0316">Add button</text>')
        p.append(f'<rect x="186" y="{py+78}" width="158" height="30" rx="6" fill="none" stroke="#a392c9" stroke-opacity="0.6"/>')
        p.append(f'<text x="265" y="{py+98}" text-anchor="middle" font-family="Consolas,monospace" font-size="12" font-weight="700" fill="#a392c9">Reset to defaults</text>')
    fy = h - 54
    p.append(f'<rect x="14" y="{fy}" width="344" height="40" rx="8" fill="url(#starGrad)"/>')
    p.append(f'<text x="186" y="{fy+25}" text-anchor="middle" font-family="Consolas,monospace" font-size="13" font-weight="700" fill="#fff">&#9733; Star the repo on GitHub</text>')
    return "".join(p), w, h


def slide_content(fname, kind):
    path = SHOTS / fname
    if path.exists():
        w, h = png_size(path)
        data = base64.b64encode(path.read_bytes()).decode()
        return f'<image xlink:href="data:image/png;base64,{data}" width="{w}" height="{h}"/>', w, h, True
    return (*mock(kind), False)


def build():
    parts = []
    used_real = 0
    for i, (fname, kind, title, lines) in enumerate(SLIDES):
        frag, w, h, real = slide_content(fname, kind)
        used_real += real
        s = min((FW - 28) / w, (FH - 28) / h)
        tx, ty = FX + FW / 2 - w * s / 2, FY + FH / 2 - h * s / 2
        begin = f"{i * SLIDE_SECONDS}s"
        fade = (f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.03;0.30;0.33;1" '
                f'dur="{CYCLE}s" begin="{begin}" repeatCount="indefinite"/>')
        parts.append(f'<g opacity="0">{fade}<g transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f})">{frag}</g></g>')
        text = (f'<text x="60" y="236" font-family="Consolas,Courier New,monospace" font-size="38" font-weight="800" '
                f'fill="url(#neon)" filter="url(#glow)">{title}</text>')
        for j, ln in enumerate(lines):
            text += (f'<text x="60" y="{284 + j * 30}" font-family="Segoe UI,Arial,sans-serif" font-size="20" '
                     f'fill="#d9ccf5">{ln}</text>')
        slide_in = (f'<animateTransform attributeName="transform" type="translate" values="-24 0;0 0;0 0;24 0;24 0" '
                    f'keyTimes="0;0.04;0.30;0.33;1" dur="{CYCLE}s" begin="{begin}" repeatCount="indefinite"/>')
        parts.append(f'<g opacity="0">{fade}{slide_in}{text}</g>')
        dot_x = 66 + i * 28
        parts.append(f'<circle cx="{dot_x}" cy="430" r="6" fill="#3a2a66"/>')
        parts.append(f'<circle cx="{dot_x}" cy="430" r="6" fill="#00e5ff" filter="url(#glow)" opacity="0">{fade}</circle>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="AIBuddy screenshots: main dashboard, edit mode, add custom links">
<defs>
<linearGradient id="neon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff2bd6"/><stop offset="0.5" stop-color="#7a3cff"/><stop offset="1" stop-color="#00e5ff"/></linearGradient>
<linearGradient id="ico" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff2bd6"/><stop offset="0.6" stop-color="#7a3cff"/><stop offset="1" stop-color="#00e5ff"/></linearGradient>
<linearGradient id="starGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff2bd6"/><stop offset="0.55" stop-color="#7a3cff"/><stop offset="1" stop-color="#00e5ff"/></linearGradient>
<pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#7a3cff" stroke-opacity="0.2"/></pattern>
<radialGradient id="pg" cx="0.1" cy="0.1" r="0.6"><stop offset="0" stop-color="#ff2bd6" stop-opacity="0.4"/><stop offset="1" stop-color="#ff2bd6" stop-opacity="0"/></radialGradient>
<radialGradient id="bg2" cx="0.95" cy="0.95" r="0.6"><stop offset="0" stop-color="#00e5ff" stop-opacity="0.35"/><stop offset="1" stop-color="#00e5ff" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="clip"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#clip)">
<rect width="{W}" height="{H}" fill="#07040f"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#pg)"><animate attributeName="opacity" values="0.6;1;0.6" dur="4s" repeatCount="indefinite"/></rect>
<rect width="{W}" height="{H}" fill="url(#bg2)"><animate attributeName="opacity" values="1;0.6;1" dur="4s" repeatCount="indefinite"/></rect>
<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="#0b0618" fill-opacity="0.85"/>
{"".join(parts)}
<rect x="0" y="-12" width="{W}" height="10" fill="#fff" opacity="0.05"><animateTransform attributeName="transform" type="translate" values="0 0;0 {H+30}" dur="5s" repeatCount="indefinite"/></rect>
</g>
<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke="url(#neon)" stroke-width="3" stroke-dasharray="220 120" filter="url(#glow)"><animate attributeName="stroke-dashoffset" values="0;-340" dur="4s" repeatCount="indefinite"/></rect>
<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="12" fill="none" stroke="#7a3cff" stroke-opacity="0.45" stroke-width="2"/>
</svg>'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB), "
          f"{used_real} of {len(SLIDES)} slides use your real screenshots.")


if __name__ == "__main__":
    build()
