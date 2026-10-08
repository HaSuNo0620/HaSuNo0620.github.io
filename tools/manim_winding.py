#!/usr/bin/env python3
"""A standalone, narration-paced winding-number animation using Manim CE."""
import argparse
import os
import subprocess
from pathlib import Path

from manim import (
    Scene, VGroup, Arrow, Circle, Dot, Text, DecimalNumber, ValueTracker,
    always_redraw, Create, FadeIn, FadeOut, Write, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN, WHITE, BLUE_C, YELLOW, TEAL_C,
    config, linear
)
import numpy as np

class WindingNumber(Scene):
    def construct(self):
        duration=float(os.getenv("VOICE_DURATION","12"))
        config.background_color="#0d1725"
        # The spoken text is split into meaningful actions using measured audio duration.
        step=duration/5.0
        heading=Text("渦の巻き数",font="Noto Sans CJK JP",font_size=34).to_corner(UP+LEFT)
        formula=Text("m = Δθ / 2π",font="Noto Sans CJK JP",font_size=34).to_corner(UP+RIGHT)
        self.add(heading)
        points=[]
        for y in np.arange(-2.25,2.3,.47):
            for x in np.arange(-4.15,4.18,.47):
                if x*x+y*y<.12: continue
                th=np.arctan2(y,x)
                start=np.array([x,y,0.])
                vec=np.array([np.cos(th),np.sin(th),0.])*.22
                points.append(Arrow(start-vec*.4,start+vec*.6,buff=0,stroke_width=2.0,
                                    tip_length=.075,color=TEAL_C))
        field=VGroup(*points)
        self.play(FadeIn(field,lag_ratio=.005),run_time=step*.75)
        self.wait(step*.25)
        path=Circle(radius=1.6,color=BLUE_C,stroke_width=5)
        self.play(Create(path),run_time=step*.8)
        self.add(formula)
        self.wait(step*.2)
        angle=ValueTracker(0.)
        walker=always_redraw(lambda: Dot(np.array([1.6*np.cos(angle.get_value()),
                                                   1.6*np.sin(angle.get_value()),0]),
                                          color=YELLOW,radius=.11))
        # Visualize local orientation with a rotating arrow at the right side.
        arrow=always_redraw(lambda: Arrow(
            np.array([3.8,0,0]),
            np.array([3.8+.65*np.cos(angle.get_value()),.65*np.sin(angle.get_value()),0]),
            buff=0,stroke_width=6,tip_length=.15,color=YELLOW))
        self.add(walker,arrow)
        self.play(angle.animate.set_value(np.pi*2),run_time=step*2.0,rate_func=linear)
        result=Text("Δθ = 2π   →   m = +1",font="Noto Sans CJK JP",
                    font_size=38,color=YELLOW).to_edge(DOWN,buff=.35)
        self.play(Write(result),run_time=step*.75)
        self.wait(step*.25)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    p.add_argument("--narration",required=True)
    p.add_argument("--reading",required=True)
    args=p.parse_args()
    from voicevox_video import synthesize,probe_duration
    output=Path(args.output)
    output.mkdir(parents=True,exist_ok=True)
    wav=output/"narration.wav"
    synthesize(args.reading,3,wav)
    duration=probe_duration(wav)
    env=dict(os.environ,VOICE_DURATION=str(duration))
    temp=output/"manim"
    temp.mkdir(exist_ok=True)
    subprocess.run(["manim","-ql","--fps","24","-r","960,540",
                    "--media_dir",str(temp),"--output_file","winding.mp4",
                    str(Path(__file__).resolve()),"WindingNumber"],
                    env=env,check=True)
    clips=list(temp.rglob("winding.mp4"))
    if len(clips)!=1:raise RuntimeError(f"Expected one Manim movie, got {clips}")
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",str(clips[0]),
                    "-i",str(wav),"-map","0:v","-map","1:a",
                    "-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac",
                    "-t",str(duration),"-movflags","+faststart",
                    str(output/"finished.mp4")],check=True)
    print("Finished winding-number Manim demo:",output/"finished.mp4")

if __name__=="__main__":main()
