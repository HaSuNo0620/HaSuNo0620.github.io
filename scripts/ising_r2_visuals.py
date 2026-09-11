"""Generate schematic and phase-map SVGs for the R=2 Ising note.

Pure stdlib: safe for GitHub Actions without extra Python packages.
"""
from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r2"
W, H = 760, 440

LIGHT = {
    "paper": "#f3efe6", "paper2": "#ebe5d9", "ink": "#171714",
    "muted": "#716d64", "line": "#cbc3b5", "accent": "#5866e9",
    "green": "#39705a", "warm": "#9b6b2f", "softblue": "#dfe8ff",
    "softgreen": "#e1efe7", "softwarm": "#f2e6cf",
}
DARK = {
    "paper": "#1c1c19", "paper2": "#272720", "ink": "#f0eadf",
    "muted": "#a8a196", "line": "#4a4740", "accent": "#99a2ff",
    "green": "#8bc4a9", "warm": "#d3a361", "softblue": "#2d334d",
    "softgreen": "#263b31", "softwarm": "#3d3324",
}

STYLE = f"""<style>
.bg2{{fill:{LIGHT['paper2']}}}.ink{{fill:{LIGHT['ink']}}}.muted{{fill:{LIGHT['muted']}}}
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}.grid{{stroke:{LIGHT['line']};stroke-width:1;opacity:.45}}
.text{{fill:{LIGHT['ink']};font:18px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.label{{fill:{LIGHT['ink']};font:19px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.panel{{fill:{LIGHT['ink']};font:600 17px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}.var{{font-style:italic}}.roman{{font-style:normal}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.dashed{{stroke-dasharray:11 7}}.warm{{stroke:{LIGHT['warm']}}}.thin{{stroke-width:2.1}}
.node{{fill:{LIGHT['paper']};stroke:{LIGHT['ink']};stroke-width:1.8}}.bond{{stroke:{LIGHT['ink']};stroke-width:2.4}}
.wall{{stroke:{LIGHT['accent']};stroke-width:4.5}}.nextbond{{stroke:{LIGHT['green']};stroke-width:2.8;stroke-dasharray:8 6}}
.softblue{{fill:{LIGHT['softblue']}}}.softgreen{{fill:{LIGHT['softgreen']}}}.softwarm{{fill:{LIGHT['softwarm']}}}
.region{{opacity:.72}}.arrow{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.2;marker-end:url(#arrow)}}
@media(prefers-color-scheme:dark){{
.bg2{{fill:{DARK['paper2']}}}.ink,.text,.label,.panel,.math{{fill:{DARK['ink']}}}.muted,.small{{fill:{DARK['muted']}}}
.axis{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}.warm{{stroke:{DARK['warm']}}}
.node{{fill:{DARK['paper']};stroke:{DARK['ink']}}}.bond,.arrow{{stroke:{DARK['ink']}}}.wall{{stroke:{DARK['accent']}}}.nextbond{{stroke:{DARK['green']}}}
.softblue{{fill:{DARK['softblue']}}}.softgreen{{fill:{DARK['softgreen']}}}.softwarm{{fill:{DARK['softwarm']}}}
}}
</style>"""

DEFS = """<defs><marker id=\"arrow\" viewBox=\"0 0 10 10\" refX=\"9\" refY=\"5\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M 0 0 L 10 5 L 0 10 z\"/></marker></defs>"""


def wrap(body: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{DEFS}\n{body}\n</svg>\n'


def save(name: str, parts: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts)), encoding="utf-8")


def mt(x, y, chunks, anchor="middle", size=None):
    attrs = f'class="math" x="{x}" y="{y}" text-anchor="{anchor}"'
    if size:
        attrs += f' style="font-size:{size}px"'
    spans = "".join(f'<tspan class="{kind}">{txt}</tspan>' for txt, kind in chunks)
    return f'<text {attrs}>{spans}</text>'


def spin_row(parts, x0, y, spins, spacing=48, show_walls=True):
    for i in range(len(spins)-1):
        x1=x0+i*spacing; x2=x0+(i+1)*spacing
        parts.append(f'<line class="bond" x1="{x1+12}" y1="{y}" x2="{x2-12}" y2="{y}"/>')
        if show_walls and spins[i] != spins[i+1]:
            xm=(x1+x2)/2
            parts.append(f'<line class="wall" x1="{xm}" y1="{y-22}" x2="{xm}" y2="{y+22}"/>')
    for i,s in enumerate(spins):
        x=x0+i*spacing
        parts.append(f'<circle class="node" cx="{x}" cy="{y}" r="15"/>')
        parts.append(f'<text class="text" x="{x}" y="{y+6}" text-anchor="middle">{"+" if s>0 else "−"}</text>')


