"""Generate physical illustrations and phase-map SVGs for the R=2 Ising note.

Pure stdlib: safe for GitHub Actions without extra Python packages.
All spin-chain geometry is data-driven: spin positions, wall positions, domain bands,
and wall-particle markers come from the same spin sequence.
"""
from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r2"
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
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}.grid{{stroke:{LIGHT['line']};stroke-width:1;opacity:.42}}
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.label{{fill:{LIGHT['ink']};font:19px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.panel{{fill:{LIGHT['ink']};font:600 17px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}.var{{font-style:italic}}.roman{{font-style:normal}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}
.inkline{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}}
.mutedline{{fill:none;stroke:{LIGHT['line']};stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}}
.dashed{{stroke-dasharray:10 7}}.dot{{stroke-dasharray:2 6}}.thin{{stroke-width:2.1}}
.node{{fill:{LIGHT['paper']};stroke:{LIGHT['ink']};stroke-width:1.8}}.node2{{fill:{LIGHT['paper2']};stroke:{LIGHT['ink']};stroke-width:1.6}}
.wall{{stroke:{LIGHT['accent']};stroke-width:5.2;stroke-linecap:round}}
.nearest{{stroke:{LIGHT['accent']};stroke-width:3.3;stroke-linecap:round}}
.next{{fill:none;stroke:{LIGHT['green']};stroke-width:3;stroke-dasharray:8 6;stroke-linecap:round}}
.arrow{{fill:none;stroke:{LIGHT['ink']};stroke-width:2.2;marker-end:url(#arrow)}}
.region{{fill:{LIGHT['paper2']};opacity:.72}}.region-accent{{fill:{LIGHT['accent_soft']};opacity:.58}}
.caption-box{{fill:{LIGHT['paper']};fill-opacity:.94;stroke:{LIGHT['line']};stroke-width:1}}
@media(prefers-color-scheme:dark){{
.paper{{fill:{DARK['paper']}}}.paper2{{fill:{DARK['paper2']}}}.soft{{fill:{DARK['accent_soft']}}}
.inkfill{{fill:{DARK['ink']}}}.greenfill{{fill:{DARK['green']}}}.accentfill{{fill:{DARK['accent']}}}
.axis,.inkline,.arrow{{stroke:{DARK['ink']}}}.grid,.mutedline{{stroke:{DARK['line']}}}
.text,.label,.panel,.math{{fill:{DARK['ink']}}}.small{{fill:{DARK['muted']}}}
.primary,.wall,.nearest{{stroke:{DARK['accent']}}}.secondary,.next{{stroke:{DARK['green']}}}
.node{{fill:{DARK['paper']};stroke:{DARK['ink']}}}.node2{{fill:{DARK['paper2']};stroke:{DARK['ink']}}}
.region{{fill:{DARK['paper2']}}}.region-accent{{fill:{DARK['accent_soft']}}}
.caption-box{{fill:{DARK['paper']};stroke:{DARK['line']}}}
}}
</style>"""

DEFS = """<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z"/></marker>
</defs>"""


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


def text_box(parts, x, y, width, text, *, cls="small", height=30):
    """Readable label with an opaque-ish paper background."""
    parts.append(f'<rect class="caption-box" x="{x-width/2:.1f}" y="{y-height+7:.1f}" width="{width}" height="{height}" rx="8"/>')
    parts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="middle">{text}</text>')


def spin_positions(x0, spins, spacing):
    return [x0 + i * spacing for i in range(len(spins))]


def wall_positions(x0, spins, spacing):
    xs = spin_positions(x0, spins, spacing)
    return [(xs[i] + xs[i + 1]) / 2 for i in range(len(spins) - 1) if spins[i] != spins[i + 1]]


def domain_segments(x0, spins, spacing):
    """Return (left, right, sign) domains from the spin sequence itself."""
    xs = spin_positions(x0, spins, spacing)
    left_edge = xs[0] - spacing / 2
    right_edge = xs[-1] + spacing / 2
    walls = wall_positions(x0, spins, spacing)
    edges = [left_edge, *walls, right_edge]
    segments = []
    start_i = 0
    for left, right in zip(edges[:-1], edges[1:]):
        segments.append((left, right, spins[start_i]))
        while start_i + 1 < len(spins) and xs[start_i + 1] < right - 1e-9:
            start_i += 1
        if start_i + 1 < len(spins):
            start_i += 1
    return segments


def draw_domain_bands(parts, x0, y, spins, spacing, height=88, rx=16):
    """Draw domains with boundaries exactly at sign-change midpoints."""
    for left, right, sign in domain_segments(x0, spins, spacing):
        cls = "region-accent" if sign > 0 else "region"
        parts.append(
            f'<rect class="{cls}" x="{left:.1f}" y="{y-height/2:.1f}" '
            f'width="{right-left:.1f}" height="{height}" rx="{rx}"/>'
        )


def spin_row(parts, x0, y, spins, spacing=48, walls=True, r=15):
    xs = spin_positions(x0, spins, spacing)
    wall_xs = set(wall_positions(x0, spins, spacing))
    for i in range(len(spins)-1):
        x1, x2 = xs[i], xs[i+1]
        parts.append(f'<line class="inkline" x1="{x1+r}" y1="{y}" x2="{x2-r}" y2="{y}"/>')
        xm = (x1 + x2) / 2
        if walls and xm in wall_xs:
            parts.append(f'<line class="wall" x1="{xm}" y1="{y-26}" x2="{xm}" y2="{y+26}"/>')
    for x, s in zip(xs, spins):
        parts.append(f'<circle class="node" cx="{x}" cy="{y}" r="{r}"/>')
        parts.append(f'<text class="text" x="{x}" y="{y+6}" text-anchor="middle">{"+" if s>0 else "−"}</text>')


def overview():
    """R=1 and R=2 use exactly the same spin configuration and wall geometry."""
    p=[]
    p += ['<text class="panel" x="42" y="38">(a) R = 1 — 自由なドメイン壁</text>', '<text class="panel" x="404" y="38">(b) R = 2 — 相互作用するドメイン壁</text>']
    p += ['<rect class="region" x="24" y="58" width="334" height="312" rx="20"/>', '<rect class="region" x="392" y="58" width="344" height="312" rx="20"/>']
    spins=[1,1,1,-1,-1,1,1]
    left_x0, right_x0, sp = 50, 418, 44
    spin_row(p,left_x0,142,spins,sp)
    spin_row(p,right_x0,142,spins,sp)
    left_walls = wall_positions(left_x0, spins, sp)
    right_walls = wall_positions(right_x0, spins, sp)
    # wall-particle view is derived from exactly the same wall coordinates
    for x in left_walls:
        p.append(f'<circle class="accentfill" cx="{x}" cy="240" r="10"/>')
    if len(left_walls) >= 2:
        p.append(f'<path class="mutedline dashed" d="M {left_walls[0]} 240 L {left_walls[1]} 240"/>')
    text_box(p,190,284,270,'壁は独立な熱欠陥として現れる')
    for x in right_walls:
        p.append(f'<circle class="accentfill" cx="{x}" cy="240" r="10"/>')
    if len(right_walls) >= 2:
        x1, x2 = right_walls[:2]
        dx=(x2-x1-20)/6
        path=f'M {x1+10:.1f} 240 '
        yy=-10
        xx=x1+10
        for _ in range(5):
            xx += dx
            path += f'l {dx:.1f} {yy} '
            yy *= -1
        path += f'L {x2-10:.1f} 240'
        p.append(f'<path class="secondary" d="{path}"/>')
    text_box(p,570,284,270,'隣接する壁の統計が結合する')
    p.append(mt(190,330,[("H",'var'),(" = −",'roman'),("J",'var'),("₁ Σ ",'roman'),("τ",'var'),("ᵢ",'roman')],size=21))
    p.append(mt(570,330,[("H",'var'),(" = −",'roman'),("J",'var'),("₁Σ",'roman'),("τ",'var'),("ᵢ − ",'roman'),("J",'var'),("₂Σ",'roman'),("τ",'var'),("ᵢ",'roman'),("τ",'var'),("ᵢ₊₁",'roman')],size=20))
    p.append('<path class="arrow" d="M 350 214 C 365 204, 380 204, 395 214"/>')
    text_box(p,372,190,145,'相互作用範囲を延ばす')
    save('overview-r1-r2.svg',p)


def domain_wall_map():
    """Domains, walls and bond variables are all generated from the same spin data."""
    p=[]
    spins=[1,1,1,-1,-1,1,1,-1]
    x0, y, sp = 78, 121, 82
    draw_domain_bands(p,x0,y,spins,sp,height=90,rx=18)
    spin_row(p,x0,y,spins,sp,True,15)
    # Domain labels are centered on the actual generated segments.
    for left,right,sign in domain_segments(x0,spins,spins and sp):
        label='+ ドメイン' if sign>0 else '− ドメイン'
        p.append(f'<text class="small" x="{(left+right)/2:.1f}" y="64" text-anchor="middle">{label}</text>')
    xs=spin_positions(x0,spins,sp)
    for i in range(len(spins)-1):
        x=(xs[i]+xs[i+1])/2
        tau=spins[i]*spins[i+1]
        cls='accentfill' if tau<0 else 'inkfill'
        rr=9 if tau<0 else 5
        p.append(f'<circle class="{cls}" cx="{x}" cy="242" r="{rr}"/>')
        p.append(f'<text class="small" x="{x}" y="276" text-anchor="middle">{"壁" if tau<0 else "壁なし"}</text>')
    p.append('<path class="arrow" d="M 380 168 L 380 216"/>')
    p.append(mt(380,332,[("τ",'var'),("ᵢ = ",'roman'),("s",'var'),("ᵢ ",'roman'),("s",'var'),("ᵢ₊₁",'roman')],size=24))
    text_box(p,380,376,500,'ドメイン壁変数は絶対的なスピン向きではなく境界を記録する')
    save('domain-wall-map.svg',p)


def transfer_network():
    p=[]
    coords={'++':(190,110), '+−':(570,110), '−+':(190,310), '−−':(570,310)}
    for name,(x,y) in coords.items():
        p.append(f'<rect class="node2" x="{x-46}" y="{y-28}" width="92" height="56" rx="18"/>')
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
    text_box(p,380,406,500,'共有スピン b が鎖に沿って1ステップの記憶を運ぶ')
    save('transfer-state-network.svg',p)


def frustration_picture():
    p=[]
    p.append('<text class="panel" x="38" y="38">同じスピン鎖上で競合する二つの局所選好</text>')
    spins=[1,1,-1,-1,1,1,-1,-1]
    x0=72; y=180; sp=82
    spin_row(p,x0,y,spins,sp,False,16)
    for i in range(len(spins)-1):
        x1=x0+i*sp; x2=x0+(i+1)*sp
        p.append(f'<line class="nearest" x1="{x1+18}" y1="{y+38}" x2="{x2-18}" y2="{y+38}"/>')
    for i in range(len(spins)-2):
        x1=x0+i*sp; x2=x0+(i+2)*sp; xm=(x1+x2)/2
        p.append(f'<path class="next" d="M {x1} {y-25} Q {xm} {y-92} {x2} {y-25}"/>')
    text_box(p,260,270,330,'J₁ > 0：隣接スピンは揃いたい')
    text_box(p,260,310,390,'J₂ < 0：2サイト離れたスピンは反対を向きたい')
    p.append('<text class="label" x="380" y="356" text-anchor="middle">二つの局所選好は全結合で同時には満たせない</text>')
    p.append('<text class="small" x="380" y="388" text-anchor="middle">競合が強まると ++−− の周期構造が有利になる</text>')
    save('frustration-competition.svg',p)


def spectrum_cartoon():
    p=[]
    labels=['disorder line より下','境界を少し越えた直後','振動領域の内部']
    qvals=[0.0,0.36,0.86]
    phivals=[0.0,-1.32,-0.45]
    for row,(lab,q,phi) in enumerate(zip(labels,qvals,phivals)):
        y0=95+row*125
        text_box(p,135,y0-32,210,lab)
        p.append(f'<line class="mutedline" x1="55" y1="{y0}" x2="705" y2="{y0}"/>')
        pts=[]
        for i in range(260):
            r=14*i/259
            c=math.exp(-r/3.0) if q==0 else math.exp(-r/3.1)*math.cos(q*r+phi)
            pts.append((55+650*i/259, y0-44*c))
        p.append('<polyline class="primary" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'"/>')
        up=[]; dn=[]
        for i in range(100):
            r=14*i/99; amp=44*math.exp(-r/3.1); x=55+650*i/99
            up.append((x,y0-amp)); dn.append((x,y0+amp))
        p.append('<polyline class="mutedline dashed" points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in up)+'"/>')
        p.append('<polyline class="mutedline dashed" points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in dn)+'"/>')
    text_box(p,380,424,510,'複素モードが生まれると最初の節が無限遠側から近づいてくる',cls='label',height=34)
    save('spectrum-complexification.svg',p)


def real_fourier_map():
    p=[]
    text_box(p,250,38,430,'中間領域：遠方は振動するが qχ = 0',cls='panel',height=32)
    lx0,lx1=62,352; ly=205
    p += [f'<line class="axis" x1="{lx0}" y1="{ly}" x2="{lx1}" y2="{ly}"/>', f'<line class="axis" x1="{lx0}" y1="90" x2="{lx0}" y2="320"/>']
    pts=[]
    for i in range(220):
        r=14*i/219
        c=math.exp(-r/2.9)*math.cos(.42*r-1.12)
        pts.append((lx0+(lx1-lx0)*i/219, ly-96*c))
    p.append('<polyline class="primary" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'"/>')
    text_box(p,205,350,300,'C(r)：遠方の tail はすでに符号反転する')
    rx0,rx1=444,710; rb=312; rt=92
    p += [f'<line class="axis" x1="{rx0}" y1="{rb}" x2="{rx1}" y2="{rb}"/>', f'<line class="axis" x1="{rx0}" y1="{rt}" x2="{rx0}" y2="{rb}"/>']
    pts=[]
    for i in range(220):
        u=i/219
        val=1.0/(1+3.8*u*u)+0.045*math.exp(-((u-.28)/.12)**2)
        x=rx0+(rx1-rx0)*u; y=rb-190*val
        pts.append((x,y))
    p.append('<polyline class="secondary" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'"/>')
    qspecx=rx0+(rx1-rx0)*.28
    p.append(f'<line class="primary dashed thin" x1="{qspecx:.1f}" y1="{rt+24}" x2="{qspecx:.1f}" y2="{rb}"/>')
    text_box(p,575,78,245,'χ(q) の最大はまだ q = 0')
    text_box(p,615,350,260,'破線：長距離 tail の q_spec')
    p.append('<path class="arrow" d="M 365 204 L 425 204"/>')
    text_box(p,395,180,115,'Fourier 和')
    save('real-fourier-map.svg',p)


def kappa_disorder(t):
    return .5*t*math.log(math.cosh(1/t))


def lam0(t,k):
    K1=1/t; K2=-k/t
    D=math.sqrt(math.exp(2*K2)*math.sinh(K1)**2 + math.exp(-2*K2))
    return math.exp(K2)*math.cosh(K1)+D


def abc1(t,k):
    K1=1/t; K2=-k/t; l0=lam0(t,k)
    D=math.sqrt(math.exp(2*K2)*math.sinh(K1)**2 + math.exp(-2*K2))
    a=2*math.exp(K2)*math.sinh(K1)/l0
    b=(math.exp(-2*K2)-math.exp(2*K2))/(l0*l0)
    c1=(math.exp(K2)*math.sinh(K1)+math.exp(2*K2)*math.sinh(K1)*math.cosh(K1)/D)/l0
    return a,b,c1


def lif_expr(t,k):
    a,b,c=abc1(t,k)
    return a*a*b+a*b*b-a*b*c-3*a*b-a*c-b*b*c-4*b*b+6*b*c+4*b-c


def kappa_lifshitz(t):
    lo=max(.0005,kappa_disorder(t)); hi=1.2
    flo=lif_expr(t,lo+1e-6)
    steps=500
    x0=lo+1e-6; f0=flo
    for j in range(1,steps+1):
        x=lo+(hi-lo)*j/steps; f=lif_expr(t,x)
        if f0*f<=0:
            a0,b0=x0,x
            for _ in range(55):
                m=(a0+b0)/2; fm=lif_expr(t,m)
                if lif_expr(t,a0)*fm<=0: b0=m
                else: a0=m
            return (a0+b0)/2
        x0,f0=x,f
    return float('nan')


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
    poly_mid=[(X(t),Y(k)) for t,k in zip(ts,kd)]+[(X(t),Y(k)) for t,k in reversed(list(zip(ts,kl)))]
    p.append('<polygon class="region" points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in poly_mid)+'"/>')
    p.append('<polyline class="primary" points="'+' '.join(f'{X(t):.1f},{Y(k):.1f}' for t,k in zip(ts,kd))+'"/>')
    p.append('<polyline class="secondary dashed" points="'+' '.join(f'{X(t):.1f},{Y(k):.1f}' for t,k in zip(ts,kl))+'"/>')
    p += [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>']
    p.append(mt((left+right)/2,422,[("t = k",'var'),("B",'roman'),("T/J",'var'),("₁",'roman')],size=21))
    p.append(mt(28,205,[("κ = −J",'var'),("₂",'roman'),("/J",'var'),("₁",'roman')],size=21))
    text_box(p,235,306,220,'単調減衰する相関',cls='label')
    text_box(p,495,230,225,'遠方で振動する相関',cls='label')
    text_box(p,505,92,240,'有限波数応答が支配',cls='label')
    text_box(p,570,319,245,'Stephenson disorder line')
    text_box(p,620,151,150,'Lifshitz line')
    p.append(f'<circle class="inkfill" cx="{X(.08):.1f}" cy="{Y(.5):.1f}" r="6"/>')
    text_box(p,240,62,300,'T = 0：κ = 1/2 基底状態境界')
    save('correlation-structure-map.svg',p)


def ising_liquid_map():
    p=[]
    p += ['<rect class="region" x="24" y="56" width="320" height="318" rx="18"/>','<rect class="region" x="416" y="56" width="320" height="318" rx="18"/>']
    p += ['<text class="panel" x="184" y="92" text-anchor="middle">Ising 転送スペクトル</text>','<text class="panel" x="576" y="92" text-anchor="middle">液体論 / OZ pole</text>']
    left=[('subleading 固有値','λ_sub / λ₀'),('減衰率','−ln|λ_sub/λ₀|'),('振動波数','arg λ_sub'),('クロスオーバー','実数 → 複素共役対')]
    right=[('leading pole','k_pole'),('減衰率','Im k_pole'),('振動波数','Re k_pole'),('クロスオーバー','純虚数 → 複素 pole')]
    for i,((a,b),(c,d)) in enumerate(zip(left,right)):
        y=142+i*62
        p.append(f'<text class="small" x="65" y="{y}">{a}</text>'); p.append(f'<text class="text" x="65" y="{y+25}">{b}</text>')
        p.append(f'<text class="small" x="457" y="{y}">{c}</text>'); p.append(f'<text class="text" x="457" y="{y+25}">{d}</text>')
        p.append(f'<path class="arrow" d="M 344 {y+10} L 408 {y+10}"/>')
    text_box(p,380,410,500,'最長距離相関を支配するスペクトルモードの型が変わる')
    save('ising-liquid-correspondence.svg',p)


def info_channel():
    p=[]
    p += ['<text class="panel" x="34" y="38">(a) R = 1：独立な熱的反転</text>', '<text class="panel" x="398" y="38">(b) R = 2：相関した熱的反転</text>']
    for side,x0 in enumerate([58,422]):
        xs=[x0+i*54 for i in range(6)]; y=175
        for i,x in enumerate(xs):
            p.append(f'<circle class="node" cx="{x}" cy="{y}" r="16"/>'); p.append(f'<text class="text" x="{x}" y="{y+6}" text-anchor="middle">s</text>')
            if i<5: p.append(f'<line class="inkline" x1="{x+17}" y1="{y}" x2="{xs[i+1]-17}" y2="{y}"/>')
        if side==0:
            for i in [0,2,4]:
                xm=(xs[i]+xs[i+1])/2; p.append(f'<line class="wall" x1="{xm}" y1="{y-28}" x2="{xm}" y2="{y+28}"/>')
            text_box(p,190,250,280,'各 bond の熱的反転は独立')
        else:
            for i in [1,2,4]:
                xm=(xs[i]+xs[i+1])/2; p.append(f'<line class="wall" x1="{xm}" y1="{y-28}" x2="{xm}" y2="{y+28}"/>')
            p.append('<path class="secondary" d="M 500 260 C 530 235, 560 235, 590 260"/>')
            p.append('<path class="secondary" d="M 590 260 C 620 235, 650 235, 680 260"/>')
            text_box(p,555,305,310,'壁の出現確率が隣接する壁に依存')
    p.append(mt(380,370,[("P(τ",'roman'),("ᵢ₊₁",'roman'),(" | τ",'roman'),("ᵢ",'roman'),(") ≠ P(τ",'roman'),("ᵢ₊₁",'roman'),(")",'roman')],size=21))
    save('information-channel.svg',p)


if __name__ == '__main__':
    overview()
    domain_wall_map()
    transfer_network()
    frustration_picture()
    spectrum_cartoon()
    real_fourier_map()
    phase_map()
    ising_liquid_map()
    info_channel()
