"""Generate the Ising-XY temperature-dependent spatial-filter crossover figure.

Pure stdlib SVG following the site's figure style. Modified Bessel ratios are
computed from their angular-integral definition with Simpson integration.
"""
from pathlib import Path
import math

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-xy-comparison"
OUT.mkdir(parents=True, exist_ok=True)

LIGHT = {"ink":"#171714","muted":"#716d64","line":"#cbc3b5","accent":"#5866e9","green":"#39705a"}
DARK = {"ink":"#f0eadf","muted":"#a8a196","line":"#4a4740","accent":"#99a2ff","green":"#8bc4a9"}
W,H=760,440
x0,y0,pw,ph=92,52,580,290
tmin,tmax=0.18,1.5
qmin,qmax=1e-5,2.0

def simpson(f,a,b,n=1200):
    if n%2: n+=1
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3

def bessel_i(m,x):
    return simpson(lambda p: math.exp(x*math.cos(p))*math.cos(m*p),0.0,math.pi)/math.pi

def q_ising(t):
    return -math.log(math.tanh(1.0/t))

def q_xy(t):
    x=1.0/t
    return -math.log(bessel_i(1,x)/bessel_i(0,x))

def X(t):
    return x0+(t-tmin)/(tmax-tmin)*pw

def Y(q):
    a,b=math.log10(qmin),math.log10(qmax)
    return y0+ph-(math.log10(max(q,qmin))-a)/(b-a)*ph

def make_path(samples, fn):
    pts=[]
    for i,t in enumerate(samples):
        pts.append(("M" if i==0 else "L")+f"{X(t):.1f},{Y(fn(t)):.1f}")
    return " ".join(pts)

samples=[tmin+(tmax-tmin)*i/179 for i in range(180)]
path_i=make_path(samples,q_ising)
path_x=make_path(samples,q_xy)
path_ia=make_path(samples,lambda t:2*math.exp(-2/t))
path_xa=make_path(samples,lambda t:t/2)

style=f"""<style>
.axis{{stroke:{LIGHT['ink']};stroke-width:1.8}}.tick{{stroke:{LIGHT['ink']};stroke-width:1.4}}.grid{{stroke:{LIGHT['line']};stroke-width:1.2}}
.ising{{fill:none;stroke:{LIGHT['accent']};stroke-width:4.5}}.xy{{fill:none;stroke:{LIGHT['green']};stroke-width:4.0}}
.isingA{{fill:none;stroke:{LIGHT['accent']};stroke-width:2;stroke-dasharray:8 7;opacity:.55}}.xyA{{fill:none;stroke:{LIGHT['green']};stroke-width:2;stroke-dasharray:8 7;opacity:.55}}
.small{{fill:{LIGHT['muted']};font:15px 'Noto Sans JP',system-ui,sans-serif}}.label{{font:17px 'Noto Sans JP',system-ui,sans-serif;font-weight:600}}
.accent{{fill:{LIGHT['accent']}}}.green{{fill:{LIGHT['green']}}}.math{{fill:{LIGHT['ink']};font:19px 'STIX Two Math','Cambria Math','Times New Roman',serif}}
@media(prefers-color-scheme:dark){{.axis,.tick{{stroke:{DARK['ink']}}}.grid{{stroke:{DARK['line']}}}.ising{{stroke:{DARK['accent']}}}.xy{{stroke:{DARK['green']}}}.isingA{{stroke:{DARK['accent']}}}.xyA{{stroke:{DARK['green']}}}.small{{fill:{DARK['muted']}}}.accent{{fill:{DARK['accent']}}}.green{{fill:{DARK['green']}}}.math{{fill:{DARK['ink']}}}}}
</style>"""
parts=[]
for q,label in [(1e-4,'10⁻⁴'),(1e-3,'10⁻³'),(1e-2,'10⁻²'),(1e-1,'10⁻¹'),(1,'1')]:
    yy=Y(q); parts += [f'<line class="grid" x1="{x0}" y1="{yy:.1f}" x2="{x0+pw}" y2="{yy:.1f}"/>',f'<text class="small" x="{x0-12}" y="{yy+5:.1f}" text-anchor="end">{label}</text>']
for t in [0.2,0.5,1.0,1.5]:
    xx=X(t); parts += [f'<line class="tick" x1="{xx:.1f}" y1="{y0+ph}" x2="{xx:.1f}" y2="{y0+ph+6}"/>',f'<text class="small" x="{xx:.1f}" y="{y0+ph+27}" text-anchor="middle">{t:g}</text>']
parts += [
    f'<line class="axis" x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}"/>',
    f'<line class="axis" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}"/>',
    f'<path class="ising" d="{path_i}"/>',f'<path class="xy" d="{path_x}"/>',f'<path class="isingA" d="{path_ia}"/>',f'<path class="xyA" d="{path_xa}"/>',
    f'<text class="label accent" x="{X(.55):.1f}" y="{Y(q_ising(.55))-12:.1f}">Ising</text>',
    f'<text class="label green" x="{X(.88):.1f}" y="{Y(q_xy(.88))-12:.1f}">XY</text>',
    f'<text class="small" x="{x0+pw-8}" y="{y0+22}" text-anchor="end">上側: qξ &gt; 1（短波長抑制）</text>',
    f'<text class="small" x="{x0+pw-8}" y="{y0+ph-16}" text-anchor="end">下側: qξ &lt; 1（協調応答）</text>',
    f'<text class="math" x="{x0+pw/2}" y="{H-24}" text-anchor="middle">k_B T / J</text>',
    f'<text class="math" x="28" y="{y0+ph/2}" text-anchor="middle" transform="rotate(-90 28 {y0+ph/2})">q_× = 1 / ξ(T)</text>',
]
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{style}\n'+"\n".join(parts)+'\n</svg>\n'
(OUT/'qxi-temperature-filter.svg').write_text(svg,encoding='utf-8')
print('generated qxi-temperature-filter.svg')
