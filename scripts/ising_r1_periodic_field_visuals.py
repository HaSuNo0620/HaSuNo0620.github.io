"""Generate SVG figures for the periodic R=1 Ising + periodic-field note.

Pure stdlib. Figures follow docs/figure-style.md and docs/diagram-style.md.
"""
from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r1-periodic-field"
W, H = 760, 440

LIGHT = {
    "paper": "#f3efe6", "paper2": "#ebe5d9", "ink": "#171714", "muted": "#716d64",
    "line": "#cbc3b5", "accent": "#5866e9", "accent_soft": "#dfe2ff", "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19", "paper2": "#272720", "ink": "#f0eadf", "muted": "#a8a196",
    "line": "#4a4740", "accent": "#99a2ff", "accent_soft": "#343957", "green": "#8bc4a9",
}

STYLE = f"""<style>
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,sans-serif}}
.label{{fill:{LIGHT['ink']};font:20px 'Noto Sans JP',system-ui,sans-serif}}
.panel{{fill:{LIGHT['ink']};font:600 17px 'Noto Sans JP',system-ui,sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.node{{fill:{LIGHT['paper']};stroke:{LIGHT['ink']};stroke-width:1.8}}
.node2{{fill:{LIGHT['paper2']};stroke:{LIGHT['ink']};stroke-width:1.6}}
.soft{{fill:{LIGHT['accent_soft']};opacity:.7}}
.region{{fill:{LIGHT['paper2']};opacity:.78}}
.inkline{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.5;stroke-linecap:round}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.mutedline{{fill:none;stroke:{LIGHT['line']};stroke-width:1.8;stroke-linecap:round}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1;opacity:.4}}
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}
.accentfill{{fill:{LIGHT['accent']}}}.greenfill{{fill:{LIGHT['green']}}}.inkfill{{fill:{LIGHT['ink']}}}
.caption{{fill:{LIGHT['paper']};fill-opacity:.92;stroke:{LIGHT['line']};stroke-width:1}}
@media(prefers-color-scheme:dark){{
.text,.label,.panel,.math{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
.node{{fill:{DARK['paper']};stroke:{DARK['ink']}}}.node2{{fill:{DARK['paper2']};stroke:{DARK['ink']}}}
.soft{{fill:{DARK['accent_soft']}}}.region{{fill:{DARK['paper2']}}}
.inkline,.axis{{stroke:{DARK['ink']}}}.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}
.mutedline,.grid{{stroke:{DARK['line']}}}.accentfill{{fill:{DARK['accent']}}}.greenfill{{fill:{DARK['green']}}}.inkfill{{fill:{DARK['ink']}}}
.caption{{fill:{DARK['paper']};stroke:{DARK['line']}}}
}}
</style>"""


def wrap(body: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{body}\n</svg>\n'


def save(name: str, parts: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts)), encoding="utf-8")


def box(parts, x, y, w, h, text, cls="region"):
    parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="18"/>')
    parts.append(f'<text class="label" x="{x+w/2}" y="{y+h/2+7}" text-anchor="middle">{text}</text>')


def spin_row(parts, x0, y, labels, fields=None, spacing=82):
    xs=[x0+i*spacing for i in range(len(labels))]
    for a,b in zip(xs[:-1],xs[1:]):
        parts.append(f'<line class="inkline" x1="{a+15}" y1="{y}" x2="{b-15}" y2="{y}"/>')
    for x,lbl in zip(xs,labels):
        parts.append(f'<circle class="node" cx="{x}" cy="{y}" r="15"/>')
        parts.append(f'<text class="text" x="{x}" y="{y+6}" text-anchor="middle">{lbl}</text>')
    if fields:
        for x,f in zip(xs,fields):
            direction=-1 if f>0 else 1
            cls='primary' if f>0 else 'secondary'
            y1=y-55*direction; y2=y-23*direction
            parts.append(f'<line class="{cls}" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}"/>')
            parts.append(f'<polygon class="{"accentfill" if f>0 else "greenfill"}" points="{x-6},{y2+(-2 if f>0 else 2)} {x+6},{y2+(-2 if f>0 else 2)} {x},{y2+(8 if f>0 else -8)}"/>')
    return xs


def overview():
    p=[]
    p.append('<text class="panel" x="36" y="38">periodic bond</text>')
    labels=['A','A','B','B','A','A','B','B']
    xs=spin_row(p,72,145,labels,spacing=88)
    for i in range(len(xs)-1):
        mid=(xs[i]+xs[i+1])/2
        txt='J' if labels[i]==labels[i+1] else 'K'
        p.append(f'<text class="small" x="{mid}" y="118" text-anchor="middle">{txt}</text>')
    p.append('<text class="panel" x="36" y="245">periodic field</text>')
    spin_row(p,72,332,labels,[1,1,-1,-1,1,1,-1,-1],spacing=88)
    p.append('<text class="small" x="380" y="410" text-anchor="middle">bond と field の単位胞が同じ空間に重なる</text>')
    save('overview-periodic-field.svg',p)


def noncommuting():
    p=[]
    box(p,42,90,250,110,'h = 0')
    box(p,468,90,250,110,'hᵢ ≠ 0')
    p.append('<text class="math" x="167" y="250" text-anchor="middle">Tᵢ = aᵢ I + bᵢ σₓ</text>')
    p.append('<text class="math" x="593" y="250" text-anchor="middle">Tᵢ = aᵢ I + bᵢ σₓ + cᵢ σ_z + …</text>')
    p.append('<text class="math" x="167" y="322" text-anchor="middle">[Tᵢ,Tⱼ] = 0</text>')
    p.append('<text class="math" x="593" y="322" text-anchor="middle">[Tᵢ,Tⱼ] ≠ 0</text>')
    p.append('<path class="primary" d="M 304 145 L 452 145"/>')
    p.append('<polygon class="accentfill" points="452,145 438,137 438,153"/>')
    p.append('<text class="small" x="380" y="126" text-anchor="middle">周期外場を加える</text>')
    save('noncommuting-transfer.svg',p)


