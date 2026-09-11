"""Generate exact three-regime R=2 Ising comparison figures.

The figures compare finite-distance C(r) and static susceptibility chi(q)
at t=k_B T/J1=1 for representative points below the disorder line,
between disorder and Lifshitz lines, and above the Lifshitz line.
Uses only the Python standard library so it is safe in GitHub Pages CI.
"""
from __future__ import annotations

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r2"
W, H = 760, 440

LIGHT = {"paper":"#f3efe6","ink":"#171714","muted":"#716d64","line":"#cbc3b5","accent":"#5866e9","green":"#39705a"}
DARK = {"paper":"#1c1c19","ink":"#f0eadf","muted":"#a8a196","line":"#4a4740","accent":"#99a2ff","green":"#8bc4a9"}
STYLE = f"""<style>
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}
.grid{{stroke:{LIGHT['line']};stroke-width:1.1;opacity:.48}}
.tick{{fill:{LIGHT['muted']};font:16px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.math{{fill:{LIGHT['ink']};font:20px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
.var{{font-style:italic}} .roman{{font-style:normal}}
.legend{{fill:{LIGHT['ink']};font:18px system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.legendbox{{fill:{LIGHT['paper']};fill-opacity:.92;stroke:{LIGHT['ink']};stroke-opacity:.14;stroke-width:1}}
.primary{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{LIGHT['green']};stroke-width:3.6;stroke-dasharray:11 7;stroke-linecap:round;stroke-linejoin:round}}
.inkdash{{fill:none;stroke:{LIGHT['ink']};stroke-width:3.6;stroke-dasharray:9 7;stroke-linecap:round;opacity:.84}}
.zero{{fill:none;stroke:{LIGHT['muted']};stroke-width:2.0;stroke-dasharray:3.5 6}}
@media(prefers-color-scheme:dark){{
.axis{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.tick{{fill:{DARK['muted']}}}
.math,.legend{{fill:{DARK['ink']}}}.legendbox{{fill:{DARK['paper']};stroke:{DARK['ink']}}}
.primary{{stroke:{DARK['accent']}}}.secondary{{stroke:{DARK['green']}}}
.inkdash{{stroke:{DARK['ink']}}}.zero{{stroke:{DARK['muted']}}}
}}
</style>"""


def mp(v,a,b,c,d):
    return c+(v-a)/(b-a)*(d-c)


def poly(points,cls):
    return f'<polyline class="{cls}" points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+'"/>'


def math_text(x,y,chunks,anchor='middle',rotate=None,size=None):
    attrs=f'class="math" x="{x}" y="{y}" text-anchor="{anchor}"'
    if rotate is not None:
        attrs += f' transform="rotate({rotate} {x} {y})"'
    if size:
        attrs += f' style="font-size:{size}px"'
    spans=''.join(f'<tspan class="{kind}">{txt}</tspan>' for txt,kind in chunks)
    return f'<text {attrs}>{spans}</text>'


def save(name,parts):
    OUT.mkdir(parents=True,exist_ok=True)
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n'+'\n'.join(parts)+'\n</svg>\n'
    (OUT/name).write_text(svg,encoding='utf-8')


def axes(xmin,xmax,ymin,ymax,xticks,yticks,xlabel,ylabel,left=96,right=716,top=28,bottom=346):
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
          math_text((left+right)/2,420,xlabel), math_text(27,(top+bottom)/2,ylabel,rotate=-90)]
    return a,(left,right,top,bottom)


def coeffs(t,kappa):
    K1=1.0/t; K2=-kappa/t
    D=math.sqrt(math.exp(2*K2)*math.sinh(K1)**2+math.exp(-2*K2))
    lam0=math.exp(K2)*math.cosh(K1)+D
    a=2*math.exp(K2)*math.sinh(K1)/lam0
    b=(math.exp(-2*K2)-math.exp(2*K2))/(lam0*lam0)
    c1=(math.exp(K2)*math.sinh(K1)+math.exp(2*K2)*math.sinh(K1)*math.cosh(K1)/D)/lam0
    return a,b,c1


def corr(t,kappa,rmax):
    a,b,c1=coeffs(t,kappa)
    values=[1.0,c1]
    for _ in range(1,rmax):
        values.append(a*values[-1]-b*values[-2])
    return values


def chi(t,kappa,nq=301,rmax=600):
    C=corr(t,kappa,rmax)
    out=[]
    for iq in range(nq):
        q=math.pi*iq/(nq-1)
        value=1.0+2*sum(C[r]*math.cos(q*r) for r in range(1,len(C)))
        out.append((q,value/t))
    return out


def legend(parts):
    # Semi-opaque site-paper background prevents data curves from crossing legend text.
    parts.append('<rect class="legendbox" x="494" y="26" width="202" height="106" rx="10"/>')
    entries=[('primary','κ = 0.15'),('secondary','κ = 0.27'),('inkdash','κ = 0.45')]
    for j,(cl,lab) in enumerate(entries):
        y=48+30*j
        parts += [f'<line class="{cl}" x1="515" y1="{y}" x2="570" y2="{y}"/>',
                  f'<text class="legend" x="585" y="{y+6}">{lab}</text>']


def correlation_figure():
    parts,box=axes(0,16,-.18,1.03,[0,4,8,12,16],[0,.25,.5,.75,1],
                   [('r','var')],[('C','var'),('(','roman'),('r','var'),(')','roman')])
    l,r,t,bo=box
    for kappa,cl in [(.15,'primary'),(.27,'secondary'),(.45,'inkdash')]:
        vals=corr(1.0,kappa,16)
        parts.append(poly([(mp(i,0,16,l,r),mp(v,-.18,1.03,bo,t)) for i,v in enumerate(vals)],cl))
    y0=mp(0,-.18,1.03,bo,t)
    parts.append(f'<line class="zero" x1="{l}" y1="{y0:.1f}" x2="{r}" y2="{y0:.1f}"/>')
    legend(parts)
    save('three-regimes-correlation.svg',parts)


def susceptibility_figure():
    parts,box=axes(0,1,0,1.05,[0,.2,.4,.6,.8,1],[0,.25,.5,.75,1],
                   [('q','var'),(' / π','roman')],
                   [('χ','var'),('(','roman'),('q','var'),(') / ','roman'),('χ','var'),('max','roman')])
    l,r,t,bo=box
    for kappa,cl in [(.15,'primary'),(.27,'secondary'),(.45,'inkdash')]:
        vals=chi(1.0,kappa)
        vmax=max(v for _,v in vals)
        parts.append(poly([(mp(q/math.pi,0,1,l,r),mp(v/vmax,0,1.05,bo,t)) for q,v in vals],cl))
    legend(parts)
    save('three-regimes-susceptibility.svg',parts)


if __name__=='__main__':
    correlation_figure()
    susceptibility_figure()
