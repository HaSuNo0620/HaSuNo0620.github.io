"""Generate SVG figures for the periodic inhomogeneous R=1 Ising note.

Pure stdlib so the figures can be regenerated in GitHub Actions.
The palette and typography follow docs/figure-style.md and docs/diagram-style.md.
"""
from __future__ import annotations

import html
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r1-periodic"
W, H = 760, 440

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

STYLE = f"""<style>
.paper{{fill:{LIGHT['paper']}}}.paper2{{fill:{LIGHT['paper2']}}}.soft{{fill:{LIGHT['accent_soft']}}}
.inkfill{{fill:{LIGHT['ink']}}}.greenfill{{fill:{LIGHT['green']}}}.accentfill{{fill:{LIGHT['accent']}}}
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}.grid{{stroke:{LIGHT['line']};stroke-width:1.1;opacity:.42}}
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.label{{fill:{LIGHT['ink']};font:19px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.panel{{fill:{LIGHT['ink']};font:600 17px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.inkline{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}}
.mutedline{{fill:none;stroke:{LIGHT['muted']};stroke-width:2.0;stroke-linecap:round;stroke-linejoin:round}}
.dashed{{stroke-dasharray:10 7}}.dotted{{stroke-dasharray:2 6}}
.node{{fill:{LIGHT['paper']};stroke:{LIGHT['ink']};stroke-width:1.8}}
.node-a{{fill:{LIGHT['accent_soft']};stroke:{LIGHT['accent']};stroke-width:2.0}}
.node-b{{fill:{LIGHT['paper2']};stroke:{LIGHT['green']};stroke-width:2.0}}
.box{{fill:{LIGHT['paper2']};fill-opacity:.70;stroke:{LIGHT['line']};stroke-width:1.2}}
.caption-box{{fill:{LIGHT['paper']};fill-opacity:.92;stroke:{LIGHT['line']};stroke-width:1}}
@media(prefers-color-scheme:dark){{
.paper{{fill:{DARK['paper']}}}.paper2{{fill:{DARK['paper2']}}}.soft{{fill:{DARK['accent_soft']}}}
.inkfill{{fill:{DARK['ink']}}}.greenfill{{fill:{DARK['green']}}}.accentfill{{fill:{DARK['accent']}}}
.axis,.inkline{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.mutedline{{stroke:{DARK['muted']}}}
.text,.label,.panel,.math{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}
.node{{fill:{DARK['paper']};stroke:{DARK['ink']}}}.node-a{{fill:{DARK['accent_soft']};stroke:{DARK['accent']}}}.node-b{{fill:{DARK['paper2']};stroke:{DARK['green']}}}
.box{{fill:{DARK['paper2']};stroke:{DARK['line']}}}.caption-box{{fill:{DARK['paper']};stroke:{DARK['line']}}}
}}
</style>"""


def wrap(body: str, height: int = H) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">\n{STYLE}\n{body}\n</svg>\n'


def save(name: str, parts: list[str], height: int = H) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts), height), encoding="utf-8")


