#!/usr/bin/env python3
"""Immersive XY phase-field animation. Colors encode spin phase, not fluid flow."""
import argparse
import math
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W,H,FPS=1280,720,24
SW,SH=320,180
FONT="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
X,Y=np.meshgrid(np.linspace(-2.7,2.7,SW),np.linspace(-1.52,1.52,SH))
SUPPORTED={"phase_field_intro","phase_smooth_lowT","zoom_to_vortex",
           "vortex_with_streamlines","vortex_antivortex_pair",
           "pair_unbinding","correlation_compare"}

def field(kind,p):
    tt=2*math.pi*p
    slow=.32*np.sin(.85*X+.35*tt)+.23*np.cos(1.25*Y-.22*tt)+.20*np.sin(.53*X+.7*Y)
    if kind in ("phase_field_intro","phase_smooth_lowT"):
        return slow+.27*X
    if kind in ("zoom_to_vortex","vortex_with_streamlines"):
        return np.arctan2(Y,X)+.18*slow
    if kind in ("vortex_antivortex_pair","pair_unbinding"):
        d=.55 if kind=="vortex_antivortex_pair" else .25+1.05*p
        return np.arctan2(Y,X+d)-np.arctan2(Y,X-d)+.13*slow
    return slow+(.3+.3*p)*np.sin(X*2.3+Y*1.9+tt)

def rgb_phase(theta):
    # Vectorized six-sector HSV, muted to preserve overlay legibility.
    hue=np.mod(theta/(2*np.pi)+.5,1)*6
    sector=np.floor(hue).astype(np.int32)
    f=hue-sector
    s,v=.68,.77
    p=v*(1-s); q=v*(1-s*f); t=v*(1-s*(1-f))
    out=np.empty((*hue.shape,3),dtype=np.uint8)
    choices=[
        (v,t,p),(q,v,p),(p,v,t),
        (p,q,v),(t,p,v),(v,p,q)]
    for k,(r,g,b) in enumerate(choices):
        mask=sector==k
        for channel,value in enumerate((r,g,b)):
            out[:,:,channel][mask]=np.asarray(value*255,dtype=np.uint8)[mask] if isinstance(value,np.ndarray) else round(value*255)
    return out

def centerline(draw,kind,phase):
    if kind not in ("zoom_to_vortex","vortex_with_streamlines","vortex_antivortex_pair","pair_unbinding"):
        return
    a=.55 if kind=="vortex_antivortex_pair" else (.25+1.05*phase if kind=="pair_unbinding" else 0)
    centers=[(0,0)] if kind in ("zoom_to_vortex","vortex_with_streamlines") else [(-a,0),(a,0)]
    for ix,c in enumerate(centers):
        cx=W/2+c[0]*W/5.4
        cy=H/2
        color="#ffc16b" if ix==0 else "#c6b4ff"
        draw.ellipse((cx-9,cy-9,cx+9,cy+9),fill=color)
    # Locally spaced *orientation strokes*. These are not velocity streamlines.
    if kind in ("vortex_with_streamlines","vortex_antivortex_pair","pair_unbinding"):
        for yy in range(96,H-88,42):
            for xx in range(52,W-48,45):
                gx=min(SW-1,max(0,round(xx/(W-1)*(SW-1))))
                gy=min(SH-1,max(0,round(yy/(H-1)*(SH-1))))
                ang=float(field_cache[gy,gx])
                dx=11*math.cos(ang);dy=11*math.sin(ang)
                draw.line((xx-dx,yy-dy,xx+dx,yy+dy),fill="#f3f8ff",width=2)
    if kind=="vortex_with_streamlines":
        cx,cy=W/2,H/2
        draw.arc((cx-124,cy-124,cx+124,cy+124),20,330,fill="#fff",width=3)

def wrap(draw,text,font,maxw):
    lines=[];cur=""
    for c in text:
        if c=="\n":
            lines.append(cur);cur="";continue
        if draw.textbbox((0,0),cur+c,font=font)[2]>maxw and cur:
            lines.append(cur);cur=c
        else:cur+=c
    if cur:lines.append(cur)
    return lines or [""]

def phase_legend(im):
    # Color is a periodic encoding of the planar spin angle.
    d=ImageDraw.Draw(im)
    cx,cy,rr=1110,115,55
    for deg in range(360):
        ang=math.radians(deg)
        color=tuple(int(v) for v in rgb_phase(np.array([[ang]]))[0,0])
        x0=cx+rr*math.cos(ang); y0=cy+rr*math.sin(ang)
        x1=cx+(rr+12)*math.cos(ang); y1=cy+(rr+12)*math.sin(ang)
        d.line((x0,y0,x1,y1),fill=color,width=3)
    d.ellipse((cx-rr+13,cy-rr+13,cx+rr-13,cy+rr-13),fill="#091626")
    f=ImageFont.truetype(FONT,24)
    d.text((cx-18,cy-16),"θ",font=f,fill="#ffffff")
    d.text((cx-103,cy+83),"色 = スピン角",font=f,fill="#ffffff")

