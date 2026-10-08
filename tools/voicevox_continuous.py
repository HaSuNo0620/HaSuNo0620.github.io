#!/usr/bin/env python3
"""Continuous BKT explainer: sparse orientational field on a neutral canvas.

Time is measured on the *final* WAV timeline; this renderer never muxes
individual scene audio. The curved lines are illustrative spin orientations,
not flow trajectories or Monte Carlo output.
"""
import argparse
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W,H,FPS=960,540,24
FONT="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
MOTIONS={"phase_field_intro","phase_smooth_lowT","zoom_to_vortex",
         "vortex_with_streamlines","vortex_antivortex_pair",
         "pair_unbinding","correlation_compare"}

def phase(x,y,motion,p,global_time):
    sway=.12*math.sin(.55*x+.35*global_time)+.1*math.cos(.65*y-.22*global_time)
    if motion in ("phase_field_intro","phase_smooth_lowT"):
        return .19*x+.15*y+sway
    if motion in ("zoom_to_vortex","vortex_with_streamlines"):
        return math.atan2(y,x)+.15*sway
    if motion in ("vortex_antivortex_pair","pair_unbinding"):
        sep=.6 if motion=="vortex_antivortex_pair" else .35+1.18*p
        return math.atan2(y,x+sep)-math.atan2(y,x-sep)+.12*sway
    return .2*x+.1*y+sway

def ease(t):
    t=max(0.,min(1.,t))
    return t*t*(3-2*t)

def cue_at(t,cues):
    for i,c in enumerate(cues):
        if t < c["end"] or i==len(cues)-1:
            return i,c
    return len(cues)-1,cues[-1]

def two_lines(draw,text,font,width):
    result=[];buffer=""
    for char in text:
        if draw.textbbox((0,0),buffer+char,font=font)[2]>width and buffer:
            result.append(buffer);buffer=char
        else:buffer+=char
    if buffer:result.append(buffer)
    return result[:2]