def txt(x, y, s, cls="text", anchor="middle"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{html.escape(s)}</text>'


def text_box(parts, x, y, width, s, *, cls="small", height=30):
    parts.append(f'<rect class="caption-box" x="{x-width/2:.1f}" y="{y-height+7:.1f}" width="{width}" height="{height}" rx="8"/>')
    parts.append(txt(x, y, s, cls))


def chain(parts, x0, y, labels, spacing=76, bond_classes=None, node_classes=None):
    xs = [x0 + i * spacing for i in range(len(labels))]
    for i in range(len(labels) - 1):
        cls = "inkline" if bond_classes is None else bond_classes[i]
        parts.append(f'<line class="{cls}" x1="{xs[i]+17}" y1="{y}" x2="{xs[i+1]-17}" y2="{y}"/>')
    for i, (x, label) in enumerate(zip(xs, labels)):
        cls = "node" if node_classes is None else node_classes[i]
        parts.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="17"/>')
        parts.append(txt(x, y+6, label, "text"))
    return xs


def overview_uniform_periodic():
    p=[]
    p += [txt(42,38,"(a) 一様 R = 1","panel","start"), txt(402,38,"(b) 周期的不均一 R = 1","panel","start")]
    p += ['<rect class="box" x="24" y="58" width="330" height="302" rx="20"/>', '<rect class="box" x="390" y="58" width="346" height="302" rx="20"/>']
    xs=chain(p,54,145,["+","+","−","−","+"],61,["primary"]*4)
    for i in range(4): p.append(txt((xs[i]+xs[i+1])/2,108,"J","math"))
    text_box(p,189,236,238,"全 bond が同じ重み")
    p.append(txt(189,304,"並進周期 1","label"))

    bclasses=["primary","secondary","primary","secondary"]
    xs=chain(p,420,145,["+","+","−","−","+"],66,bclasses)
    labs=["J₁","J₂","J₃","J₄"]
    for i,l in enumerate(labs): p.append(txt((xs[i]+xs[i+1])/2,108,l,"math"))
    text_box(p,563,236,270,"bond の重みが周期 p で反復")
    p.append(txt(563,304,"単位胞 p が新しい空間尺度","label"))
    save("overview-uniform-periodic.svg",p)


def domain_wall_periodic():
    p=[]
    p.append(txt(44,42,"同じドメイン壁でも置く bond によってコストが違う","panel","start"))
    labels=["+","+","−","−","+","+"]
    bclasses=["primary","secondary","primary","secondary","primary"]
    xs=chain(p,96,138,labels,112,bclasses)
    js=["J₁","J₂","J₃","J₄","J₁"]
    for i,l in enumerate(js): p.append(txt((xs[i]+xs[i+1])/2,100,l,"math"))
    # wall candidates at bond 2 and 4
    for idx,label in [(1,"ΔE = 2J₂"),(3,"ΔE = 2J₄")]:
        xm=(xs[idx]+xs[idx+1])/2
        p.append(f'<line class="primary" x1="{xm}" y1="166" x2="{xm}" y2="226"/>')
        p.append(txt(xm,257,label,"math"))
    p.append('<path class="mutedline dashed" d="M 82 314 L 678 314"/>')
    p.append(txt(380,352,"壁同士の相互作用はない：H = −Σ Jᵢ τᵢ","label"))
    p.append(txt(380,390,"independent, but nonidentical","small"))
    save("domain-wall-periodic.svg",p)


def correlation_envelope_modulation():
    p=[]
    left,right,top,bottom=72,724,42,378
    x0,y0=left,bottom
    p += [f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>', f'<line class="axis" x1="{left}" y1="{bottom}" x2="{left}" y2="{top}"/>']
    p.append(txt(398,424,"r","math")); p.append(txt(25,215,"C(r)","math"))
    for frac in [0.25,0.5,0.75]:
        yy=bottom-(bottom-top)*frac
        p.append(f'<line class="grid" x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}"/>')
    # Example p=4, positive coefficients chosen only to illustrate exact product structure.
    ts=[0.88,0.52,0.76,0.52]
    q=math.prod(ts); xi=-4/math.log(q)
    vals=[]
    prod=1.0
    for r in range(33):
        if r==0: c=1.0
        else:
            prod*=ts[(r-1)%4]; c=prod
        vals.append(c)
    def xy(r,c):
        return left+(right-left)*r/32, bottom-(bottom-top)*c
    points=" ".join(f"{xy(r,c)[0]:.1f},{xy(r,c)[1]:.1f}" for r,c in enumerate(vals))
    p.append(f'<polyline class="primary" points="{points}"/>')
    for r,c in enumerate(vals):
        x,y=xy(r,c); p.append(f'<circle class="accentfill" cx="{x:.1f}" cy="{y:.1f}" r="4.5"/>')
    env=[]
    for n in range(161):
        r=32*n/160; c=math.exp(-r/xi); x,y=xy(r,c); env.append(f"{x:.1f},{y:.1f}")
    p.append(f'<polyline class="secondary dashed" points="{" ".join(env)}"/>')
    text_box(p,570,88,245,"指数包絡  exp(−r / ξ)")
    text_box(p,500,196,255,"単位胞内で振幅が周期変調")
    save("correlation-envelope-modulation.svg",p)


def aabb_bond_pattern():
    p=[]
    p.append(txt(42,42,"4サイト単位胞","panel","start"))
    labels=["A","A","B","B","A","A","B","B"]
    nodes=["node-a","node-a","node-b","node-b","node-a","node-a","node-b","node-b"]
    bclasses=["primary","secondary","secondary","secondary","primary","secondary","secondary"]
    xs=chain(p,70,170,labels,88,bclasses,nodes)
    bonds=["JAA","JAB","JBB","JAB","JAA","JAB","JBB"]
    for i,l in enumerate(bonds):
        p.append(txt((xs[i]+xs[i+1])/2,126,l,"math"))
    p.append('<path class="mutedline dashed" d="M 48 238 L 392 238"/>')
    p.append('<path class="mutedline dashed" d="M 400 238 L 744 238"/>')
    p.append(txt(220,274,"unit cell 1","small")); p.append(txt(572,274,"unit cell 2","small"))
    p.append(txt(380,342,"JAA = JBB > 0,  JAB < 0 なら低温で  ++−−  が反復","label"))
    p.append(txt(380,385,"基本波数  k₀ = π / 2","math"))
    save("aabb-bond-pattern.svg",p)


def _kstar(T: float, ratio: float) -> float:
    b=1.0/T
    t=math.tanh(b)
    v=math.tanh(ratio*b)
    if t <= 0 or v <= 0:
        return 0.0
    x=((1-t*v)*(math.sqrt(t)-math.sqrt(v)))/(2*math.sqrt(t*v)*(math.sqrt(t)+math.sqrt(v)))
    x=max(-1.0,min(1.0,x))
    return math.acos(x)


def kstar_temperature():
    p=[]
    left,right,top,bottom=80,716,42,372
    p += [f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>', f'<line class="axis" x1="{left}" y1="{bottom}" x2="{left}" y2="{top}"/>']
    p.append(txt(400,420,"kBT / J","math")); p.append(txt(30,210,"k★ / π","math"))
    for yv in [0,.25,.5,.75,1.0]:
        yy=bottom-(bottom-top)*yv
        p.append(f'<line class="grid" x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}"/>')
        p.append(txt(left-14,yy+5,f"{yv:g}","small","end"))
    # log T from 0.12 to 30, direct labels at right
    Tmin,Tmax=0.12,30.0
    logmin,logmax=math.log(Tmin),math.log(Tmax)
    def X(T): return left+(right-left)*(math.log(T)-logmin)/(logmax-logmin)
    def Y(k): return bottom-(bottom-top)*(k/math.pi)
    curves=[(0.5,"primary","|K| / J = 0.5"),(1.0,"secondary","|K| / J = 1"),(2.0,"mutedline dashed","|K| / J = 2")]
    for ratio,cls,label in curves:
        pts=[]
        for n in range(220):
            T=math.exp(logmin+(logmax-logmin)*n/219)
            pts.append(f"{X(T):.1f},{Y(_kstar(T,ratio)):.1f}")
        p.append(f'<polyline class="{cls}" points="{" ".join(pts)}"/>')
        Tlab=12.0; p.append(txt(X(Tlab)+8,Y(_kstar(Tlab,ratio))-8,label,"small","start"))
    for T,lbl in [(0.2,"0.2"),(1,"1"),(5,"5"),(20,"20")]:
        x=X(T); p.append(f'<line class="axis" x1="{x:.1f}" y1="{bottom}" x2="{x:.1f}" y2="{bottom+6}"/>'); p.append(txt(x,bottom+28,lbl,"small"))
    save("kstar-temperature.svg",p)


def periodic_vs_r2():
    p=[]
    p += [txt(40,40,"(a) 周期的不均一 R = 1","panel","start"), txt(402,40,"(b) 一様 R = 2","panel","start")]
    p += ['<rect class="box" x="24" y="58" width="332" height="322" rx="20"/>', '<rect class="box" x="390" y="58" width="346" height="322" rx="20"/>']
    xs=chain(p,52,142,["+","+","−","−","+"],66,["primary","secondary","primary","secondary"])
    p.append(txt(190,214,"Jᵢ₊ₚ = Jᵢ","math")); p.append(txt(190,260,"単位胞 p を先に与える","label")); p.append(txt(190,310,"structure-imposed","small")); p.append(txt(190,340,"wavevector basis","small"))
    xs=chain(p,418,142,["+","+","−","−","+"],66,["primary"]*4)
    # next-nearest arcs
    for i in range(3):
        x1,x2=xs[i],xs[i+2]; mid=(x1+x2)/2
        p.append(f'<path class="secondary dashed" d="M {x1} 122 Q {mid} 72 {x2} 122"/>')
    p.append(txt(565,214,"J₁ cos k + J₂ cos 2k","math")); p.append(txt(565,260,"距離 1 と 2 が競合","label")); p.append(txt(565,310,"interaction-selected","small")); p.append(txt(565,340,"wavevector","small"))
    save("periodic-r1-vs-uniform-r2.svg",p)


def main():
    overview_uniform_periodic()
    domain_wall_periodic()
    correlation_envelope_modulation()
    aabb_bond_pattern()
    kstar_temperature()
    periodic_vs_r2()


if __name__ == "__main__":
    main()
