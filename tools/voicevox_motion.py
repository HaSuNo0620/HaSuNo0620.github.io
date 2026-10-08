#!/usr/bin/env python3
"""Frame-by-frame XY/BKT conceptual animation for the VOICEVOX video pipeline."""
import argparse
import math
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 24
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

def spin(draw, x, y, angle, radius=18, color="#66f2df"):
    dx=math.cos(angle)*radius; dy=math.sin(angle)*radius
    draw.line((x-dx,y-dy,x+dx,y+dy), fill=color, width=4)
    ex,ey=x+dx,y+dy
    a=angle+2.65; b=angle-2.65
    draw.line((ex,ey,ex+10*math.cos(a),ey+10*math.sin(a)),fill=color,width=4)
    draw.line((ex,ey,ex+10*math.cos(b),ey+10*math.sin(b)),fill=color,width=4)

def render(base, draw, mode, t, total):
    left, top, width, height=110,327,1060,278
    draw.rounded_rectangle((left-17,top-12,left+width+17,top+height+12),radius=22,fill="#111f35",outline="#30445b",width=2)
    if mode=="spins":
        for row in range(5):
            for col in range(16):
                x=left+col*66+22; y=top+row*55+22
                angle=.25*math.sin(col*.38+row*.7+t*1.5)+.05*col
                spin(draw,x,y,angle,17)
    elif mode in ("vortex_pair","unbinding"):
        progress=max(0,min(1,t/max(.01,total)))
        gap=(125+progress*350) if mode=="unbinding" else (250+18*math.sin(t))
        centers=((W/2-gap/2,top+height/2,1),(W/2+gap/2,top+height/2,-1))
        for row in range(5):
            for col in range(17):
                x=left+col*63+22; y=top+row*55+25
                theta=0
                for cx,cy,charge in centers:
                    theta+=charge*math.atan2(y-cy,x-cx)
                spin(draw,x,y,theta+.08*math.sin(t*1.5),13)
        for cx,cy,q in centers:
            col="#ffba68" if q==1 else "#aa9bff"
            draw.ellipse((cx-12,cy-12,cx+12,cy+12), fill=col)
        if mode=="unbinding":
            d=ImageDraw.Draw(base)
            font=ImageFont.truetype(FONT,26)
            d.text((left+15,top+height-32),"温度上昇 → 渦と反渦が離れる",font=font,fill="#c7e9e4")
    else:
        for row in range(5):
            for col in range(16):
                x=left+col*66+22; y=top+row*55+22
                spin(draw,x,y,.15*math.sin(t+col*.25),15)

def animate(image_path, wav_path, output_path, mode, seconds):
    original=Image.open(image_path).convert("RGB")
    frames=max(1,math.ceil(float(seconds)*FPS))
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo","-vcodec","rawvideo",
         "-s",f"{W}x{H}","-pix_fmt","rgb24","-r",str(FPS),"-i","-",
         "-i",str(wav_path),"-c:v","libx264","-preset","veryfast","-crf","27",
         "-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-ar","48000",
         "-t",str(seconds),"-movflags","+faststart",str(output_path)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for n in range(frames):
            canvas=original.copy()
            draw=ImageDraw.Draw(canvas)
            render(canvas,draw,mode,n/FPS,seconds)
            proc.stdin.write(canvas.tobytes())
        proc.stdin.close()
        if proc.wait()!=0:
            raise RuntimeError("FFmpeg motion rendering failed")
    except BaseException:
        if proc.stdin and not proc.stdin.closed:
            proc.stdin.close()
        proc.kill()
        proc.wait()
        raise

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--image",required=True)
    p.add_argument("--audio",required=True)
    p.add_argument("--output",required=True)
    p.add_argument("--motion",required=True)
    p.add_argument("--duration",required=True,type=float)
    a=p.parse_args()
    animate(a.image,a.audio,a.output,a.motion,a.duration)