def render_scene(t,cues,show_subtitle=True,forced_idx=None):
    idx,c=cue_at(t,cues) if forced_idx is None else (forced_idx,cues[forced_idx])
    motion=c["motion"]
    p=ease((t-c["start"])/max(.01,c["end"]-c["start"])) if forced_idx is None else 1.0
    image=Image.new("RGB",(W,H),"#0e1724")
    d=ImageDraw.Draw(image)
    f=ImageFont.truetype(FONT,25)
    fs=ImageFont.truetype(FONT,19)
    # No hue flood fill: spin direction is encoded by geometric line direction.
    # Open on the finite lattice, then inspect topological defects at wider view.
    xmin,xmax=-3.15,3.15
    ymin,ymax=-1.8,1.8
    centers=[]
    if motion in ("zoom_to_vortex","vortex_with_streamlines"):
        centers=[(0.,0.,1)]
    elif motion in ("vortex_antivortex_pair","pair_unbinding"):
        sep=.6 if motion=="vortex_antivortex_pair" else .35+1.18*p
        centers=[(-sep,0.,1),(sep,0.,-1)]
    def xp(x):return (x-xmin)/(xmax-xmin)*(W-90)+45
    def yp(y):return (y-ymin)/(ymax-ymin)*(H-135)+42
    # Faint lattice grid gives scale, rather than a decorative color field.
    for x in np.arange(-3.0,3.01,.36):
        d.line((xp(x),yp(ymin),xp(x),yp(ymax)),fill="#1b2d3f",width=1)
    for y in np.arange(-1.8,1.81,.36):
        d.line((xp(xmin),yp(y),xp(xmax),yp(y)),fill="#1b2d3f",width=1)
    for y in np.arange(-1.65,1.7,.36):
        for x in np.arange(-3.0,3.1,.36):
            a=phase(x,y,motion,p,t)
            cx,cy=xp(x),yp(y)
            ll=11
            dx=ll*math.cos(a);dy=ll*math.sin(a)
            col="#90cdd2" if not centers else "#abc5d8"
            d.line((cx-dx,cy-dy,cx+dx,cy+dy),fill=col,width=3)
            d.line((cx+dx,cy+dy,cx+dx-5*math.cos(a-.6),cy+dy-5*math.sin(a-.6)),fill=col,width=2)
            d.line((cx+dx,cy+dy,cx+dx-5*math.cos(a+.6),cy+dy-5*math.sin(a+.6)),fill=col,width=2)
    for x,y,charge in centers:
        cx,cy=xp(x),yp(y)
        radius=30 if motion=="zoom_to_vortex" else 47
        outline="#ffbe76" if charge==1 else "#8db5ff"
        d.ellipse((cx-radius,cy-radius,cx+radius,cy+radius),outline=outline,width=3)
        d.ellipse((cx-7,cy-7,cx+7,cy+7),fill=outline)
        d.text((cx+radius+9,cy-18),"m=+1" if charge==1 else "m=−1",font=fs,fill=outline)
    if motion=="vortex_with_streamlines":
        cx,cy=xp(0),yp(0)
        d.arc((cx-88,cy-88,cx+88,cy+88),20,330,fill="#ffbe76",width=4)
        d.text((42,58),"閉曲線に沿って角度が 2π 回転",font=f,fill="#fff")
    if motion=="pair_unbinding":
        d.text((42,55),"模式図：渦対の解離",font=f,fill="#f0f4fc")
    if motion=="correlation_compare":
        d.rounded_rectangle((180,75,810,395),radius=22,fill="#162637")
        d.line((240,110,240,350,760,350),fill="#e4ecf3",width=2)
        power=[];exp=[]
        for i in range(0,190):
            r=1+i/30
            power.append((245+i*2.6,340-205*r**(-.25)))
            exp.append((245+i*2.6,340-205*math.exp(-(r-1)/1.6)))
        d.line(power,fill="#75d9c5",width=4)
        d.line(exp,fill="#ffa572",width=4)
        d.text((490,130),"代数減衰",font=f,fill="#75d9c5")
        d.text((560,264),"指数減衰",font=f,fill="#ffa572")
    # Persistent semantic explanation, deliberately not a title-card.
    label="矢印 = スピンの向き  θ"
    d.text((35,12),label,font=fs,fill="#e0e9f5")
    # Fade the label? Keep it readable throughout; context is more important.
    if show_subtitle:
        draw_subtitle(image,c.get("subtitle",""))
    return image

def draw_subtitle(image,text):
    d=ImageDraw.Draw(image)
    font=ImageFont.truetype(FONT,25)
    d.rounded_rectangle((38,H-107,W-38,H-18),radius=14,fill="#07101a")
    lines=two_lines(d,text,font,W-108)
    for n,line in enumerate(lines):
        tw=d.textbbox((0,0),line,font=font)[2]
        d.text(((W-tw)/2,H-100+36*n),line,font=font,fill="#ffffff")

def render(t,cues):
    idx,c=cue_at(t,cues)
    current=render_scene(t,cues,show_subtitle=False)
    if idx>0:
        blend_seconds=min(0.9,max(0.15,(c["end"]-c["start"])*0.22))
        elapsed=t-c["start"]
        if elapsed<blend_seconds:
            previous=render_scene(c["start"],cues,show_subtitle=False,forced_idx=idx-1)
            current=Image.blend(previous,current,ease(elapsed/blend_seconds))
    draw_subtitle(current,c.get("subtitle",""))
    return current

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--timeline",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    timeline=json.loads(Path(args.timeline).read_text(encoding="utf-8"))
    cues=timeline["cues"]
    for c in cues:
        if c["motion"] not in MOTIONS:raise ValueError("Unknown motion")
    total=float(timeline["duration"])
    frames=math.ceil(total*FPS)
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo",
         "-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
         "-an","-c:v","libx264","-preset","veryfast","-crf","24","-pix_fmt","yuv420p",
         "-t",str(total),str(args.output)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for i in range(frames):
            proc.stdin.write(render(i/FPS,cues).tobytes())
        proc.stdin.close()
        if proc.wait()!=0:raise RuntimeError("ffmpeg video encoding failed")
    finally:
        if proc.poll() is None:proc.kill();proc.wait()
if __name__=="__main__":main()
