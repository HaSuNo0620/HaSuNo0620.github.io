"""Regenerate elliptic-function diagrams using the shared site SVG helpers."""
from math import sin, cos, sqrt, pi
from concept_schematics import label, line, arrow, circle, curve, poly, save

def sample(f,a,b,n=180):
    return [f(a+(b-a)*i/n) for i in range(n+1)]

def ellipse():
    p=[]
    for cx,a,b,name in [(185,112,112,"円"),(565,145,82,"楕円")]:
        cy=170
        X=lambda t:cx+a*sin(t)
        Y=lambda t:cy-b*cos(t)
        p.extend([line(cx-a-17,cy,cx+a+17,cy,"muted",1.3,"4 5"),
                  line(cx,cy-b-17,cx,cy+b+17,"muted",1.3,"4 5"),
                  poly(sample(X,0,2*pi),sample(Y,0,2*pi),"ink",2.5),
                  label(cx,30,name,"middle",23)])
        for j in range(12):
            t=j*pi/6
            p.append(circle(X(t),Y(t),4,"ink","var(--paper)",1.5))
        for t in [0,pi/3]:
            p.append(poly(sample(X,t,t+pi/6),sample(Y,t,t+pi/6),"accent",5))
        p.append(label(cx,315,"等しい角度差 Δφ","middle",19))
        p.append(label(cx,345,"弧長は等しい" if a==b else "弧長は位置によって異なる","middle",18))
    save("mathematics/ellipse-arc.svg",p,370)

def lemniscate():
    p=[]
    cx,cy,scale=380,195,245
    p.extend([line(105,cy,655,cy,"muted",1.5,"4 5"),line(cx,55,cx,335,"muted",1.5,"4 5")])
    for shift in [0,pi]:
        X=lambda t:cx+scale*sqrt(max(0,cos(2*t)))*cos(t+shift)
        Y=lambda t:cy-scale*sqrt(max(0,cos(2*t)))*sin(t+shift)
        p.append(poly(sample(X,-pi/4,pi/4),sample(Y,-pi/4,pi/4),"ink",2.8))
    t=.42
    X=lambda q:cx+scale*sqrt(max(0,cos(2*q)))*cos(q)
    Y=lambda q:cy-scale*sqrt(max(0,cos(2*q)))*sin(q)
    p.append(poly(sample(X,t,pi/4),sample(Y,t,pi/4),"accent",5))
    x,y=X(t),Y(t)
    p.extend([line(cx,cy,x,y,"green",3,"7 5"),circle(x,y,5,"accent","var(--accent)",1),
              label((cx+x)/2+5,(cy+y)/2+24,"r","middle",22),
              label(450,62,"弧長 s","middle",21),line(450,72,437,139,"muted",1.5),
              label(cx-12,cy+28,"O","end",18),label(630,cy+28,"1","middle",18),
              label(380,360,"r² = cos 2θ","middle",23)])
    save("mathematics/lemniscate-arc.svg",p,390)

def lattice():
    p=[]
    x0,y0=115,293
    a,b=(105,0),(40,-75)
    P=lambda i,j:(x0+i*a[0]+j*b[0],y0+i*a[1]+j*b[1])
    for i in range(5):
        p.append(line(*P(i,0),*P(i,3),"line",1.6))
    for j in range(4):
        p.append(line(*P(0,j),*P(4,j),"line",1.6))
    pts=[P(1,1),P(2,1),P(2,2),P(1,2)]
    p.append(curve("M "+" L ".join(f"{x},{y}" for x,y in pts)+" Z","accent",3,"var(--accent)",'fill-opacity=".12"'))
    for i in range(5):
        for j in range(4):
            p.append(circle(*P(i,j),4,"ink","var(--ink)",0))
    ox,oy=P(1,1)
    p.extend([arrow(ox,oy,*P(2,1),"accent"),arrow(ox,oy,*P(1,2),"green"),
              label(ox+52,oy+25,"ω₁","middle",21),label(ox-8,oy-40,"ω₂","end",21),
              label(380,340,"対辺を同一視 → 複素トーラス","middle",20),
              label(380,373,"格子点は ℘ の二位の極","middle",19)])
    save("mathematics/period-lattice.svg",p,400)

def connections():
    p=[]
    # Three construction routes and their explicit common algebraic relation.
    for x,name,sub in [(130,"Jacobi","楕円・角度の再設定"),(380,"Gauss","レムニスケートの弧長"),(630,"Weierstrass","複素周期格子")]:
        p.extend([label(x,35,name,"middle",24),label(x,66,sub,"middle",18)])
    p.extend([label(130,112,"sn, cn, dn","middle",22),label(380,112,"sl","middle",22),label(630,112,"℘, ℘′","middle",22),
              arrow(245,105,290,105,"green"),arrow(515,105,470,105,"muted"),
              arrow(130,130,130,185,"accent"),arrow(380,130,380,185,"accent"),arrow(630,130,630,185,"accent"),
              label(130,210,"四次式","middle",21),label(380,210,"特殊な四次式","middle",21),label(630,210,"三次式","middle",21),
              label(130,243,"(1−s²)(1−k²s²)","middle",19),label(380,243,"1−r⁴","middle",21),label(630,243,"4x³−g₂x−g₃","middle",21),
              arrow(130,260,130,290,"muted"),arrow(380,260,380,290,"muted"),arrow(630,260,630,290,"muted"),
              line(130,290,630,290,"muted",2),arrow(380,290,380,325,"accent"),
              label(380,355,"楕円積分・複素トーラス・楕円曲線","middle",22)])
    save("mathematics/elliptic-unification.svg",p,390)

if __name__=="__main__":
    ellipse()
    lemniscate()
    lattice()
    connections()
