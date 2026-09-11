"""Generate conceptual SVGs for the finite-range R=N Ising note.

Pure stdlib. The figures follow the site's light/dark-aware SVG palette and are
postprocessed by scripts/postprocess_figures.py before Astro builds.
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-rn"
W, H = 760, 440

LIGHT = {
    "paper": "#f3efe6", "paper2": "#ebe5d9", "ink": "#171714",
    "muted": "#716d64", "line": "#cbc3b5", "accent": "#5866e9",
    "accent_soft": "#dfe2ff", "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19", "paper2": "#272720", "ink": "#f0eadf",
    "muted": "#a8a196", "line": "#4a4740", "accent": "#99a2ff",
    "accent_soft": "#34395f", "green": "#8bc4a9",
}

STYLE = f"""<style>
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,sans-serif}}
.label{{fill:{LIGHT['ink']};font:19px 'Noto Sans JP',system-ui,sans-serif}}
.panel{{fill:{LIGHT['ink']};font:600 17px 'Noto Sans JP',system-ui,sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.var{{font-style:italic}}.roman{{font-style:normal}}
.region{{fill:{LIGHT['paper2']};opacity:.74}}.soft{{fill:{LIGHT['accent_soft']};opacity:.58}}
.node{{fill:{LIGHT['paper']};stroke:{LIGHT['ink']};stroke-width:1.8}}
.accentnode{{fill:{LIGHT['accent']}}}.greennode{{fill:{LIGHT['green']}}}
.inkline{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.4;stroke-linecap:round}}
.mutedline{{fill:none;stroke:{LIGHT['line']};stroke-width:1.8;stroke-linecap:round}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.2;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.dashed{{stroke-dasharray:10 7}}
.arrow-primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:3.4;stroke-linecap:round;marker-end:url(#arrow-accent)}}
.caption-box{{fill:{LIGHT['paper']};fill-opacity:.94;stroke:{LIGHT['line']};stroke-width:1}}
@media(prefers-color-scheme:dark){{
.text,.label,.panel,.math{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
.region{{fill:{DARK['paper2']}}}.soft{{fill:{DARK['accent_soft']}}}
.node{{fill:{DARK['paper']};stroke:{DARK['ink']}}}.accentnode{{fill:{DARK['accent']}}}.greennode{{fill:{DARK['green']}}}
.inkline{{stroke:{DARK['ink']}}}.mutedline{{stroke:{DARK['line']}}}
.primary,.arrow-primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}
.caption-box{{fill:{DARK['paper']};stroke:{DARK['line']}}}
}}
</style>"""

DEFS = f"""<defs>
<marker id="arrow-accent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{LIGHT['accent']}"/></marker>
</defs>"""


def wrap(body: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{DEFS}\n{body}\n</svg>\n'


def save(name: str, parts: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts)), encoding="utf-8")


def box(parts: list[str], x: float, y: float, w: float, text: str, cls: str = "small", h: float = 30) -> None:
    parts.append(f'<rect class="caption-box" x="{x-w/2:.1f}" y="{y-h+7:.1f}" width="{w}" height="{h}" rx="8"/>')
    parts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="middle">{text}</text>')


def range_memory_map() -> None:
    p: list[str] = []
    p.append('<text class="panel" x="380" y="38" text-anchor="middle">相互作用範囲を伸ばすと、壁相互作用の次数と記憶長が同時に増える</text>')

    cols = [(120, "R = 1"), (380, "R = 2"), (640, "R = N")]
    for x, title in cols:
        p.append(f'<rect class="region" x="{x-105}" y="64" width="210" height="300" rx="18"/>')
        p.append(f'<text class="panel" x="{x}" y="94" text-anchor="middle">{title}</text>')

    # R=1
    p.append('<text class="label" x="120" y="145" text-anchor="middle">壁は独立</text>')
    for j, x in enumerate((78, 120, 162)):
        cls = "accentnode" if j == 1 else "node"
        p.append(f'<circle class="{cls}" cx="{x}" cy="190" r="10"/>')
    box(p, 120, 245, 156, "1体項 τᵢ", cls="math")
    box(p, 120, 307, 156, "0-step memory")

    # R=2
    p.append('<text class="label" x="380" y="145" text-anchor="middle">壁ペアが結合</text>')
    p.append('<circle class="accentnode" cx="350" cy="190" r="10"/>')
    p.append('<circle class="accentnode" cx="410" cy="190" r="10"/>')
    p.append('<line class="secondary" x1="362" y1="190" x2="398" y2="190"/>')
    box(p, 380, 245, 170, "2体項 τᵢτᵢ₊₁", cls="math")
    box(p, 380, 307, 156, "1-step memory")

    # R=N
    xs = [590, 615, 640, 665, 690]
    for x in xs:
        p.append(f'<circle class="accentnode" cx="{x}" cy="190" r="8"/>')
    p.append('<path class="secondary" d="M 582 190 C 610 148, 670 148, 698 190"/>')
    p.append('<text class="label" x="640" y="145" text-anchor="middle">局所パターンが結合</text>')
    box(p, 640, 245, 178, "最大 N 体項", cls="math")
    box(p, 640, 307, 178, "(N−1)-step memory")

    p.append('<path class="arrow-primary" d="M 228 214 L 272 214"/>')
    p.append('<path class="arrow-primary" d="M 488 214 L 532 214"/>')
    box(p, 380, 408, 560, "spin range N  ↔  wall の最大 N 体相互作用  ↔  有限記憶 N−1", cls="label", h=34)
    save("range-memory-map.svg", p)


def r3_wall_interaction() -> None:
    p: list[str] = []
    p.append('<text class="panel" x="380" y="38" text-anchor="middle">R = 3：J₃ は3つ並んだ壁変数のパターンに直接エネルギーを与える</text>')

    # Three tau variables
    xs = [250, 380, 510]
    vals = ["τᵢ", "τᵢ₊₁", "τᵢ₊₂"]
    for x, lab in zip(xs, vals):
        p.append(f'<circle class="node" cx="{x}" cy="176" r="28"/>')
        p.append(f'<text class="math" x="{x}" y="183" text-anchor="middle">{lab}</text>')
    p.append('<line class="mutedline" x1="278" y1="176" x2="352" y2="176"/>')
    p.append('<line class="mutedline" x1="408" y1="176" x2="482" y2="176"/>')

    # Pair interaction bracket
    p.append('<path class="secondary" d="M 250 230 C 290 272, 340 272, 380 230"/>')
    box(p, 315, 294, 190, "J₂：2体の壁相互作用", h=32)

    # Three-body interaction arc
    p.append('<path class="primary" d="M 250 120 C 315 54, 445 54, 510 120"/>')
    box(p, 380, 92, 240, "J₃：3体の壁相互作用", h=32)

    p.append('<text class="math" x="380" y="350" text-anchor="middle">−J₃ τᵢ τᵢ₊₁ τᵢ₊₂</text>')
    box(p, 380, 405, 520, "R = 2 では壁ペア、R = 3 では壁3個の局所パターンまで区別される", cls="label", h=34)
    save("r3-wall-interaction.svg", p)


def main() -> None:
    range_memory_map()
    r3_wall_interaction()
    print("generated R=N Ising conceptual figures")


if __name__ == "__main__":
    main()