def local_orientation(im,theta,kind):
    # Show how the smooth color field comes from actual local spin directions.
    # Sparse glyphs throughout the opening, concentrated in a focus region later.
    layer=Image.new("RGBA",(W,H),(0,0,0,0))
    d=ImageDraw.Draw(layer)
    if kind in ("phase_field_intro","phase_smooth_lowT"):
        positions=[(xx,yy) for yy in range(105,515,66) for xx in range(85,1040,67)]
        opacity=220
    else:
        positions=[(xx,yy) for yy in range(150,520,43) for xx in range(300,930,43)]
        opacity=155
    for xx,yy in positions:
        ix=min(SW-1,int(xx/W*SW));iy=min(SH-1,int(yy/H*SH))
        a=float(theta[iy,ix]); length=12
        vx=math.cos(a)*length;vy=math.sin(a)*length
        d.line((xx-vx,yy-vy,xx+vx,yy+vy),fill=(255,255,255,opacity),width=3)
        d.line((xx+vx,yy+vy,xx+vx-5*math.cos(a-.5),yy+vy-5*math.sin(a-.5)),fill=(255,255,255,opacity),width=2)
        d.line((xx+vx,yy+vy,xx+vx-5*math.cos(a+.5),yy+vy-5*math.sin(a+.5)),fill=(255,255,255,opacity),width=2)
    return Image.alpha_composite(im.convert("RGBA"),layer).convert("RGB")

def subtitle(draw,txt):
    if not txt:return
    font=ImageFont.truetype(FONT,34)
    lines=wrap(draw,txt,font,W-160)
    lines=lines[:2]
    heights=[draw.textbbox((0,0),line,font=font)[3] for line in lines]
    top=H-64-(len(lines)*49+26)
    draw.rounded_rectangle((55,top,W-55,H-64),radius=16,fill="#071120")
    for i,line in enumerate(lines):
        bb=draw.textbbox((0,0),line,font=font)
        draw.text(((W-(bb[2]-bb[0]))/2,top+9+i*49),line,font=font,fill="#fff")

def frame(kind,txt,progress):
    global field_cache
    theta=field(kind,progress)
    field_cache=theta
    im=Image.fromarray(rgb_phase(theta),"RGB").resize((W,H),Image.Resampling.BILINEAR)
    im=local_orientation(im,theta,kind)
    phase_legend(im)
    d=ImageDraw.Draw(im)
    centerline(d,kind,progress)
    if kind=="vortex_with_streamlines":
        f=ImageFont.truetype(FONT,34)
        d.rounded_rectangle((42,38,365,97),radius=13,fill="#071120")
        d.text((57,48),"巻き数  m = +1",font=f,fill="#fff")
    if kind=="correlation_compare":
        # Genuine calculated curves, inset on phase field.
        d.rounded_rectangle((230,120,1050,540),radius=20,fill="#091626")
        x0,y0=310,455
        d.line((x0,175,x0,y0,995,y0),fill="#edf1fb",width=3)
        for typ,col in (("algebraic","#77e9e2"),("exponential","#ffa86a")):
            pts=[]
            for i in range(1,160):
                r=1+i/20
                val=r**(-.25) if typ=="algebraic" else math.exp(-(r-1)/1.6)
                pts.append((x0+4*i, y0-260*val))
            d.line(pts,fill=col,width=5)
        f=ImageFont.truetype(FONT,29)
        d.text((470,194),"代数減衰",font=f,fill="#77e9e2")
        d.text((685,360),"指数減衰",font=f,fill="#ffa86a")
    subtitle(d,txt)
    return im

def render(kind,subtitle_text,audio,output,duration):
    if kind not in SUPPORTED:raise ValueError("Unknown motion "+kind)
    n=max(1,math.ceil(duration*FPS))
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo","-pixel_format","rgb24",
         "-video_size",f"{W}x{H}","-framerate",str(FPS),"-i","-",
         "-i",str(audio),"-c:v","libx264","-preset","ultrafast","-crf","30","-pix_fmt","yuv420p",
         "-c:a","aac","-ar","48000","-b:a","160k",
         "-t",str(duration),"-movflags","+faststart",str(output)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for i in range(n):
            im=frame(kind,subtitle_text,i/max(1,n-1))
            proc.stdin.write(im.tobytes())
        proc.stdin.close()
        if proc.wait()!=0:raise RuntimeError("ffmpeg failed")
    finally:
        if proc.poll() is None:proc.kill();proc.wait()

if __name__=="__main__":
    p=argparse.ArgumentParser()
    for a in ("motion","subtitle","audio","output"):p.add_argument("--"+a,required=True)
    p.add_argument("--duration",type=float,required=True)
    a=p.parse_args()
    render(a.motion,a.subtitle,a.audio,a.output,a.duration)
