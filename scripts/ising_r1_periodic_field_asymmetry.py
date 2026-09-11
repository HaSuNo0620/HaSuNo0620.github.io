"""Generate the asymmetric AABB response-structure map.

Pure stdlib SVG following the site's Figure/Diagram Style rules.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r1-periodic-field"
OUT.mkdir(parents=True, exist_ok=True)

LIGHT = {
    "paper": "#f3efe6", "paper2": "#ebe5d9", "ink": "#171714",
    "muted": "#716d64", "line": "#cbc3b5", "accent": "#5866e9",
    "accent_soft": "#dfe2ff", "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19", "paper2": "#272720", "ink": "#f0eadf",
    "muted": "#a8a196", "line": "#4a4740", "accent": "#99a2ff",
    "accent_soft": "#343957", "green": "#8bc4a9",
}

W, H = 760, 440
STYLE = f"""<style>
.ink{{fill:{LIGHT['ink']}}}.muted{{fill:{LIGHT['muted']}}}
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}.guide{{stroke:{LIGHT['line']};stroke-width:1.5;stroke-dasharray:7 6}}
.sym{{stroke:{LIGHT['ink']};stroke-width:2.5}}.cross{{stroke:{LIGHT['muted']};stroke-width:2.0;stroke-dasharray:8 6}}
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,sans-serif}}
.label{{fill:{LIGHT['ink']};font:17px 'Noto Sans JP',system-ui,sans-serif}}
.math{{fill:{LIGHT['ink']};font:19px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.right{{fill:{LIGHT['accent_soft']};fill-opacity:.72}}.left{{fill:{LIGHT['green']};fill-opacity:.12}}
.mix{{fill:none;stroke:{LIGHT['ink']};stroke-width:1.1;stroke-opacity:.22}}
@media(prefers-color-scheme:dark){{
.ink,.text,.label,.math{{fill:{DARK['ink']}}}.muted,.small{{fill:{DARK['muted']}}}
.axis,.sym{{stroke:{DARK['ink']}}}.guide{{stroke:{DARK['line']}}}.cross{{stroke:{DARK['muted']}}}
.right{{fill:{DARK['accent_soft']};fill-opacity:.62}}.left{{fill:{DARK['green']};fill-opacity:.16}}
.mix{{stroke:{DARK['ink']};stroke-opacity:.20}}
}}
</style>"""

x0, y0, pw, ph = 120, 55, 560, 300
xm, ym = x0 + pw/2, y0 + ph/2
parts = [
    f'<rect class="left" x="{x0}" y="{y0}" width="{pw/2}" height="{ph}" rx="8"/>',
    f'<rect class="right" x="{xm}" y="{y0}" width="{pw/2}" height="{ph}" rx="8"/>',
]

# light hatch away from the symmetry line to signal mixed response without inventing another color
for yy in range(y0 + 18, y0 + ph, 24):
    if abs(yy - ym) < 16:
        continue
    parts.append(f'<line class="mix" x1="{x0+8}" y1="{yy}" x2="{x0+pw-8}" y2="{yy}"/>')

parts += [
    f'<line class="axis" x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}"/>',
    f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}"/>',
    f'<line class="cross" x1="{xm}" y1="{y0}" x2="{xm}" y2="{y0+ph}"/>',
    f'<line class="sym" x1="{x0}" y1="{ym}" x2="{x0+pw}" y2="{ym}"/>',
    f'<text class="label" x="{x0+pw*0.25}" y="{y0+34}" text-anchor="middle">周期4 channel 優勢</text>',
    f'<text class="label" x="{x0+pw*0.75}" y="{y0+34}" text-anchor="middle">一様 channel 優勢</text>',
    f'<text class="small" x="{xm+10}" y="{y0+ph-16}">χ₀₀ = χ_AB,AB</text>',
    f'<text class="small" x="{x0+pw-8}" y="{ym-10}" text-anchor="end">χ₀,AB = 0</text>',
    f'<text class="small" x="{x0+pw-8}" y="{y0+ph-44}" text-anchor="end">上下では mode mixing</text>',
    f'<text class="math" x="{x0+pw/2}" y="{H-28}" text-anchor="middle">J_AB / J̄</text>',
    f'<text class="math" x="32" y="{y0+ph/2}" text-anchor="middle" transform="rotate(-90 32 {y0+ph/2})">δJ / J̄</text>',
    f'<text class="small" x="{x0}" y="{y0+ph+23}" text-anchor="middle">−</text>',
    f'<text class="small" x="{xm}" y="{y0+ph+23}" text-anchor="middle">0</text>',
    f'<text class="small" x="{x0+pw}" y="{y0+ph+23}" text-anchor="middle">+</text>',
    f'<text class="small" x="{x0-16}" y="{y0+8}" text-anchor="end">+</text>',
    f'<text class="small" x="{x0-16}" y="{ym+5}" text-anchor="end">0</text>',
    f'<text class="small" x="{x0-16}" y="{y0+ph}" text-anchor="end">−</text>',
]

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n' + "\n".join(parts) + '\n</svg>\n'
(OUT / "response-structure-map.svg").write_text(svg, encoding="utf-8")
print("generated response-structure-map.svg")
