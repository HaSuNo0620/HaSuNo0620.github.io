"""Generate R=2 Ising figures for HaSuNo0620.github.io.

Focus: J1 > 0, J2 = -kappa J1 <= 0, with J1 as the energy unit.
Figures follow the site figure conventions: transparent SVG, large labels,
heavy curves, readable paper-backed legends, and mixed roman/italic math.
"""
from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r2"
W, H = 760, 440

LIGHT = {
    "paper": "#f3efe6", "ink": "#171714", "muted": "#716d64", "line": "#cbc3b5",
    "accent": "#5866e9", "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19", "ink": "#f0eadf", "muted": "#a8a196", "line": "#4a4740",
    "accent": "#99a2ff", "green": "#8bc4a9",
}

STYLE = f"""<style>
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1;opacity:.48}}
.tick{{fill:{LIGHT['muted']};font:16px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.text{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.var{{font-style:italic}} .roman{{font-style:normal}}
.legend{{fill:{LIGHT['ink']};font:18px 'Noto Sans JP',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.legendbox{{fill:{LIGHT['paper']};fill-opacity:.92;stroke:{LIGHT['ink']};stroke-opacity:.14;stroke-width:1}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-dasharray:11 7;stroke-linecap:round;stroke-linejoin:round}}
.inkdash{{fill:none;stroke:{LIGHT['ink']};stroke-width:3.6;stroke-dasharray:9 7;stroke-linecap:round;opacity:.84}}
.muteddot{{fill:none;stroke:{LIGHT['muted']};stroke-width:3.0;stroke-dasharray:3.5 6;stroke-linecap:round}}
@media(prefers-color-scheme:dark){{
.axis{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.tick{{fill:{DARK['muted']}}}
.text,.math,.legend{{fill:{DARK['ink']}}}.legendbox{{fill:{DARK['paper']};stroke:{DARK['ink']}}}
.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}.inkdash{{stroke:{DARK['ink']}}}.muteddot{{stroke:{DARK['muted']}}}
}}
</style>"""


def mp(v, a, b, c, d):
    return c + (v-a)/(b-a)*(d-c)


def poly(points, cls):
    return f'<polyline class="{cls}" points="' + ' '.join(f'{x:.2f},{y:.2f}' for x,y in points) + '"/>'


def wrap(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{body}\n</svg>\n'


def save(name, parts):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/name).write_text(wrap('\n'.join(parts)), encoding='utf-8')


def math_text(x, y, chunks, anchor='middle', rotate=None, size=None):
    attrs = f'class="math" x="{x}" y="{y}" text-anchor="{anchor}"'
    if rotate is not None:
        attrs += f' transform="rotate({rotate} {x} {y})"'
    if size:
        attrs += f' style="font-size:{size}px"'
    spans=[]
    for text, kind in chunks:
        spans.append(f'<tspan class="{kind}">{text}</tspan>')
    return f'<text {attrs}>' + ''.join(spans) + '</text>'


