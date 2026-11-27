"""Editorial interface schematics; geometry is illustrative, not simulation data."""
from pathlib import Path
from math import sin, cos, pi, tanh
from xml.sax.saxutils import escape
from xml.etree import ElementTree as ET
from figure_style import COLORS, DARK_COLORS

OUT=Path(__file__).resolve().parents[1]/"public"/"figures"/"interfaces"
def label(x,y,s,anchor="start",size=19):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="var(--ink)">{escape(s)}</text>'
def line(x,y,X,Y,role="ink",width=2,dash=""):
    return f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" stroke="var(--{role})" stroke-width="{width}" {f"stroke-dasharray={chr(34)}{dash}{chr(34)}" if dash else ""}/>'
def arrow(x,y,X,Y,role="ink",width=3):
    # Directly constructed arrowhead keeps its color with the shaft.
    from math import atan2
    t=atan2(Y-y,X-x)
    pts=[(X,Y),(X-12*cos(t-.42),Y-12*sin(t-.42)),(X-12*cos(t+.42),Y-12*sin(t+.42))]
    return line(x,y,X,Y,role,width)+f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in pts)}" fill="var(--{role})"/>'
def path(d,role="ink",width=2,fill="none",extra=""):
    return f'<path d="{d}" stroke="var(--{role})" stroke-width="{width}" fill="{fill}" {extra}/>'
def circle(x,y,r,role="ink",fill="none",width=2,extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="var(--{role})" stroke-width="{width}" fill="{fill}" {extra}/>'
def save(name,parts,h=440):
    def palette(p): return ";".join(f"--{k}:{v}" for k,v in p.items())
    style=f':root{{{palette(COLORS)}}}@media(prefers-color-scheme:dark){{:root{{{palette(DARK_COLORS)}}}}}text{{font-family:"Noto Sans JP","Hiragino Sans","Yu Gothic",sans-serif}}'
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{h}" viewBox="0 0 760 {h}" role="img"><style>{style}</style>{"".join(parts)}</svg>'
    ET.fromstring(svg)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/name).write_text(svg,encoding="utf-8")

def young_laplace():
    # Hemisphere cross-section: forces on the upper half are vertical in total.
    p=[]
    p.append(path("M 76,280 A 150,150 0 0 1 376,280 L 76,280 Z","accent",2,"var(--accent)",'fill-opacity=".09"'))
    p.append('<ellipse cx="226" cy="280" rx="150" ry="38" fill="var(--accent)" fill-opacity=".09" stroke="var(--accent)" stroke-width="2.4"/>')
    p.append(path("M 76,280 A 150,150 0 0 1 376,280","accent",3))
    p.append(line(226,280,376,280,"muted",1.8,"5 5"))
    p.append(label(299,268,"R","middle"))
    for x in [100,160,226,292,352]:
        p.append(arrow(x,300,x,247,"green",3))
    # Rim tangent force of lower hemisphere on upper hemisphere points downward.
    for x in [76,376]:
        p.append(arrow(x,280,x,357,"accent",4))
    p.append(label(226,397,"赤道面に作用する力","middle",18))
    p.append(label(226,177,"内相 α","middle",21))
    p.append(label(40,93,"外相 β"))
    p.append(line(438,67,438,373,"line",1.5))
    p.append(label(476,100,"圧力差による力",size=20))
    p.append(arrow(493,162,493,124,"green",4))
    p.append(label(522,148,"Δp · πR²",size=24))
    p.append(label(476,215,"円周に沿う張力の合力",size=20))
    p.append(arrow(493,235,493,273,"accent",4))
    p.append(label(522,265,"2πRγ",size=24))
    p.append(line(476,299,722,299,"line",1.5))
    p.append(label(598,348,"Δp = 2γ/R","middle",27))
    save("young-laplace-hemisphere.svg",p)

