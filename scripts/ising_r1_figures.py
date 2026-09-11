"""Regenerate the R=1 Ising figures using Figure Style v1.4.

SVG labels mimic mathematical typesetting semantically: variable identifiers are
italic, while numerals, operators, punctuation, constants, and prose remain
upright. MathJax cannot typeset text inside an SVG loaded through <img>, so the
roles are represented with SVG <tspan> elements instead.
"""
from __future__ import annotations

import html
import math
from pathlib import Path

from figure_style import COLORS, DARK_COLORS

OUT = Path(__file__).resolve().parents[1] / "public" / "figures" / "ising-r1"
W, H = 760, 440
KVALS = (0.4, 0.8, 1.2, 1.8)
STYLES = ("muteddot", "inkdash", "primary", "secondary")

STYLE = f"""<style>
.axis{{stroke:{COLORS["ink"]};stroke-width:1.8}}
.grid{{stroke:{COLORS["line"]};stroke-width:1.1;opacity:.48}}
.tick{{fill:{COLORS["muted"]};font:16px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.textlabel{{fill:{COLORS["ink"]};font:19px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.mathlabel{{fill:{COLORS["ink"]};font-family:"STIX Two Math","Cambria Math","Times New Roman",serif;font-size:20px;font-style:normal}}
.legend{{fill:{COLORS["ink"]};font:18px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.mathlegend{{fill:{COLORS["ink"]};font-family:"STIX Two Math","Cambria Math","Times New Roman",serif;font-size:18px;font-style:normal}}
.legendbox{{fill:{COLORS["paper"]};fill-opacity:.92;stroke:{COLORS["ink"]};stroke-opacity:.14;stroke-width:1}}
.panel{{fill:{COLORS["ink"]};font:600 18px system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.panelmath{{fill:{COLORS["ink"]};font-family:"STIX Two Math","Cambria Math","Times New Roman",serif;font-size:18px;font-style:normal}}
.mi{{font-style:italic}}
.mo,.mn,.mconst{{font-style:normal}}
.primary{{fill:none;stroke:{COLORS["accent"]};stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round}}
.secondary{{fill:none;stroke:{COLORS["green"]};stroke-width:3.6;stroke-dasharray:10 7;stroke-linecap:round;stroke-linejoin:round}}
.inkdash{{fill:none;stroke:{COLORS["ink"]};stroke-width:3.6;stroke-dasharray:9 7;opacity:.84}}
.muteddot{{fill:none;stroke:{COLORS["muted"]};stroke-width:3.6;stroke-dasharray:3.5 5.5;opacity:.94}}
@media(prefers-color-scheme:dark){{
.axis{{stroke:{DARK_COLORS["ink"]}}}.grid{{stroke:{DARK_COLORS["line"]}}}
.tick{{fill:{DARK_COLORS["muted"]}}}
.textlabel,.mathlabel,.legend,.mathlegend,.panel,.panelmath{{fill:{DARK_COLORS["ink"]}}}
.legendbox{{fill:{DARK_COLORS["paper"]};stroke:{DARK_COLORS["ink"]}}}
.primary{{stroke:{DARK_COLORS["accent"]}}}.secondary{{stroke:{DARK_COLORS["green"]}}}
.inkdash{{stroke:{DARK_COLORS["ink"]}}}.muteddot{{stroke:{DARK_COLORS["muted"]}}}
}}
</style>"""


def mp(v, a, b, c, d):
    return c + (v - a) / (b - a) * (d - c)


def line(points, cls):
    return f'<polyline class="{cls}" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in points) + '"/>'


def span(text: str, role: str = "mo") -> str:
    return f'<tspan class="{role}">{html.escape(text)}</tspan>'


def math_markup(parts) -> str:
    return "".join(span(text, role) for role, text in parts)


def math_text(x, y, parts, *, cls="mathlabel", anchor=None, transform=None):
    attrs = [f'class="{cls}"', f'x="{x}"', f'y="{y}"']
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if transform:
        attrs.append(f'transform="{transform}"')
    return f'<text {" ".join(attrs)}>{math_markup(parts)}</text>'