def axes(xmin,xmax,ymin,ymax,xticks,yticks,xlabel_chunks,ylabel_chunks,left=96,right=716,top=28,bottom=346):
    a=[]
    for x in xticks:
        X=mp(x,xmin,xmax,left,right)
        a += [f'<line class="grid" x1="{X:.1f}" y1="{top}" x2="{X:.1f}" y2="{bottom}"/>',
              f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y in yticks:
        Y=mp(y,ymin,ymax,bottom,top)
        a += [f'<line class="grid" x1="{left}" y1="{Y:.1f}" x2="{right}" y2="{Y:.1f}"/>',
              f'<text class="tick" x="{left-14}" y="{Y+5:.1f}" text-anchor="end">{y:g}</text>']
    a += [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',
          f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>',
          math_text((left+right)/2,420,xlabel_chunks),
          math_text(27,(top+bottom)/2,ylabel_chunks,rotate=-90)]
    return a,(left,right,top,bottom)


def add_legend_box(parts, x, y, width, height):
    parts.insert(0, f'<rect class="legendbox" x="{x}" y="{y}" width="{width}" height="{height}" rx="10"/>')


def kappa_disorder(T):
    return 0.5*T*math.log(math.cosh(1.0/T))


def spectrum(T,kappa):
    K1=1.0/T; K2=-kappa/T
    lam0 = math.exp(K2)*math.cosh(K1) + math.sqrt(math.exp(2*K2)*math.sinh(K1)**2 + math.exp(-2*K2))
    disc = math.exp(2*K2)*math.cosh(K1)**2 - math.exp(-2*K2)
    re = math.exp(K2)*math.sinh(K1)
    if disc < 0:
        im = math.sqrt(-disc)
        rho = math.hypot(re,im)
        q = math.atan2(im,re)
        xi = 1.0/(-math.log(rho/lam0))
        return lam0, q, xi, True
    root = math.sqrt(max(disc,0.0))
    l1, l2 = re+root, re-root
    l = l1 if abs(l1)>=abs(l2) else l2
    q = 0.0 if l>=0 else math.pi
    xi = 1.0/(-math.log(abs(l)/lam0))
    return lam0, q, xi, False


def boundary_figure():
    a,b=axes(0.15,2.0,0.0,0.55,[0.25,0.5,1,1.5,2],[0,.1,.2,.3,.4,.5],
             [("t",'var')],[("κ",'var')])
    l,r,t,bo=b
    pts=[]
    for i in range(220):
        temp=.15+(2-.15)*i/219
        pts.append((mp(temp,.15,2,l,r),mp(kappa_disorder(temp),0,.55,bo,t)))
    a.append(poly(pts,'primary'))
    Y=mp(.5,0,.55,bo,t)
    a.append(f'<line class="muteddot" x1="{l}" y1="{Y:.1f}" x2="{r}" y2="{Y:.1f}"/>')
    a.append('<rect class="legendbox" x="470" y="34" width="224" height="78" rx="10"/>')
    a += [f'<line class="primary" x1="490" y1="55" x2="544" y2="55"/>',
          '<text class="legend" x="558" y="61">スペクトル境界</text>',
          f'<line class="muteddot" x1="490" y1="89" x2="544" y2="89"/>',
          math_text(558,95,[("κ",'var'),(" = 1/2",'roman')],anchor='start',size=18)]
    a.append('<text class="text" x="142" y="292">単調減衰する相関</text>')
    a.append('<text class="text" x="382" y="160">減衰振動する相関</text>')
    save('oscillatory-boundary.svg',a)


def qstar_figure():
    a,b=axes(0,1.0,0,.52,[0,.2,.4,.6,.8,1],[0,.1,.2,.3,.4,.5],[("κ",'var')],[("q",'var'),("*",'roman'),(" / π",'roman')])
    l,r,t,bo=b
    temps=[0.2,0.5,1.0,2.0]
    classes=['primary','secondary','inkdash','muteddot']
    for temp,cl in zip(temps,classes):
        pts=[]
        for i in range(201):
            k=i/200
            _,q,_,_=spectrum(temp,k)
            pts.append((mp(k,0,1,l,r),mp(q/math.pi,0,.52,bo,t)))
        a.append(poly(pts,cl))
    a.append('<rect class="legendbox" x="500" y="25" width="190" height="136" rx="10"/>')
    for j,(temp,cl) in enumerate(zip(temps,classes)):
        y=48+30*j
        a += [f'<line class="{cl}" x1="518" y1="{y}" x2="574" y2="{y}"/>',
              math_text(590,y+6,[("t",'var'),(" = ",'roman'),(f"{temp:g}",'roman')],anchor='start',size=18)]
    save('qstar-kappa.svg',a)


def xi_figure():
    l,r,t,bo=98,716,28,346
    a=[]; ylo,yhi=-.25,2.2
    for x in [0,.2,.4,.6,.8,1]:
        X=mp(x,0,1,l,r)
        a += [f'<line class="grid" x1="{X:.1f}" y1="{t}" x2="{X:.1f}" y2="{bo}"/>',f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y,lab in [(1,'1'),(3,'3'),(10,'10'),(30,'30'),(100,'100')]:
        Y=mp(math.log10(y),ylo,yhi,bo,t)
        a += [f'<line class="grid" x1="{l}" y1="{Y:.1f}" x2="{r}" y2="{Y:.1f}"/>',f'<text class="tick" x="{l-14}" y="{Y+5:.1f}" text-anchor="end">{lab}</text>']
    a += [f'<line class="axis" x1="{l}" y1="{t}" x2="{l}" y2="{bo}"/>',f'<line class="axis" x1="{l}" y1="{bo}" x2="{r}" y2="{bo}"/>',math_text((l+r)/2,420,[("κ",'var')]),math_text(28,(t+bo)/2,[("ξ",'var')],rotate=-90)]
    temps=[0.2,0.5,1.0,2.0]; classes=['primary','secondary','inkdash','muteddot']
    for temp,cl in zip(temps,classes):
        pts=[]
        for i in range(201):
            k=i/200
            _,_,xi,_=spectrum(temp,k)
            pts.append((mp(k,0,1,l,r),mp(math.log10(xi),ylo,yhi,bo,t)))
        a.append(poly(pts,cl))
    a.append('<rect class="legendbox" x="500" y="25" width="190" height="136" rx="10"/>')
    for j,(temp,cl) in enumerate(zip(temps,classes)):
        y=48+30*j
        a += [f'<line class="{cl}" x1="518" y1="{y}" x2="574" y2="{y}"/>',math_text(590,y+6,[("t",'var'),(" = ",'roman'),(f"{temp:g}",'roman')],anchor='start',size=18)]
    save('correlation-length-kappa.svg',a)


if __name__=='__main__':
    boundary_figure()
    qstar_figure()
    xi_figure()
