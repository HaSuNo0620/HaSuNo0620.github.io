"""Regenerate the R=1 Ising figures using Figure Style v1.1."""
from __future__ import annotations
import math
from pathlib import Path
from figure_style import COLORS, DARK_COLORS

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r1"
W, H = 760, 440
KVALS = (0.4, 0.8, 1.2, 1.8)
STYLES = ("muteddot", "inkdash", "primary", "secondary")

STYLE = f"""<style>
.axis{{stroke:{COLORS["ink"]};stroke-width:1.4}}.grid{{stroke:{COLORS["line"]};stroke-width:.9;opacity:.52}}
.tick{{fill:{COLORS["muted"]};font:14px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.label{{fill:{COLORS["ink"]};font:17px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.legend{{fill:{COLORS["muted"]};font:14px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.panel{{fill:{COLORS["ink"]};font:600 16px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.primary{{fill:none;stroke:{COLORS["accent"]};stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{COLORS["green"]};stroke-width:2.6;stroke-dasharray:9 6;stroke-linecap:round;stroke-linejoin:round}}
.inkdash{{fill:none;stroke:{COLORS["ink"]};stroke-width:2.6;stroke-dasharray:8 6;opacity:.82}}
.muteddot{{fill:none;stroke:{COLORS["muted"]};stroke-width:2.6;stroke-dasharray:3 5;opacity:.92}}
@media(prefers-color-scheme:dark){{.axis{{stroke:{DARK_COLORS["ink"]}}}.grid{{stroke:{DARK_COLORS["line"]}}}.tick,.legend{{fill:{DARK_COLORS["muted"]}}}.label,.panel{{fill:{DARK_COLORS["ink"]}}}.primary{{stroke:{DARK_COLORS["accent"]}}}.secondary{{stroke:{DARK_COLORS["green"]}}}.inkdash{{stroke:{DARK_COLORS["ink"]}}}.muteddot{{stroke:{DARK_COLORS["muted"]}}}}}
</style>"""

