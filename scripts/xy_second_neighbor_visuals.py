"""Generate figures for the second-neighbor classical XY note.

Pure-stdlib SVG following docs/figure-style.md.
"""
from pathlib import Path
import math

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "xy-second-neighbor"
OUT.mkdir(parents=True, exist_ok=True)

LIGHT = {
    "paper": "#f3efe6", "ink": "#171714", "muted": "#716d64",
    "line": "#cbc3b5", "accent": "#5866e9", "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19", "ink": "#f0eadf", "muted": "#a8a196",
    "line": "#4a4740", "accent": "#99a2ff", "green": "#8bc4a9",
}

W, H = 760, 440
PANELS = [(92, 56, 276, 280), (414, 56, 276, 280)]
KMIN, KMAX = 0.0, 1.25


def qstar(kappa):
    if kappa <= 0.25:
        return 0.0
    return math.acos(1.0 / (4.0 * kappa))


def stiffness(kappa):
    if kappa <= 0.25:
        return 1.0 - 4.0 * kappa
    return 4.0 * kappa - 1.0 / (4.0 * kappa)


def X(kappa, panel):
    x0, _, pw, _ = panel
    return x0 + (kappa - KMIN) / (KMAX - KMIN) * pw


def Y(value, panel, ymin, ymax):
    _, y0, _, ph = panel
    return y0 + ph - (value - ymin) / (ymax - ymin) * ph


def make_path(fn, panel, ymin, ymax):
    pts = []
    n = 240
    for i in range(n):
        k = KMIN + (KMAX - KMIN) * i / (n - 1)
        y = fn(k)
        pts.append(("M" if i == 0 else "L") + f"{X(k,panel):.1f},{Y(y,panel,ymin,ymax):.1f}")
    return " ".join(pts)


style = f'''<style>
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}} .tick{{stroke:{LIGHT['ink']};stroke-width:1.4}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1}} .guide{{stroke:{LIGHT['muted']};stroke-width:2.0;stroke-dasharray:4 6}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5}} .secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:4.0}}
.text{{fill:{LIGHT['ink']};font:17px 'Noto Sans JP',system-ui,sans-serif}} .small{{fill:{LIGHT['muted']};font:16px 'Noto Sans JP',system-ui,sans-serif}}
.math{{fill:{LIGHT['ink']};font:19px 'STIX Two Math','Cambria Math','Times New Roman',serif}} .panel{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,sans-serif;font-weight:600}}
@media(prefers-color-scheme:dark){{
.axis,.tick{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.guide{{stroke:{DARK['muted']}}}.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}
.text,.math,.panel{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
}}
</style>'''

parts = []
configs = [
    (PANELS[0], qstar, 0.0, 0.5 * math.pi, "(a)", "q*/π", "primary"),
    (PANELS[1], stiffness, 0.0, 5.0, "(b)", "A₀/J₁", "secondary"),
]

for idx, (panel, fn, ymin, ymax, plabel, ylabel, klass) in enumerate(configs):
    x0, y0, pw, ph = panel
    # major y grid/ticks
    yticks = [0.0, 0.25, 0.5] if idx == 0 else [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    for val in yticks:
        raw = val * math.pi if idx == 0 else val
        yy = Y(raw, panel, ymin, ymax)
        parts.append(f'<line class="grid" x1="{x0}" y1="{yy:.1f}" x2="{x0+pw}" y2="{yy:.1f}"/>')
        if idx == 0:
            label = "0" if val == 0 else ("1/4" if val == 0.25 else "1/2")
        else:
            label = f"{int(val)}"
        parts.append(f'<text class="small" x="{x0-10}" y="{yy+5:.1f}" text-anchor="end">{label}</text>')
    for k in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25]:
        xx = X(k, panel)
        parts += [
            f'<line class="tick" x1="{xx:.1f}" y1="{y0+ph}" x2="{xx:.1f}" y2="{y0+ph+6}"/>',
            f'<text class="small" x="{xx:.1f}" y="{y0+ph+27}" text-anchor="middle">{k:g}</text>',
        ]
    xc = X(0.25, panel)
    parts += [
        f'<line class="axis" x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}"/>',
        f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}"/>',
        f'<line class="guide" x1="{xc:.1f}" y1="{y0}" x2="{xc:.1f}" y2="{y0+ph}"/>',
        f'<path class="{klass}" d="{make_path(fn,panel,ymin,ymax)}"/>',
        f'<text class="panel" x="{x0+8}" y="{y0+22}">{plabel}</text>',
        f'<text class="math" x="{x0-48}" y="{y0+ph/2:.1f}" text-anchor="middle" transform="rotate(-90 {x0-48} {y0+ph/2:.1f})">{ylabel}</text>',
    ]

parts += [
    '<text class="math" x="381" y="416" text-anchor="middle">κ = |J₂| / J₁</text>',
    f'<text class="small" x="{X(0.25,PANELS[1])+8:.1f}" y="{PANELS[1][1]+20}" text-anchor="start">κ = 1/4</text>',
]

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{style}\n' + "\n".join(parts) + '\n</svg>\n'
(OUT / "preferred-twist-stiffness.svg").write_text(svg, encoding="utf-8")
print("generated preferred-twist-stiffness.svg")
