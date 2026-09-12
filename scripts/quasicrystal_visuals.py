"""Generate SVG figures for the quasicrystal note series.

Pure stdlib. Figures follow docs/figure-style.md and docs/diagram-style.md.
"""
from __future__ import annotations

import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "quasicrystals"

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
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.mutedline{{fill:none;stroke:{LIGHT['muted']};stroke-width:3.0;stroke-linecap:round;stroke-linejoin:round}}
.guide{{fill:none;stroke:{LIGHT['line']};stroke-width:1.5;stroke-linecap:round}}
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1;opacity:.45}}
.accentfill{{fill:{LIGHT['accent']}}}.greenfill{{fill:{LIGHT['green']}}}.mutedfill{{fill:{LIGHT['muted']}}}.linefill{{fill:{LIGHT['line']}}}
.paperbox{{fill:{LIGHT['paper']};fill-opacity:.92;stroke:{LIGHT['line']};stroke-width:1}}
@media(prefers-color-scheme:dark){{
.text,.label,.panel,.math{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}.mutedline{{stroke:{DARK['muted']}}}
.guide,.grid{{stroke:{DARK['line']}}}.axis{{stroke:{DARK['ink']}}}
.accentfill{{fill:{DARK['accent']}}}.greenfill{{fill:{DARK['green']}}}.mutedfill{{fill:{DARK['muted']}}}.linefill{{fill:{DARK['line']}}}
.paperbox{{fill:{DARK['paper']};stroke:{DARK['line']}}}
}}
</style>"""


def wrap(body: str, h: int = 440) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{h}" viewBox="0 0 760 {h}">\n{STYLE}\n{body}\n</svg>\n'


def save(name: str, parts: list[str], h: int = 440) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts), h), encoding="utf-8")


def order_comparison() -> None:
    p: list[str] = []
    rows = [(90, "周期", "AB" * 9, "accent"),
            (220, "Fibonacci", "LSLLSLSLLSLLSLSLLS", "green"),
            (350, "ランダム", "LSSLLSLSLLLSSLSLSL", "muted")]
    x0, step = 210, 28
    for y, name, seq, role in rows:
        p.append(f'<text class="label" x="28" y="{y+7}">{name}</text>')
        for i, ch in enumerate(seq[:18]):
            x = x0 + i * step
            cls = {"accent":"accentfill","green":"greenfill","muted":"mutedfill"}[role]
            fill = cls if ch in ("A", "L") else "none"
            stroke = {"accent":LIGHT['accent'],"green":LIGHT['green'],"muted":LIGHT['muted']}[role]
            darkstroke = {"accent":DARK['accent'],"green":DARK['green'],"muted":DARK['muted']}[role]
            p.append(f'<rect class="{fill}" x="{x}" y="{y-18}" width="20" height="36" rx="2" style="stroke:{stroke};stroke-width:2"/>')
        if name == "周期":
            p.append('<line class="primary" x1="210" y1="42" x2="322" y2="42"/>')
            p.append('<polygon class="accentfill" points="210,42 224,34 224,50"/>')
            p.append('<polygon class="accentfill" points="322,42 308,34 308,50"/>')
            p.append('<text class="small" x="266" y="28" text-anchor="middle">同じ単位が反復</text>')
        elif name == "Fibonacci":
            p.append('<text class="small" x="466" y="177" text-anchor="middle">反復周期はないが生成規則はある</text>')
        else:
            p.append('<text class="small" x="466" y="307" text-anchor="middle">配置そのものは生成則で固定されない</text>')
    save("order-comparison.svg", p)


def quasiperiodic_signal_phase() -> None:
    p: list[str] = []
    # top signal panel
    x0, y0, w, h = 70, 40, 640, 170
    p.append(f'<line class="axis" x1="{x0}" y1="{y0+h/2}" x2="{x0+w}" y2="{y0+h/2}"/>')
    p.append(f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}"/>')
    def path(alpha: float, cls: str, scale: float = 42.0):
        pts=[]
        n=700
        for i in range(n):
            xx=8*math.pi*i/(n-1)
            yy=math.cos(xx)+0.55*math.cos(alpha*xx)
            sx=x0+w*i/(n-1)
            sy=y0+h/2-scale*yy
            pts.append((sx,sy))
        d="M "+" L ".join(f"{a:.2f},{b:.2f}" for a,b in pts)
        p.append(f'<path class="{cls}" d="{d}"/>')
    path(2.0, "mutedline", 43)
    path(math.sqrt(2), "primary", 43)
    p.append('<rect class="paperbox" x="444" y="54" width="246" height="64" rx="10"/>')
    p.append('<line class="mutedline" x1="462" y1="77" x2="505" y2="77"/><text class="small" x="518" y="82">periodic 1:2</text>')
    p.append('<line class="primary" x1="462" y1="101" x2="505" y2="101"/><text class="small" x="518" y="106">quasiperiodic 1:√2</text>')
    p.append('<text class="math" x="390" y="229" text-anchor="middle">x / π</text>')
    # phase squares
    for left, alpha, title, cls in [(100,2.0,"有理比：閉じる","mutedline"),(430,math.sqrt(2),"無理数比：閉じない","primary")]:
        top=275; size=190
        p.append(f'<rect x="{left}" y="{top}" width="{size}" height="{size}" fill="none" class="guide"/>')
        p.append(f'<text class="panel" x="{left+size/2}" y="255" text-anchor="middle">{title}</text>')
        pts=[]
        n=500
        for i in range(n):
            t=20*math.pi*i/(n-1)
            a=(t%(2*math.pi))/(2*math.pi)
            b=((alpha*t)%(2*math.pi))/(2*math.pi)
            sx=left+a*size; sy=top+(1-b)*size
            pts.append((sx,sy))
        d="M "+" L ".join(f"{a:.2f},{b:.2f}" for a,b in pts)
        p.append(f'<path class="{cls}" d="{d}"/>')
        p.append(f'<text class="math" x="{left+size/2}" y="490" text-anchor="middle">θ₁ / 2π</text>')
    save("quasiperiodic-signal-phase.svg", p, 510)


def cut_and_project() -> None:
    p: list[str] = []
    tau=(1+math.sqrt(5))/2
    norm=math.sqrt(1+tau*tau)
    ux,uy=1/norm,tau/norm
    vx,vy=-uy,ux
    cx,cy=390,250
    scale=48
    # lattice
    pts=[]
    for i in range(-6,7):
        for j in range(-5,6):
            x=cx+scale*i; y=cy-scale*j
            pts.append((i,j,x,y))
            p.append(f'<circle class="linefill" cx="{x}" cy="{y}" r="5"/>')
    strip=0.62
    # strip edges
    for s in (-strip,strip):
        x1=cx+scale*(-7*ux+s*vx); y1=cy-scale*(-7*uy+s*vy)
        x2=cx+scale*(7*ux+s*vx); y2=cy-scale*(7*uy+s*vy)
        p.append(f'<line class="secondary" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-dasharray="10 8"/>')
    # physical axis
    x1=cx+scale*(-7*ux); y1=cy-scale*(-7*uy)
    x2=cx+scale*(7*ux); y2=cy-scale*(7*uy)
    p.append(f'<line class="axis" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    # selected and projected
    for i,j,x,y in pts:
        par=i*ux+j*uy
        perp=i*vx+j*vy
        if abs(perp)<strip:
            p.append(f'<circle class="accentfill" cx="{x}" cy="{y}" r="8"/>')
            qx=cx+scale*par*ux; qy=cy-scale*par*uy
            p.append(f'<line class="guide" x1="{x}" y1="{y}" x2="{qx:.1f}" y2="{qy:.1f}"/>')
            p.append(f'<circle class="greenfill" cx="{qx:.1f}" cy="{qy:.1f}" r="6"/>')
    p.append('<text class="math" x="520" y="118">E∥</text>')
    p.append('<text class="math" x="284" y="238">E⊥</text>')
    p.append('<text class="label" x="36" y="54">window 内の格子点だけを採用する</text>')
    p.append('<path class="primary" d="M 278 72 L 350 180"/>')
    p.append('<polygon class="accentfill" points="350,180 338,170 337,186"/>')
    save("cut-and-project.svg", p, 500)


def diffraction_fourier_module() -> None:
    p: list[str] = []
    panels=[(55,"周期格子：rank 1"),(405,"準周期：rank 2")]
    for left,title in panels:
        p.append(f'<text class="panel" x="{left+145}" y="34" text-anchor="middle">{title}</text>')
        p.append(f'<line class="axis" x1="{left}" y1="365" x2="{left+290}" y2="365"/>')
        p.append(f'<line class="axis" x1="{left}" y1="70" x2="{left}" y2="365"/>')
    # periodic peaks
    for m in range(-5,6):
        x=200+26*m
        amp=math.exp(-0.055*m*m)
        y=365-260*amp
        p.append(f'<line class="primary" x1="{x}" y1="365" x2="{x}" y2="{y:.1f}"/>')
        p.append(f'<circle class="accentfill" cx="{x}" cy="{y:.1f}" r="5"/>')
    # quasi peaks
    tau=(1+math.sqrt(5))/2
    vals=[]
    for m in range(-8,9):
        for n in range(-8,9):
            if m==0 and n==0: continue
            k=m+n/tau
            kp=-m/tau+n
            amp=(math.sin(math.pi*0.36*kp)/(math.pi*0.36*kp) if abs(kp)>1e-9 else 1.0)**2
            amp*=math.exp(-0.006*(m*m+n*n))
            if -5.2<k<5.2 and amp>0.012:
                vals.append((k,amp))
    for k,amp in vals:
        x=550+27*k
        y=365-255*min(amp,1)
        width=1.2+2.5*min(amp,1)
        p.append(f'<line x1="{x:.1f}" y1="365" x2="{x:.1f}" y2="{y:.1f}" style="stroke:{LIGHT["green"]};stroke-width:{width:.1f}"/>')
    p.append('<rect class="paperbox" x="430" y="78" width="274" height="62" rx="10"/>')
    p.append('<text class="small" x="446" y="102">強い peak は疎</text>')
    p.append('<text class="small" x="446" y="126">弱い peak まで含めると高密度</text>')
    p.append('<text class="math" x="200" y="405" text-anchor="middle">k / k₀</text>')
    p.append('<text class="math" x="550" y="405" text-anchor="middle">k / k₀</text>')
    save("diffraction-fourier-module.svg", p)


def main() -> None:
    order_comparison()
    quasiperiodic_signal_phase()
    cut_and_project()
    diffraction_fourier_module()


if __name__ == "__main__":
    main()