def fourier():
    p=[]
    box(p,32,72,205,90,'(1,1,1,1)')
    box(p,278,72,205,90,'(1,1,−1,−1)')
    box(p,524,72,205,90,'一般周期外場')
    p.append('<text class="math" x="134" y="220" text-anchor="middle">G = 0</text>')
    p.append('<text class="math" x="380" y="220" text-anchor="middle">G = ±π/2</text>')
    p.append('<text class="math" x="626" y="220" text-anchor="middle">Gₙ = 2πn/p</text>')
    for x in (134,380,626):
        p.append(f'<line class="primary" x1="{x}" y1="250" x2="{x}" y2="300"/>')
        p.append(f'<polygon class="accentfill" points="{x},312 {x-7},298 {x+7},298"/>')
    p.append('<text class="label" x="134" y="355" text-anchor="middle">一様磁化</text>')
    p.append('<text class="label" x="380" y="355" text-anchor="middle">周期4磁化</text>')
    p.append('<text class="label" x="626" y="355" text-anchor="middle">各構造モード</text>')
    save('field-fourier-coupling.svg',p)


def aabb_modes():
    p=[]
    labels=['A','A','B','B','A','A','B','B']
    p.append('<text class="panel" x="32" y="42">(a) h₀ : 一様 channel</text>')
    spin_row(p,72,130,labels,[1]*8,spacing=88)
    p.append('<text class="panel" x="32" y="250">(b) h_AB : 周期4 channel</text>')
    spin_row(p,72,338,labels,[1,1,-1,-1,1,1,-1,-1],spacing=88)
    save('aabb-field-modes.svg',p)


def chi00(beta,J,K):
    j=beta*J; k=beta*K
    return beta*math.exp(j+k)/math.cosh(j-k)


def chiab(beta,J,K):
    j=beta*J; k=beta*K
    return beta*math.exp(j-k)/math.cosh(j+k)


def plot_path(vals, xmin,xmax,ymin,ymax,left,top,width,height):
    pts=[]
    for x,y in vals:
        px=left+(x-xmin)/(xmax-xmin)*width
        py=top+height-(y-ymin)/(ymax-ymin)*height
        pts.append((px,py))
    return 'M '+' L '.join(f'{x:.1f} {y:.1f}' for x,y in pts)


def susceptibility():
    p=[]
    left,top,width,height=86,42,610,320
    for frac in (0,.25,.5,.75,1):
        y=top+height*frac
        p.append(f'<line class="grid" x1="{left}" y1="{y}" x2="{left+width}" y2="{y}"/>')
    p.append(f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{top+height}"/>')
    p.append(f'<line class="axis" x1="{left}" y1="{top+height}" x2="{left+width}" y2="{top+height}"/>')
    Ts=[0.55+i*(3.0-0.55)/150 for i in range(151)]
    for K,cls,label,dy in [(-1.0,'primary','χ_AB,AB   (K = −J)',-8),(1.0,'secondary','χ_00   (K = +J)',18)]:
        vals=[]
        for T in Ts:
            beta=1/T
            y=chiab(beta,1,K) if K<0 else chi00(beta,1,K)
            vals.append((T,min(y,12)))
        p.append(f'<path class="{cls}" d="{plot_path(vals,.55,3,0,12,left,top,width,height)}"/>')
        x=565; T=2.45; beta=1/T; y=chiab(beta,1,K) if K<0 else chi00(beta,1,K)
        py=top+height-(min(y,12)/12)*height
        p.append(f'<rect class="caption" x="{x-95}" y="{py+dy-20}" width="190" height="28" rx="7"/>')
        p.append(f'<text class="small" x="{x}" y="{py+dy}" text-anchor="middle">{label}</text>')
    p.append('<text class="label" x="390" y="415" text-anchor="middle">k_B T / J</text>')
    p.append('<text class="label" x="24" y="210" transform="rotate(-90 24 210)" text-anchor="middle">χ J</text>')
    p.append('<text class="small" x="690" y="390" text-anchor="end">上端は χJ = 12 で表示を打ち切り</text>')
    save('susceptibility-channels.svg',p)


def comparison():
    p=[]
    box(p,30,76,305,248,'periodic R = 1')
    box(p,425,76,305,248,'uniform R = 2')
    p.append('<text class="small" x="182" y="160" text-anchor="middle">structure-imposed basis</text>')
    p.append('<text class="math" x="182" y="205" text-anchor="middle">Gₙ = 2πn/p</text>')
    p.append('<text class="small" x="182" y="260" text-anchor="middle">外場が channel を選択</text>')
    p.append('<text class="small" x="578" y="160" text-anchor="middle">interaction-selected wavelength</text>')
    p.append('<text class="math" x="578" y="205" text-anchor="middle">J(q) = J₁ cos q + J₂ cos 2q</text>')
    p.append('<text class="small" x="578" y="260" text-anchor="middle">相互作用競合が q を選択</text>')
    p.append('<path class="primary" d="M 342 200 L 418 200"/>')
    p.append('<polygon class="accentfill" points="418,200 404,192 404,208"/>')
    p.append('<text class="small" x="380" y="184" text-anchor="middle">対比</text>')
    save('periodic-r1-vs-r2-field.svg',p)


def main():
    overview(); noncommuting(); fourier(); aabb_modes(); susceptibility(); comparison()

if __name__ == '__main__':
    main()