def mp(v,a,b,c,d): return c+(v-a)/(b-a)*(d-c)
def line(points, cls): return f'<polyline class="{cls}" points="'+" ".join(f"{x:.1f},{y:.1f}" for x,y in points)+'"/>'
def wrap(body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{body}\n</svg>\n'
def save(name, parts): OUT.mkdir(parents=True, exist_ok=True); (OUT/name).write_text(wrap("\n".join(parts)), encoding="utf-8")

def axes(xmin,xmax,ymin,ymax,xticks,yticks,xlabel,ylabel,left=88,right=724,top=26,bottom=350):
    a=[]
    for x in xticks:
        X=mp(x,xmin,xmax,left,right); a += [f'<line class="grid" x1="{X:.1f}" y1="{top}" x2="{X:.1f}" y2="{bottom}"/>',f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y in yticks:
        Y=mp(y,ymin,ymax,bottom,top); a += [f'<line class="grid" x1="{left}" y1="{Y:.1f}" x2="{right}" y2="{Y:.1f}"/>',f'<text class="tick" x="{left-12}" y="{Y+5:.1f}" text-anchor="end">{y:g}</text>']
    a += [f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>',f'<text class="label" x="405" y="418" text-anchor="middle">{xlabel}</text>',f'<text class="label" x="25" y="188" text-anchor="middle" transform="rotate(-90 25 188)">{ylabel}</text>']
    return a,(left,right,top,bottom)

def add_legend(a):
    for i,(K,cl) in enumerate(zip(KVALS,STYLES)):
        y=44+25*i; a += [f'<line class="{cl}" x1="548" y1="{y}" x2="588" y2="{y}"/>',f'<text class="legend" x="600" y="{y+5}">βJ = {K:.1f}</text>']

def magnetization():
    a,b=axes(-2.5,2.5,-1.05,1.05,[-2,-1,0,1,2],[-1,-.5,0,.5,1],"h / J","m"); l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        pts=[]
        for i in range(81):
            x=-2.5+5*i/80; bh=K*x; m=math.sinh(bh)/math.sqrt(math.sinh(bh)**2+math.exp(-4*K)); pts.append((mp(x,-2.5,2.5,l,r),mp(m,-1.05,1.05,bo,t)))
        a.append(line(pts,cl))
    add_legend(a); save("magnetization-field.svg",a)

def correlation():
    a,b=axes(0,30,0,1.02,[0,5,10,15,20,25,30],[0,.25,.5,.75,1],"r","C(r)"); l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        q=math.tanh(K); a.append(line([(mp(i,0,30,l,r),mp(q**i,0,1.02,bo,t)) for i in range(31)],cl))
    add_legend(a); save("correlation-distance.svg",a)

def susceptibility():
    a,b=axes(0,1,0,1.02,[0,.25,.5,.75,1],[0,.25,.5,.75,1],"q / π","χ(q) / χ(0)"); l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        u=math.tanh(K); c0=K*(1-u*u)/(1-2*u+u*u); pts=[]
        for i in range(81):
            q=math.pi*i/80; c=K*(1-u*u)/(1-2*u*math.cos(q)+u*u); pts.append((mp(i/80,0,1,l,r),mp(c/c0,0,1.02,bo,t)))
        a.append(line(pts,cl))
    add_legend(a); save("susceptibility-q.svg",a)

def correlation_length():
    l,r,t,bo=92,724,26,350; a=[]; xmin,xmax=.25,4; ylo,yhi=-1,3.2
    for x in [.5,1,2,3,4]:
        X=mp(x,xmin,xmax,l,r); a += [f'<line class="grid" x1="{X:.1f}" y1="{t}" x2="{X:.1f}" y2="{bo}"/>',f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y,lab in [(.1,"10⁻¹"),(1,"1"),(10,"10"),(100,"10²"),(1000,"10³")]:
        Y=mp(math.log10(y),ylo,yhi,bo,t); a += [f'<line class="grid" x1="{l}" y1="{Y:.1f}" x2="{r}" y2="{Y:.1f}"/>',f'<text class="tick" x="{l-12}" y="{Y+5:.1f}" text-anchor="end">{lab}</text>']
    a += [f'<line class="axis" x1="{l}" y1="{t}" x2="{l}" y2="{bo}"/>',f'<line class="axis" x1="{l}" y1="{bo}" x2="{r}" y2="{bo}"/>','<text class="label" x="407" y="418" text-anchor="middle">T / J</text>','<text class="label" x="25" y="188" text-anchor="middle" transform="rotate(-90 25 188)">ξ</text>']
    ex=[]; ap=[]
    for i in range(81):
        T=xmin+(xmax-xmin)*i/80; K=1/T; xi=-1/math.log(math.tanh(K)); xa=.5*math.exp(2*K); X=mp(T,xmin,xmax,l,r); ex.append((X,mp(math.log10(xi),ylo,yhi,bo,t))); ap.append((X,mp(math.log10(xa),ylo,yhi,bo,t)))
    a += [line(ex,"primary"),line(ap,"secondary"),'<line class="primary" x1="500" y1="48" x2="540" y2="48"/>','<text class="legend" x="552" y="53">exact</text>','<line class="secondary" x1="500" y1="76" x2="540" y2="76"/>','<text class="legend" x="552" y="81">low-T asymptote</text>']; save("correlation-length-temperature.svg",a)

def spatial_response():
    a=[]; pls=[70,416]; prs=[350,696]; pt,pb=52,338; ymin,ymax=-.19,.19
    for idx,(pl,pr,q) in enumerate(zip(pls,prs,[math.pi/10,math.pi/2])):
        for y in [-.1,0,.1]:
            Y=mp(y,ymin,ymax,pb,pt); a.append(f'<line class="grid" x1="{pl}" y1="{Y:.1f}" x2="{pr}" y2="{Y:.1f}"/>')
            if idx==0: a.append(f'<text class="tick" x="{pl-11}" y="{Y+5:.1f}" text-anchor="end">{y:g}</text>')
        for i in [0,10,20,30,40]:
            X=mp(i,0,40,pl,pr); a += [f'<line class="grid" x1="{X:.1f}" y1="{pt}" x2="{X:.1f}" y2="{pb}"/>',f'<text class="tick" x="{X:.1f}" y="366" text-anchor="middle">{i}</text>']
        a += [f'<line class="axis" x1="{pl}" y1="{pt}" x2="{pl}" y2="{pb}"/>',f'<line class="axis" x1="{pl}" y1="{pb}" x2="{pr}" y2="{pb}"/>',f'<text class="panel" x="{pl+9}" y="{pt+20}">({"ab"[idx]}) q = {"π/10" if idx==0 else "π/2"}</text>',f'<text class="label" x="{(pl+pr)/2:.1f}" y="410" text-anchor="middle">site i</text>']
        if idx==0: a.append('<text class="label" x="22" y="195" text-anchor="middle" transform="rotate(-90 22 195)">hᵢ , ⟨sᵢ⟩</text>')
        K=1.2; u=math.tanh(K); chi=K*(1-u*u)/(1-2*u*math.cos(q)+u*u); field=[]; resp=[]
        for i in range(41):
            X=mp(i,0,40,pl,pr); c=math.cos(q*i); field.append((X,mp(.05*c,ymin,ymax,pb,pt))); resp.append((X,mp(chi*.05*c,ymin,ymax,pb,pt)))
        a += [line(resp,"primary"),line(field,"secondary")]
    a += ['<line class="primary" x1="210" y1="25" x2="252" y2="25"/>','<text class="legend" x="264" y="30">linear response ⟨sᵢ⟩</text>','<line class="secondary" x1="472" y1="25" x2="514" y2="25"/>','<text class="legend" x="526" y="30">field hᵢ</text>']; save("spatial-field-response.svg",a)

if __name__ == "__main__":
    magnetization(); correlation(); correlation_length(); susceptibility(); spatial_response()
