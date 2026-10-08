#!/usr/bin/env python3
"""Render a narrated educational video from a JSON job using tts.quest VOICEVOX."""
import argparse
import io
import json
import os
import subprocess
import time
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont

BASE = "https://api.tts.quest/v3/voicevox/synthesis"
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
W, H = 1280, 720

def api_request(method, url, **kwargs):
    r = requests.request(method, url, timeout=60, **kwargs)
    r.raise_for_status()
    return r

def synthesize(text, speaker, dst):
    for attempt in range(5):
        r = requests.post(BASE, data={"speaker": str(speaker), "text": text}, timeout=60)
        if r.status_code == 429:
            pause = min(int(r.json().get("retryAfter", 30)), 180)
            print(f"Rate limit: waiting {pause}s", flush=True)
            time.sleep(pause)
            continue
        r.raise_for_status()
        payload = r.json()
        if not payload.get("success"):
            raise RuntimeError("VOICEVOX request failed: " + str(payload))
        status_url, wav_url = payload["audioStatusUrl"], payload["wavDownloadUrl"]
        for _ in range(120):
            status = api_request("GET", status_url).json()
            if status.get("isAudioError"):
                raise RuntimeError("VOICEVOX generation error: " + str(status))
            if status.get("isAudioReady"):
                wav = api_request("GET", wav_url).content
                if not wav.startswith(b"RIFF"):
                    raise RuntimeError("Downloaded audio is not WAV")
                dst.write_bytes(wav)
                return
            time.sleep(8)
        raise TimeoutError("VOICEVOX generation timed out")
    raise RuntimeError("VOICEVOX API rate limited after retries")

def wrapped(draw, text, font, maxwidth):
    lines = []
    for para in text.splitlines():
        acc = ""
        for c in para:
            if draw.textbbox((0, 0), acc+c, font=font)[2] > maxwidth and acc:
                lines.append(acc)
                acc = c
            else:
                acc += c
        lines.append(acc)
    return lines

def make_slide(scene, i, total, path):
    im = Image.new("RGB", (W, H), "#0b1220")
    d = ImageDraw.Draw(im)
    reg = ImageFont.truetype(FONT, 35)
    big = ImageFont.truetype(FONT_BOLD, 68)
    small = ImageFont.truetype(FONT, 29)
    d.rectangle((0, 0, W, 14), fill="#20bfae")
    d.text((68, 56), "XY MODEL  /  BKT TRANSITION", font=small, fill="#73dbc9")
    y = 143
    for ln in wrapped(d, scene["title"], big, W-140):
        d.text((68, y), ln, font=big, fill="#ffffff")
        y += 88
    y += 34
    for ln in wrapped(d, scene.get("caption", ""), reg, W-140):
        d.text((78, y), ln, font=reg, fill="#ced8e8")
        y += 64
    d.line((68, H-105, W-68, H-105), fill="#33445b", width=2)
    d.text((69, H-81), "VOICEVOX  /  学習用動画", font=small, fill="#8da3b9")
    d.text((W-190, H-81), f"{i+1:02d} / {total:02d}", font=small, fill="#8da3b9")
    im.save(path)

def probe_duration(wav_path):
    s = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(wav_path)], text=True)
    return float(s.strip())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    ap.add_argument("--output", default="output")
    args = ap.parse_args()
    job = json.loads(Path(args.job).read_text(encoding="utf-8"))
    scenes = job.get("scenes", [])
    if not (1 <= len(scenes) <= 15):
        raise ValueError("Expected 1-15 scenes")
    speaker = int(job.get("speaker", 3))
    if not (0 <= speaker <= 200):
        raise ValueError("Speaker id out of range")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    segs = []
    for i, scene in enumerate(scenes):
        title = str(scene.get("title", ""))
        caption = str(scene.get("caption", ""))
        narration = str(scene.get("narration", ""))
        if not title or not narration or len(narration)>240 or len(title)>100 or len(caption)>500:
            raise ValueError(f"Invalid scene {i}: title/narration required; narration <= 240 characters")
        png = out / f"slide_{i:02d}.png"
        wav = out / f"voice_{i:02d}.wav"
        mp4 = out / f"segment_{i:02d}.mp4"
        make_slide(scene, i, len(scenes), png)
        print(f"Synthesizing scene {i+1}/{len(scenes)}", flush=True)
        synthesize(narration, speaker, wav)
        seconds = probe_duration(wav) + 0.6
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-loop", "1", "-framerate", "24", "-i", str(png), "-i", str(wav), "-vf", "format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", str(seconds), "-movflags", "+faststart", str(mp4)], check=True)
        segs.append(mp4)
    list_path = out / "concat.txt"
    list_path.write_text("".join("file '" + p.name + "'\n" for p in segs), encoding="utf-8")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path), "-c", "copy", "-movflags", "+faststart", str(out / "finished.mp4")], check=True)
    print(f"Created {out / 'finished.mp4'}", flush=True)

if __name__ == "__main__":
    main()
