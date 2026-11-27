"""Editorial diagrams for quantum, mathematics and economics notes.
The figures are explanatory schematics, not measured data.
"""
from pathlib import Path
from math import sin, cos, pi, tanh, exp, sqrt
from xml.sax.saxutils import escape
from xml.etree import ElementTree as ET
from figure_style import COLORS, DARK_COLORS

OUT=Path(__file__).resolve().parents[1]/"public"/"figures"

def label(x,y,s,anchor="start",size=19,role="ink"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="var(--{role})">{escape(s)}</text>'
def line(x,y,X,Y,role="ink",width=2,dash=""):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" stroke="var(--{role})" stroke-width="{width}"{d}/>'
def arrow(x,y,X,Y,role="ink",width=3):
    from math import atan2
    t=atan2(Y-y,X-x)
    pts=[(X,Y),(X-12*cos(t-.42),Y-12*sin(t-.42)),(X-12*cos(t+.42),Y-12*sin(t+.42))]
    return line(x,y,X,Y,role,width)+f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in pts)}" fill="var(--{role})"/>'
def curve(d,role="ink",width=2,fill="none",extra=""):
    return f'<path d="{d}" stroke="var(--{role})" stroke-width="{width}" fill="{fill}" {extra}/>'
def circle(x,y,r,role="ink",fill="none",width=2,extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="var(--{role})" stroke-width="{width}" fill="{fill}" {extra}/>'
def rect(x,y,w,h,role="accent",opacity=.08):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="var(--{role})" fill-opacity="{opacity}"/>'
def poly(xs,ys,role="accent",width=3,dash=""):
    d="M "+" L ".join(f"{x:.2f},{y:.2f}" for x,y in zip(xs,ys))
    return curve(d,role,width,extra=f'stroke-dasharray="{dash}"' if dash else "")
def save(name,parts,h=440):
    def palette(p): return ";".join(f"--{k}:{v}" for k,v in p.items())
    style=f':root{{{palette(COLORS)}}}@media(prefers-color-scheme:dark){{:root{{{palette(DARK_COLORS)}}}}}text{{font-family:"Noto Sans JP","Hiragino Sans","Yu Gothic",sans-serif}}'
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{h}" viewBox="0 0 760 {h}" role="img"><style>{style}</style>{"".join(parts)}</svg>'
    ET.fromstring(svg)
    dest=OUT/name
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(svg,encoding="utf-8")

def xxz():
    p=[]
    # The horizontal axis is Delta. The middle panel represents correlations,
    # not a classical spin configuration.
    for x,w,r in [(32,190,"muted"),(222,316,"accent"),(538,190,"green")]:
        p.append(rect(x,58,w,249,r,.10))
    p.extend([label(127,92,"易軸強磁性","middle",23),label(380,92,"Luttinger液体","middle",25),label(633,92,"Néel秩序","middle",23)])
    for xs,signs,r in [([63+26*i for i in range(6)],[1]*6,"ink"),([570+26*i for i in range(6)],[(-1)**i for i in range(6)],"green")]:
        for x,s in zip(xs,signs):
            p.append(circle(x,164,4,r,f"var(--{r})",0))
            p.append(arrow(x,164+23*s,x,164-25*s,r,2.4))
    # Illustrative power-law envelope of staggered correlations.
    xs=[251+i*2.0 for i in range(130)]
    ys=[175-52*cos(pi*i/11)/(1+i/8)**.65 for i in range(130)]
    p.append(line(250,175,511,175,"muted",1.3,"3 5"))
    p.append(poly(xs,ys,"accent",3))
    p.extend([label(127,243,"ギャップあり","middle",18),label(380,243,"べき減衰する相関","middle",20),label(633,243,"ギャップあり","middle",18)])
    p.append(label(380,269,"ギャップレス","middle",18))
    p.append(arrow(28,329,733,329,"ink",2.2))
    for x,txt in [(222,"−1"),(380,"0"),(538,"1")]:
        p.append(line(x,315,x,344,"ink",1.6))
        p.append(label(x,366,txt,"middle",21))
    p.append(label(730,365,"Δ","middle",22))
    p.append(label(222,401,"強磁性境界","middle",17))
    p.append(label(380,401,"XX点","middle",17))
    p.append(label(538,401,"BKT転移点","middle",17))
    p.append(label(380,29,"J > 0・零温度・零磁場","middle",18,"muted"))
    save("xxz/phase-structure.svg",p,430)

def asymptotic():
    p=[]
    # Four distinct graphical failure modes on shared visual grammar.
    for x,y in [(28,32),(395,32),(28,258),(395,258)]:
        p.append(line(x,y+186,x+335,y+186,"line",1.4))
    p.append(label(28,55,"正則摂動",size=23))
    p.append(label(395,55,"境界層",size=23))
    p.append(label(28,281,"WKB・転回点",size=23))
    p.append(label(395,281,"多重尺度",size=23))
    xs=[48+3*i for i in range(94)]
    for e,r,d in [(0,"muted","5 5"),(.18,"accent","")]:
        p.append(poly(xs,[145-25*sin(i/23)-e*90*(i/93)**2 for i in range(94)],r,3,d))
    p.append(label(48,202,"小さな変化が全域で小さい",size=17))
    xs=[415+3*i for i in range(94)]
    p.append(rect(415,76,29,87,"accent",.12))
    p.append(poly(xs,[84]*94,"muted",2.5,"6 5"))
    p.append(poly(xs,[84+72*exp(-i/6) for i in range(94)],"accent",3))
    p.append(label(415,202,"狭い領域で微分項が競合",size=17))
    xs=[48+3*i for i in range(94)]
    p.append(line(48,368,327,368,"muted",1.2,"3 4"))
    p.append(rect(176,303,36,104,"accent",.12))
    # Oscillatory to exponential schematic, not an Airy solution.
    ys=[368-28*cos(1.0*((45-i)/5)**1.5) if i<=45 else 368-28*exp(-(i-45)/11) for i in range(94)]
    p.append(poly(xs,ys,"accent",3))
    p.append(line(183,301,183,414,"muted",1.5,"4 4"))
    p.append(label(183,320,"Q = 0","middle",16))
    p.append(label(48,431,"局所波長の尺度分離が失われる",size=17))
    xs=[415+3*i for i in range(94)]
    p.append(poly(xs,[368-30*cos(i*.28) for i in range(94)],"muted",2,"5 4"))
    p.append(poly(xs,[368-30*cos(i*.30) for i in range(94)],"accent",3))
    p.append(label(415,431,"微小な周波数差が累積する",size=17))
    save("mathematics/asymptotic-scales.svg",p,470)

def elliptic():
    p=[]
    # Spatially distinct representations, with explicit meanings of arrows.
    p.append(label(126,31,"非線形振り子","middle",23))
    p.append(line(93,64,159,64,"ink",3))
    p.append(line(126,64,126,151,"muted",1.5,"4 5"))
    p.append(curve("M 65,127 A 87,87 0 0 0 187,127","muted",1.5,extra='stroke-dasharray="5 5"'))
    p.append(line(126,64,187,126,"accent",3))
    p.append(circle(187,126,11,"accent","var(--accent)",0))
    p.append(label(126,190,"エネルギー保存","middle",17))
    p.append(arrow(230,105,300,105,"ink",2.6))
    p.append(label(266,88,"積分","middle",16))
    p.append(label(489,31,"第一種楕円積分","middle",23))
    p.append(label(489,102,"u = ∫ ds / √[(1−s²)(1−k²s²)]","middle",20))
    p.append(arrow(489,126,489,190,"accent",2.8))
    p.append(label(505,164,"逆関数",size=17))
    p.append(rect(306,202,366,65,"accent",.09))
    p.append(label(489,243,"x = sn(u, k)","middle",26))
    p.append(arrow(389,273,188,323,"ink",2.4))
    p.append(arrow(589,273,645,323,"ink",2.4))
    p.append(label(267,289,"複素解析接続","middle",17))
    p.append(label(643,295,"変数変換","middle",17))
    # Complex fundamental parallelogram.
    x0,y0=80,415
    for i in range(4):
        for j in range(3):
            p.append(circle(x0+52*i+14*j,y0-36*j,3.4,"muted","var(--muted)",0))
    p.append(curve("M 80,415 L 132,415 L 146,379 L 94,379 Z","accent",2.2,"var(--accent)",'fill-opacity=".10"'))
    p.append(label(170,451,"複素周期格子","middle",20))
    # Real slice of nonsingular cubic y^2=4(x+1)x(x-1).
    for sign in [-1,1]:
        for a,b in [(-1,0),(1,1.52)]:
            X=[a+(b-a)*i/100 for i in range(101)]
            Y=[sign*sqrt(max(0,4*(x+1)*x*(x-1))) for x in X]
            p.append(poly([542+59*x for x in X],[390-31*y for y in Y],"green",2.7))
    p.append(line(465,390,662,390,"muted",1.3))
    p.append(label(566,451,"楕円曲線","middle",20))
    p.append(arrow(278,396,447,396,"muted",2.2))
    p.append(label(363,379,"一様化","middle",16))
    save("mathematics/elliptic-connections.svg",p,480)

def choice():
    p=[]
    # p = theta q + Z; plotted values match the table in the article.
    X=lambda q: 94+(q-.5)*263
    Y=lambda price: 343-(price-65)*2.45
    p.append(arrow(94,343,716,343,"ink",2))
    p.append(arrow(94,343,94,41,"ink",2))
    for q in [1,1.5,2]:
        p.append(line(X(q),343,X(q),350,"ink",1.4))
        p.append(label(X(q),373,f"{q:g}","middle",17))
    for pr in [80,100,120,140,160,180]:
        p.append(line(88,Y(pr),707,Y(pr),"line",1))
        p.append(label(80,Y(pr)+6,str(pr),"end",16))
    for theta,Z,r,d in [(40,60,"muted","6 5"),(60,30,"accent","")]:
        qs=[.5+i*2.3/100 for i in range(101)]
        p.append(poly([X(q) for q in qs],[Y(theta*q+Z) for q in qs],r,3,d))
    # Each line indicates an actual minimum Z among the three products.
    for name,q,price in [("A",1,100),("B",1.5,120),("C",2,150)]:
        p.append(circle(X(q),Y(price),6,"ink","var(--paper)",2.4))
        p.append(label(X(q)+13,Y(price)-10,name,size=22))
    p.append(label(570,64,"θ = 60",size=19,role="accent"))
    p.append(label(585,133,"θ = 40",size=19,role="muted"))
    p.append(label(400,411,"品質 q","middle",21))
    p.append(label(32,31,"価格 p",size=20))
    p.append(label(380,26,"直線上では品質調整価格 Z が等しい","middle",18))
    save("economics/quality-adjusted-price.svg",p,440)

def diversion():
    p=[]
    p.append(rect(30,52,456,326,"accent",.06))
    p.append(rect(505,52,225,326,"green",.06))
    p.append(label(50,83,"企業A","start",23))
    p.append(label(525,83,"企業外","start",23))
    nodes=[(145,129,"Basic"),(145,291,"Pro"),(363,210,"Standard"),(616,129,"競合商品"),(616,291,"非購入")]
    for x,y,name in nodes:
        p.append(f'<rect x="{x-75}" y="{y-24}" width="150" height="48" rx="8" fill="var(--paper)" stroke="var(--line)" stroke-width="1.8"/>')
        p.append(label(x,y+7,name,"middle",20))
    p.append(arrow(288,195,220,145,"accent",4))
    p.append(arrow(288,225,220,275,"accent",3))
    p.append(label(255,151,"40%","middle",17,"accent"))
    p.append(label(255,279,"20%","middle",17,"accent"))
    p.append(arrow(438,195,541,145,"green",3))
    p.append(arrow(438,225,541,275,"green",3))
    p.append(label(490,151,"流出","middle",17))
    p.append(label(490,279,"流出","middle",17))
    p.append(label(258,352,"自社内移転 60%","middle",19))
    p.append(label(617,352,"残り 40%","middle",19))
    p.append(label(380,23,"Standardの値上げで失われた需要","middle",20))
    p.append(label(380,414,"例示の流出率。企業内での移転は利幅で重みづける。","middle",18))
    save("economics/ownership-diversion.svg",p,440)

if __name__=="__main__":
    xxz()
    asymptotic()
    elliptic()
    choice()
    diversion()