def wrap(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{STYLE}\n{body}\n</svg>\n'


def save(name, parts):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(wrap("\n".join(parts)), encoding="utf-8")


def axes(xmin, xmax, ymin, ymax, xticks, yticks, xlabel, ylabel, left=96, right=716, top=30, bottom=346):
    a = []
    for x in xticks:
        X = mp(x, xmin, xmax, left, right)
        a += [f'<line class="grid" x1="{X:.1f}" y1="{top}" x2="{X:.1f}" y2="{bottom}"/>', f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y in yticks:
        Y = mp(y, ymin, ymax, bottom, top)
        a += [f'<line class="grid" x1="{left}" y1="{Y:.1f}" x2="{right}" y2="{Y:.1f}"/>', f'<text class="tick" x="{left-14}" y="{Y+5:.1f}" text-anchor="end">{y:g}</text>']
    a += [
        f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',
        f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>',
        math_text(406, 420, xlabel, anchor="middle"),
        math_text(27, 188, ylabel, anchor="middle", transform="rotate(-90 27 188)"),
    ]
    return a, (left, right, top, bottom)


def add_legend(a):
    a.append('<rect class="legendbox" x="500" y="24" width="196" height="132" rx="10"/>')
    for i, (K, cl) in enumerate(zip(KVALS, STYLES)):
        y = 48 + 30 * i
        a += [
            f'<line class="{cl}" x1="526" y1="{y}" x2="578" y2="{y}"/>',
            math_text(592, y + 6, [("mi", "β"), ("mi", "J"), ("mo", " = "), ("mn", f"{K:.1f}")], cls="mathlegend"),
        ]


def magnetization():
    a, b = axes(-2.5,2.5,-1.05,1.05,[-2,-1,0,1,2],[-1,-.5,0,.5,1],[("mi","h"),("mo"," / "),("mi","J")],[("mi","m")])
    l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        pts=[]
        for i in range(101):
            x=-2.5+5*i/100; bh=K*x
            m=math.sinh(bh)/math.sqrt(math.sinh(bh)**2+math.exp(-4*K))
            pts.append((mp(x,-2.5,2.5,l,r),mp(m,-1.05,1.05,bo,t)))
        a.append(line(pts,cl))
    add_legend(a); save("magnetization-field.svg",a)


def correlation():
    a,b=axes(0,30,0,1.02,[0,5,10,15,20,25,30],[0,.25,.5,.75,1],[("mi","r")],[("mi","C"),("mo","("),("mi","r"),("mo",")")])
    l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        q=math.tanh(K)
        a.append(line([(mp(i,0,30,l,r),mp(q**i,0,1.02,bo,t)) for i in range(31)],cl))
    add_legend(a); save("correlation-distance.svg",a)


def susceptibility():
    a,b=axes(0,1,0,1.02,[0,.25,.5,.75,1],[0,.25,.5,.75,1],[("mi","q"),("mo"," / "),("mconst","π")],[("mi","χ"),("mo","("),("mi","q"),("mo",") / "),("mi","χ"),("mo","("),("mn","0"),("mo",")")])
    l,r,t,bo=b
    for K,cl in zip(KVALS,STYLES):
        u=math.tanh(K); c0=K*(1-u*u)/(1-2*u+u*u); pts=[]
        for i in range(101):
            q=math.pi*i/100; c=K*(1-u*u)/(1-2*u*math.cos(q)+u*u)
            pts.append((mp(i/100,0,1,l,r),mp(c/c0,0,1.02,bo,t)))
        a.append(line(pts,cl))
    add_legend(a); save("susceptibility-q.svg",a)


def correlation_length():
    l,r,t,bo=102,716,30,346; a=[]; xmin,xmax=.25,4; ylo,yhi=-1,3.2
    for x in [.5,1,2,3,4]:
        X=mp(x,xmin,xmax,l,r); a += [f'<line class="grid" x1="{X:.1f}" y1="{t}" x2="{X:.1f}" y2="{bo}"/>',f'<text class="tick" x="{X:.1f}" y="378" text-anchor="middle">{x:g}</text>']
    for y,lab in [(.1,"10⁻¹"),(1,"1"),(10,"10"),(100,"10²"),(1000,"10³")]:
        Y=mp(math.log10(y),ylo,yhi,bo,t); a += [f'<line class="grid" x1="{l}" y1="{Y:.1f}" x2="{r}" y2="{Y:.1f}"/>',f'<text class="tick" x="{l-14}" y="{Y+5:.1f}" text-anchor="end">{lab}</text>']
    a += [f'<line class="axis" x1="{l}" y1="{t}" x2="{l}" y2="{bo}"/>',f'<line class="axis" x1="{l}" y1="{bo}" x2="{r}" y2="{bo}"/>',math_text(409,420,[("mi","T"),("mo"," / "),("mi","J")],anchor="middle"),math_text(29,188,[("mi","ξ")],anchor="middle",transform="rotate(-90 29 188)")]
    ex,ap=[],[]
    for i in range(101):
        T=xmin+(xmax-xmin)*i/100; K=1/T; xi=-1/math.log(math.tanh(K)); xa=.5*math.exp(2*K); X=mp(T,xmin,xmax,l,r)
        ex.append((X,mp(math.log10(xi),ylo,yhi,bo,t))); ap.append((X,mp(math.log10(xa),ylo,yhi,bo,t)))
    a += [line(ex,"primary"),line(ap,"secondary"),'<rect class="legendbox" x="446" y="28" width="244" height="82" rx="10"/>','<line class="primary" x1="468" y1="52" x2="526" y2="52"/>','<text class="legend" x="542" y="59">exact</text>','<line class="secondary" x1="468" y1="86" x2="526" y2="86"/>','<text class="legend" x="542" y="93">low-T asymptote</text>']
    save("correlation-length-temperature.svg",a)


def spatial_response():
    a=[]; pls,prs=[80,422],[346,688]; pt,pb=60,334; ymin,ymax=-.19,.19
    for idx,(pl,pr,q) in enumerate(zip(pls,prs,[math.pi/10,math.pi/2])):
        for y in [-.1,0,.1]:
            Y=mp(y,ymin,ymax,pb,pt); a.append(f'<line class="grid" x1="{pl}" y1="{Y:.1f}" x2="{pr}" y2="{Y:.1f}"/>')
            if idx==0: a.append(f'<text class="tick" x="{pl-12}" y="{Y+5:.1f}" text-anchor="end">{y:g}</text>')
        for i in [0,10,20,30,40]:
            X=mp(i,0,40,pl,pr); a += [f'<line class="grid" x1="{X:.1f}" y1="{pt}" x2="{X:.1f}" y2="{pb}"/>',f'<text class="tick" x="{X:.1f}" y="366" text-anchor="middle">{i}</text>']
        denom="10" if idx==0 else "2"
        a += [f'<line class="axis" x1="{pl}" y1="{pt}" x2="{pl}" y2="{pb}"/>',f'<line class="axis" x1="{pl}" y1="{pb}" x2="{pr}" y2="{pb}"/>',f'<text class="panel" x="{pl+8}" y="{pt+22}">({"ab"[idx]})</text>',math_text(pl+44,pt+22,[("mi","q"),("mo"," = "),("mconst","π"),("mo","/"),("mn",denom)],cls="panelmath"),math_text((pl+pr)/2,410,[("mi","i")],anchor="middle")]
        if idx==0: a.append(math_text(24,196,[("mi","hᵢ"),("mo"," , ⟨"),("mi","sᵢ"),("mo","⟩")],anchor="middle",transform="rotate(-90 24 196)"))
        K=1.2; u=math.tanh(K); chi=K*(1-u*u)/(1-2*u*math.cos(q)+u*u); field,resp=[],[]
        for i in range(41):
            X=mp(i,0,40,pl,pr); c=math.cos(q*i); field.append((X,mp(.05*c,ymin,ymax,pb,pt))); resp.append((X,mp(chi*.05*c,ymin,ymax,pb,pt)))
        a += [line(resp,"primary"),line(field,"secondary")]
    a += ['<rect class="legendbox" x="152" y="8" width="456" height="38" rx="10"/>','<line class="primary" x1="174" y1="27" x2="230" y2="27"/>','<text class="legend" x="244" y="33">response</text>',math_text(323,33,[("mo","⟨"),("mi","sᵢ"),("mo","⟩")],cls="mathlegend"),'<line class="secondary" x1="454" y1="27" x2="510" y2="27"/>','<text class="legend" x="524" y="33">field</text>',math_text(570,33,[("mi","hᵢ")],cls="mathlegend")]
    save("spatial-field-response.svg",a)


if __name__ == "__main__":
    magnetization(); correlation(); correlation_length(); susceptibility(); spatial_response()