def overview():
    p=[]
    p += ['<text class="panel" x="34" y="38">(a) R = 1</text>', '<text class="panel" x="404" y="38">(b) R = 2</text>']
    p += ['<rect class="bg2" x="22" y="56" width="336" height="324" rx="18"/>', '<rect class="bg2" x="392" y="56" width="346" height="324" rx="18"/>']
    spins=[1,1,1,-1,-1,1]
    spin_row(p,52,150,spins,46)
    p.append('<text class="label" x="190" y="105" text-anchor="middle">independent domain walls</text>')
    p.append(mt(190,250,[("H",'var'),(" = −",'roman'),("J",'var'),("₁ Σ ",'roman'),("τ",'var'),("ᵢ",'roman')],size=22))
    p.append('<text class="small" x="190" y="296" text-anchor="middle">each wall costs energy, but walls do not couple</text>')
    spin_row(p,420,150,spins,46)
    p.append('<path class="secondary" d="M 505 210 C 530 188, 555 188, 580 210"/>')
    p.append('<path class="secondary" d="M 580 210 C 605 188, 630 188, 655 210"/>')
    p.append('<text class="label" x="565" y="105" text-anchor="middle">interacting domain walls</text>')
    p.append(mt(565,250,[("H",'var'),(" = −",'roman'),("J",'var'),("₁Σ",'roman'),("τ",'var'),("ᵢ − ",'roman'),("J",'var'),("₂Σ",'roman'),("τ",'var'),("ᵢ",'roman'),("τ",'var'),("ᵢ₊₁",'roman')],size=21))
    p.append('<text class="small" x="565" y="296" text-anchor="middle">the next-neighbor spin term becomes a wall-wall coupling</text>')
    p.append('<path class="arrow" d="M 326 218 C 350 204, 380 204, 404 218"/>')
    p.append('<text class="small" x="365" y="193" text-anchor="middle">extend interaction range</text>')
    save('overview-r1-r2.svg',p)


def domain_wall_map():
    p=[]
    spins=[1,1,1,-1,-1,1,1,-1]
    spin_row(p,72,115,spins,72)
    p.append('<text class="label" x="38" y="120" text-anchor="end">spin</text>')
    for i in range(len(spins)-1):
        x=(72+i*72+72+(i+1)*72)/2
        tau=spins[i]*spins[i+1]
        p.append(f'<circle class="node" cx="{x}" cy="235" r="17"/>')
        p.append(f'<text class="text" x="{x}" y="241" text-anchor="middle">{"+1" if tau>0 else "−1"}</text>')
        if tau<0:
            p.append(f'<text class="small" x="{x}" y="278" text-anchor="middle">wall</text>')
    p.append('<text class="label" x="38" y="241" text-anchor="end">τ</text>')
    p.append('<path class="arrow" d="M 375 155 L 375 202"/>')
    p.append(mt(375,340,[("τ",'var'),("ᵢ = ",'roman'),("s",'var'),("ᵢ ",'roman'),("s",'var'),("ᵢ₊₁",'roman')],size=24))
    p.append('<text class="small" x="375" y="378" text-anchor="middle">one reference spin + all bond variables reconstructs the spin configuration</text>')
    save('domain-wall-map.svg',p)


