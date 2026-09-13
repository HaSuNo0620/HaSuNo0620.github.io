"""Generate the Ising–XY spatial-filter crossover comparison.

Two panels compare exact crossover scale with its low-temperature asymptote.
The horizontal axis is K = beta J, so moving right means lowering temperature.
Pure-stdlib SVG following docs/figure-style.md; transparent canvas.
"""
from pathlib import Path
import math

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-xy-comparison"
OUT.mkdir(parents=True, exist_ok=True)

LIGHT = {"paper":"#f3efe6","ink":"#171714","muted":"#716d64","line":"#cbc3b5","accent":"#5866e9","green":"#39705a"}
DARK  = {"paper":"#1c1c19","ink":"#f0eadf","muted":"#a8a196","line":"#4a4740","accent":"#99a2ff","green":"#8bc4a9"}

W, H = 760, 440
PANELS = [(92, 54, 276, 286), (414, 54, 276, 286)]
KMIN, KMAX = 0.35, 6.0
QMIN, QMAX = 1e-5, 2.0


def simpson(f, a, b, n=1000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def bessel_i(m, x):
    # Integral definition used in the accompanying XY note.
    return simpson(lambda p: math.exp(x * math.cos(p)) * math.cos(m * p), 0.0, math.pi) / math.pi


def q_ising(K):
    return -math.log(math.tanh(K))


def q_xy(K):
    return -math.log(bessel_i(1, K) / bessel_i(0, K))


def q_ising_asym(K):
    return 2.0 * math.exp(-2.0 * K)


def q_xy_asym(K):
    return 1.0 / (2.0 * K)


def X(K, panel):
    x0, _, pw, _ = panel
    return x0 + (K - KMIN) / (KMAX - KMIN) * pw


def Y(q, panel):
    _, y0, _, ph = panel
    a, b = math.log10(QMIN), math.log10(QMAX)
    return y0 + ph - (math.log10(max(q, QMIN)) - a) / (b - a) * ph


def path(fn, panel):
    pts = []
    for i in range(220):
        K = KMIN + (KMAX - KMIN) * i / 219
        pts.append(("M" if i == 0 else "L") + f"{X(K, panel):.1f},{Y(fn(K), panel):.1f}")
    return " ".join(pts)


style = f'''<style>
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}} .tick{{stroke:{LIGHT['ink']};stroke-width:1.4}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1}} .exact{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5}}
.asym{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-dasharray:10 7}}
.text{{fill:{LIGHT['ink']};font:17px 'Noto Sans JP',system-ui,sans-serif}} .small{{fill:{LIGHT['muted']};font:16px 'Noto Sans JP',system-ui,sans-serif}}
.math{{fill:{LIGHT['ink']};font:19px 'STIX Two Math','Cambria Math','Times New Roman',serif}} .panel{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,sans-serif;font-weight:600}}
.labelbox{{fill:{LIGHT['paper']};fill-opacity:.88;stroke:{LIGHT['ink']};stroke-opacity:.10}}
@media(prefers-color-scheme:dark){{
.axis,.tick{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.exact{{stroke:{DARK['accent']}}}.asym{{stroke:{DARK['green']}}}
.text,.math,.panel{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}.labelbox{{fill:{DARK['paper']};stroke:{DARK['ink']}}}
}}
</style>'''

parts = []
models = [
    (PANELS[0], "Ising", q_ising, q_ising_asym),
    (PANELS[1], "XY", q_xy, q_xy_asym),
]

for idx, (panel, model, exact, asym) in enumerate(models):
    x0, y0, pw, ph = panel

    for q, label in [(1e-4, '10⁻⁴'), (1e-3, '10⁻³'), (1e-2, '10⁻²'), (1e-1, '10⁻¹'), (1, '1')]:
        yy = Y(q, panel)
        parts.append(f'<line class="grid" x1="{x0}" y1="{yy:.1f}" x2="{x0+pw}" y2="{yy:.1f}"/>')
        if idx == 0:
            parts.append(f'<text class="small" x="{x0-10}" y="{yy+5:.1f}" text-anchor="end">{label}</text>')

    for K in [0.5, 1, 2, 4, 6]:
        xx = X(K, panel)
        parts += [
            f'<line class="tick" x1="{xx:.1f}" y1="{y0+ph}" x2="{xx:.1f}" y2="{y0+ph+6}"/>',
            f'<text class="small" x="{xx:.1f}" y="{y0+ph+26}" text-anchor="middle">{K:g}</text>',
        ]

    parts += [
        f'<line class="axis" x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}"/>',
        f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}"/>',
        f'<path class="exact" d="{path(exact, panel)}"/>',
        f'<path class="asym" d="{path(asym, panel)}"/>',
        f'<text class="panel" x="{x0+8}" y="{y0+22}">({chr(97+idx)}) {model}</text>',
    ]

    # Paper-backed direct labels: exact (solid blue) and low-T asymptote (green dashed).
    Ke = 2.3 if idx == 0 else 2.2
    xe, ye = X(Ke, panel), Y(exact(Ke), panel)
    parts += [
        f'<rect class="labelbox" x="{xe-6:.1f}" y="{ye-27:.1f}" width="72" height="23" rx="4"/>',
        f'<text class="text" x="{xe+2:.1f}" y="{ye-10:.1f}">exact</text>',
    ]

    Ka = 3.2 if idx == 0 else 3.0
    xa, ya = X(Ka, panel), Y(asym(Ka), panel)
    parts += [
        f'<rect class="labelbox" x="{xa-8:.1f}" y="{ya+7:.1f}" width="121" height="23" rx="4"/>',
        f'<text class="small" x="{xa:.1f}" y="{ya+24:.1f}">low-T asymptote</text>',
    ]

parts += [
    '<text class="math" x="381" y="418" text-anchor="middle">K = βJ</text>',
    '<text class="math" x="28" y="197" text-anchor="middle" transform="rotate(-90 28 197)">q_× = ξ⁻¹</text>',
]

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{style}\n' + "\n".join(parts) + '\n</svg>\n'
(OUT / 'qxi-temperature-filter.svg').write_text(svg, encoding='utf-8')
print('generated qxi-temperature-filter.svg')