def gibbs():
    p=[]
    x0,x1=88,714
    ytop,ybottom=83,353
    z0=420
    def rho(x): return ytop+(ybottom-ytop)*(1+tanh((x-375)/85))/2
    y=lambda x:rho(x)
    xs=[x0+(x1-x0)*i/300 for i in range(301)]
    def curve(a,b): return " L ".join(f"{x:.2f},{y(x):.2f}" for x in [a]+[x for x in xs if a<x<b]+[b])
    p.append(path(f"M {x0},{ytop} L {z0},{ytop} L "+curve(z0,x0)[0:0]+f"{z0},{y(z0):.2f} L "+" L ".join(f"{x:.2f},{y(x):.2f}" for x in reversed([x for x in xs if x<z0]))+f" L {x0},{y(x0):.2f} Z","accent",0,"var(--accent)",'fill-opacity=".19"'))
    p.append(path(f"M {z0},{ybottom} L {x1},{ybottom} L "+" L ".join(f"{x:.2f},{y(x):.2f}" for x in reversed([x for x in xs if x>z0]))+f" L {z0},{y(z0):.2f} Z","green",0,"var(--green)",'fill-opacity=".20"'))
    p.append(path("M "+curve(x0,x1),"ink",3.6))
    p.append(path(f"M {x0},{ytop} H {z0} V {ybottom} H {x1}","muted",2.4,"none",'stroke-dasharray="8 5"'))
    p.append(line(z0,55,z0,383,"accent",2,"4 5"))
    p.append(arrow(x0,383,727,383))
    p.append(arrow(x0,383,x0,47))
    p.append(label(50,89,"ρᵅ","middle"))
    p.append(label(50,358,"ρᵝ","middle"))
    p.append(label(420,416,"z₀","middle"))
    p.append(label(730,409,"z","middle"))
    p.append(label(92,37,"ρ(z)"))
    p.append(label(252,124,"不足分 (−)","middle"))
    p.append(line(306,131,355,155,"accent",1.5))
    p.append(label(555,311,"過剰分 (+)","middle"))
    p.append(line(510,306,462,318,"green",1.5))
    p.append(label(450,60,"仮想分割面"))
    p.append(label(180,250,"実際の密度分布",size=18))
    p.append(line(322,240,359,193,"ink",1.3))
    save("gibbs-surface-excess.svg",p)

def tolman():
    p=[]
    cx,cy=230,216
    # Illustrative Re > Rs, not a universal sign assumption.
    for r in range(122,164,3):
        opacity=.035*(1-abs(r-143)/24)
        p.append(circle(cx,cy,r,"accent","none",4,f'stroke-opacity="{max(0,opacity):.3f}"'))
    p.append(circle(cx,cy,122,"accent","var(--accent)",0,'fill-opacity=".07"'))
    p.append(circle(cx,cy,135,"accent","none",3.2))
    p.append(circle(cx,cy,154,"green","none",3.2,'stroke-dasharray="9 6"'))
    p.append(circle(cx,cy,3,"ink","var(--ink)",0))
    p.append(arrow(cx,cy,cx+135,cy,"accent",2.7))
    t=-pi/4
    p.append(arrow(cx,cy,cx+154*cos(t),cy+154*sin(t),"green",2.7))
    p.append(label(297,205,"Rₛ","middle",22))
    p.append(label(277,145,"Rₑ","middle",22))
    p.append(line(365,216,405,216,"accent",1.5))
    p.append(line(384,216,405,249,"green",1.5))
    p.append(arrow(365,272,384,272,"ink",2))
    p.append(line(365,250,365,286,"muted",1.4))
    p.append(line(384,250,384,286,"muted",1.4))
    p.append(label(375,308,"δ","middle",22))
    p.append(label(230,407,"液滴断面（模式図）","middle",18))
    p.append(label(456,116,"張力面 Rₛ",size=23))
    p.append(line(456,133,705,133,"accent",3))
    p.append(label(456,163,"Δp = 2γₛ/Rₛ",size=22))
    p.append(label(456,239,"等モル面 Rₑ",size=23))
    p.append(line(456,256,705,256,"green",3,"8 5"))
    p.append(label(456,286,"Nᵟ(Rₑ) = 0",size=22))
    p.append(label(456,358,"δ = Rₑ − Rₛ",size=26))
    save("tolman-dividing-surfaces.svg",p)

def stress_paths():
    p=[]
    for x in (74,402):
        p.append('<rect x="%s" y="74" width="284" height="284" rx="15" fill="var(--accent)" fill-opacity=".035" stroke="var(--line)" stroke-width="1.5"/>'%x)
        for i in range(4):
            for j in range(4):
                xx=x+37+i*70+(j%2)*9
                yy=104+j*70
                if (i,j) in [(0,3),(3,0)]: continue
                p.append(circle(xx,yy,8,"line","var(--line)",0,'fill-opacity=".6"'))
        a=(x+58,295);b=(x+226,130)
        p.append(circle(*a,13,"accent","var(--accent)",0))
        p.append(circle(*b,13,"accent","var(--accent)",0))
        if x==74:
            p.append(path(f"M {a[0]},{a[1]} L {b[0]},{b[1]}","accent",4))
        else:
            p.append(path(f"M {a[0]},{a[1]} H {b[0]} V {b[1]}","green",4,"none",'stroke-dasharray="10 5"'))
        p.append(label(a[0]-20,a[1]+29,"j"))
        p.append(label(b[0]+16,b[1]-13,"i"))
    p.append(label(216,42,"直線経路","middle",23))
    p.append(label(544,42,"折れ線経路","middle",23))
    p.append(label(380,400,"粒子対は同じ。局所への力の配分が異なる。","middle",20))
    save("local-stress-paths.svg",p,440)

if __name__=="__main__":
    young_laplace()
    gibbs()
    tolman()
    stress_paths()