def transfer_network():
    p=[]
    coords={'++':(190,110), '+−':(570,110), '−+':(190,310), '−−':(570,310)}
    for name,(x,y) in coords.items():
        p.append(f'<rect class="node" x="{x-46}" y="{y-28}" width="92" height="56" rx="18"/>')
        p.append(f'<text class="label" x="{x}" y="{y+7}" text-anchor="middle">{name}</text>')
    edges=[('++','++'),('++','+−'),('+−','−+'),('+−','−−'),('−+','++'),('−+','+−'),('−−','−+'),('−−','−−')]
    for a,b in edges:
        x1,y1=coords[a]; x2,y2=coords[b]
        if a==b:
            p.append(f'<path class="arrow thin" d="M {x1-28} {y1-30} C {x1-72} {y1-82}, {x1+72} {y1-82}, {x1+28} {y1-30}"/>')
        else:
            dx=x2-x1; dy=y2-y1; n=max((dx*dx+dy*dy)**0.5,1)
            sx=x1+dx/n*55; sy=y1+dy/n*35; ex=x2-dx/n*55; ey=y2-dy/n*35
            p.append(f'<path class="arrow thin" d="M {sx:.1f} {sy:.1f} L {ex:.1f} {ey:.1f}"/>')
    p.append(mt(380,46,[("(a,b) → (b,c)", 'roman')],size=25))
    p.append('<text class="small" x="380" y="398" text-anchor="middle">the overlapping spin b is the one-step memory carried by the transfer state</text>')
    save('transfer-state-network.svg',p)


def spectrum_cartoon():
    p=[]
    centers=[145,380,615]
    labels=['two real modes','mode coalescence','complex-conjugate pair']
    for j,cx in enumerate(centers):
        p.append(f'<line class="axis" x1="{cx-85}" y1="210" x2="{cx+85}" y2="210"/>')
        p.append(f'<line class="axis" x1="{cx}" y1="125" x2="{cx}" y2="295"/>')
        p.append(f'<text class="small" x="{cx}" y="82" text-anchor="middle">{labels[j]}</text>')
    p += [
        '<circle cx="110" cy="210" r="8" fill="#5866e9"/><circle cx="175" cy="210" r="8" fill="#5866e9"/>',
        '<circle cx="380" cy="210" r="10" fill="#5866e9"/>',
        '<circle cx="615" cy="168" r="8" fill="#5866e9"/><circle cx="615" cy="252" r="8" fill="#5866e9"/>',
        '<path class="arrow" d="M 235 210 L 292 210"/>','<path class="arrow" d="M 468 210 L 525 210"/>'
    ]
    p.append(mt(145,345,[("C(r) ∼ A₁μ₁ʳ + A₂μ₂ʳ",'roman')],size=19))
    p.append(mt(380,345,[("C(r) ∼ (A+Br)μʳ",'roman')],size=19))
    p.append(mt(615,345,[("C(r) ∼ e",'roman'),("−r/ξ",'roman'),(" cos(qr+φ)",'roman')],size=19))
    save('spectrum-complexification.svg',p)


def real_fourier_map():
    p=[]
    p += ['<text class="panel" x="34" y="38">(a) real space</text>', '<text class="panel" x="410" y="38">(b) wave-vector space</text>']
    x0,x1=70,340; y0=212
    p.append(f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}"/>')
    p.append(f'<line class="axis" x1="{x0}" y1="95" x2="{x0}" y2="330"/>')
    pts=[]
    for i in range(180):
        r=14*i/179
        c=math.exp(-r/3.0)*math.cos(0.95*r-0.65)
        pts.append((x0+(x1-x0)*i/179, y0-92*c))
    p.append('<polyline class="primary" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'"/>')
    p.append(mt(205,375,[("r",'var')],size=20)); p.append(mt(25,216,[("C(r)",'roman')],size=20))
    q0,q1=445,720; base=318
    p.append(f'<line class="axis" x1="{q0}" y1="{base}" x2="{q1}" y2="{base}"/>')
    p.append(f'<line class="axis" x1="{q0}" y1="85" x2="{q0}" y2="{base}"/>')
    pts=[]
    for i in range(180):
        q=math.pi*i/179
        peak=0.27*math.pi
        val=.14+1/(1+((q-peak)/.34)**2)
        pts.append((q0+(q1-q0)*i/179, base-190*val/1.14))
    p.append('<polyline class="secondary" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'"/>')
    p.append(mt(582,375,[("q/π",'roman')],size=20)); p.append(mt(395,216,[("χ(q)",'roman')],size=20))
    p.append('<path class="arrow" d="M 350 215 L 424 215"/>')
    p.append('<text class="small" x="387" y="190" text-anchor="middle">Fourier sum over all r</text>')
    p.append('<text class="small" x="205" y="410" text-anchor="middle">tail phase → q_spec</text>')
    p.append('<text class="small" x="582" y="410" text-anchor="middle">peak position → q_χ</text>')
    save('real-fourier-map.svg',p)


def kappa_disorder(t):
    return 0.5*t*math.log(math.cosh(1/t))


def _params(t,k):
    k1=1/t; k2=-k/t
    d=math.sqrt(math.exp(2*k2)*math.sinh(k1)**2+math.exp(-2*k2))
    l0=math.exp(k2)*math.cosh(k1)+d
    a=2*math.exp(k2)*math.sinh(k1)/l0
    b=(math.exp(-2*k2)-math.exp(2*k2))/(l0*l0)
    c1=(math.exp(k2)*math.sinh(k1)+math.exp(2*k2)*math.sinh(k1)*math.cosh(k1)/d)/l0
    return a,b,c1


def _lif_expr(t,k):
    a,b,c=_params(t,k)
    return a*a*b+a*b*b-a*b*c-3*a*b-a*c-b*b*c-4*b*b+6*b*c+4*b-c


def kappa_lifshitz(t):
    lo=max(kappa_disorder(t)+1e-7,1e-6); hi=1.2
    flo=_lif_expr(t,lo); fhi=_lif_expr(t,hi)
    if flo*fhi>0: return float('nan')
    for _ in range(80):
        mid=(lo+hi)/2; fm=_lif_expr(t,mid)
        if flo*fm<=0: hi=mid; fhi=fm
        else: lo=mid; flo=fm
    return (lo+hi)/2


def phase_map():
    left,right,top,bottom=96,716,30,350
    xmin,xmax=.08,3.0; ymin,ymax=0,.6
    def X(x): return left+(x-xmin)/(xmax-xmin)*(right-left)
    def Y(y): return bottom-(y-ymin)/(ymax-ymin)*(bottom-top)
    p=[]
    for x in [.1,.5,1,1.5,2,2.5,3]:
        xx=X(x); p.append(f'<line class="grid" x1="{xx:.1f}" y1="{top}" x2="{xx:.1f}" y2="{bottom}"/>'); p.append(f'<text class="small" x="{xx:.1f}" y="378" text-anchor="middle">{x:g}</text>')
    for y in [0,.1,.2,.3,.4,.5,.6]:
        yy=Y(y); p.append(f'<line class="grid" x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}"/>'); p.append(f'<text class="small" x="{left-12}" y="{yy+5:.1f}" text-anchor="end">{y:g}</text>')
    ts=[xmin+(xmax-xmin)*i/240 for i in range(241)]
    kd=[kappa_disorder(t) for t in ts]; kl=[kappa_lifshitz(t) for t in ts]
    poly_low=[(X(xmin),Y(0))]+[(X(t),Y(k)) for t,k in zip(ts,kd)]+[(X(xmax),Y(0))]
    poly_mid=[(X(t),Y(k)) for t,k in zip(ts,kd)]+[(X(t),Y(k)) for t,k in reversed(list(zip(ts,kl)))]
    poly_hi=[(X(xmin),Y(.6)),(X(xmax),Y(.6))]+[(X(t),Y(k)) for t,k in reversed(list(zip(ts,kl)))]
    def polygon(points,cls): return f'<polygon class="{cls} region" points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in points)+'"/>'
    p += [polygon(poly_low,'softblue'),polygon(poly_mid,'softwarm'),polygon(poly_hi,'softgreen')]
    p.append('<polyline class="primary" points="'+' '.join(f'{X(t):.1f},{Y(k):.1f}' for t,k in zip(ts,kd))+'"/>')
    p.append('<polyline class="secondary dashed" points="'+' '.join(f'{X(t):.1f},{Y(k):.1f}' for t,k in zip(ts,kl))+'"/>')
    p += [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>']
    p.append(mt((left+right)/2,422,[("t = k",'var'),("B",'roman'),("T/J",'var'),("₁",'roman')],size=21))
    p.append(mt(28,205,[("κ = −J",'var'),("₂",'roman'),("/J",'var'),("₁",'roman')],size=21))
    p.append('<text class="label" x="230" y="300" text-anchor="middle">monotone correlations</text>')
    p.append(mt(230,326,[("q",'var'),("spec = 0,  ",'roman'),("q",'var'),("χ = 0",'roman')],size=17))
    p.append('<text class="label" x="495" y="235" text-anchor="middle">oscillatory tail</text>')
    p.append(mt(495,261,[("q",'var'),("spec &gt; 0,  ",'roman'),("q",'var'),("χ = 0",'roman')],size=17))
    p.append('<text class="label" x="494" y="92" text-anchor="middle">finite-q dominant response</text>')
    p.append(mt(494,118,[("q",'var'),("spec &gt; 0,  ",'roman'),("q",'var'),("χ &gt; 0",'roman')],size=17))
    p.append('<text class="small" x="565" y="319">Stephenson disorder line</text>')
    p.append('<text class="small" x="566" y="150">Lifshitz line</text>')
    p.append(f'<circle cx="{X(.08):.1f}" cy="{Y(.5):.1f}" r="6" fill="{LIGHT["ink"]}"/>')
    p.append('<text class="small" x="132" y="62">T = 0: κ = 1/2 ground-state boundary</text>')
    save('correlation-structure-map.svg',p)


def ising_liquid_map():
    p=[]
    p += ['<rect class="bg2" x="24" y="56" width="320" height="318" rx="18"/>','<rect class="bg2" x="416" y="56" width="320" height="318" rx="18"/>']
    p += ['<text class="panel" x="184" y="92" text-anchor="middle">Ising transfer spectrum</text>','<text class="panel" x="576" y="92" text-anchor="middle">liquid / OZ pole picture</text>']
    left=[('subleading eigenvalue','λ_sub / λ₀'),('decay rate','−ln|λ_sub/λ₀|'),('oscillation wave number','arg λ_sub'),('crossover','real → complex pair')]
    right=[('leading pole','k_pole'),('decay rate','Im k_pole'),('oscillation wave number','Re k_pole'),('crossover','imaginary → complex poles')]
    for i,((a,b),(c,d)) in enumerate(zip(left,right)):
        y=142+i*62
        p.append(f'<text class="small" x="65" y="{y}">{a}</text>'); p.append(f'<text class="text" x="65" y="{y+25}">{b}</text>')
        p.append(f'<text class="small" x="457" y="{y}">{c}</text>'); p.append(f'<text class="text" x="457" y="{y+25}">{d}</text>')
        p.append(f'<path class="arrow" d="M 344 {y+10} L 408 {y+10}"/>')
    p.append('<text class="small" x="380" y="410" text-anchor="middle">same spectral idea: the longest-range correlation mode changes character</text>')
    save('ising-liquid-correspondence.svg',p)


def info_channel():
    p=[]
    p += ['<text class="panel" x="34" y="38">(a) R = 1: memoryless wall noise</text>', '<text class="panel" x="398" y="38">(b) R = 2: correlated wall noise</text>']
    for side,x0 in enumerate([58,422]):
        xs=[x0+i*54 for i in range(6)]
        y=175
        for i,x in enumerate(xs):
            p.append(f'<circle class="node" cx="{x}" cy="{y}" r="16"/>'); p.append(f'<text class="text" x="{x}" y="{y+6}" text-anchor="middle">s</text>')
            if i<5: p.append(f'<line class="bond" x1="{x+17}" y1="{y}" x2="{xs[i+1]-17}" y2="{y}"/>')
        if side==0:
            for i in [0,2,4]:
                xm=(xs[i]+xs[i+1])/2; p.append(f'<line class="wall" x1="{xm}" y1="{y-28}" x2="{xm}" y2="{y+28}"/>')
            p.append('<text class="small" x="190" y="250" text-anchor="middle">each bond has an independent thermal bit-flip probability</text>')
        else:
            for i in [1,2,4]:
                xm=(xs[i]+xs[i+1])/2; p.append(f'<line class="wall" x1="{xm}" y1="{y-28}" x2="{xm}" y2="{y+28}"/>')
            p.append('<path class="secondary" d="M 500 260 C 530 235, 560 235, 590 260"/>')
            p.append('<path class="secondary" d="M 590 260 C 620 235, 650 235, 680 260"/>')
            p.append('<text class="small" x="555" y="305" text-anchor="middle">wall variables are correlated: the noise carries memory</text>')
    p.append(mt(380,370,[("P(τ",'roman'),("ᵢ₊₁",'roman'),(" | τ",'roman'),("ᵢ",'roman'),(") ≠ P(τ",'roman'),("ᵢ₊₁",'roman'),(")",'roman')],size=21))
    save('information-channel.svg',p)


if __name__ == '__main__':
    overview()
    domain_wall_map()
    transfer_network()
    spectrum_cartoon()
    real_fourier_map()
    phase_map()
    ising_liquid_map()
    info_channel()
