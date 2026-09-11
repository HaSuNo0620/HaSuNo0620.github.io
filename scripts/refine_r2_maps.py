"""Refine the two correspondence diagrams in the R=2 Ising note.

This script intentionally imports the shared SVG helpers from ising_r2_visuals so
palette, typography, dark-mode behavior, and output dimensions remain identical.
It overwrites only real-fourier-map.svg and ising-liquid-correspondence.svg after
the base visual generator runs.
"""
from __future__ import annotations

import math

from ising_r2_visuals import save, text_box, mt


def real_fourier_map() -> None:
    p: list[str] = []

    text_box(p, 380, 34, 520, "遠方相関は振動しても、最大応答はまだ q = 0", cls="panel", height=32)

    # --- left: real-space correlation ---
    lx0, lx1 = 70, 350
    ly, ltop, lbot = 205, 82, 320
    p += [
        f'<line class="axis" x1="{lx0}" y1="{ly}" x2="{lx1}" y2="{ly}"/>',
        f'<line class="axis" x1="{lx0}" y1="{ltop}" x2="{lx0}" y2="{lbot}"/>',
        '<text class="panel" x="76" y="72">実空間</text>',
    ]

    rmax = 8.2
    qtail = 0.47
    pts = []
    for i in range(260):
        r = rmax * i / 259
        c = math.exp(-r / 3.0) * math.cos(qtail * r)
        x = lx0 + (lx1 - lx0) * i / 259
        y = ly - 98 * c
        pts.append((x, y))
    p.append('<polyline class="primary" points="' + ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts) + '"/>')

    # The first node is explicitly marked so the onset of the oscillatory tail is visual,
    # rather than being left to a sentence below the plot.
    rzero = math.pi / (2 * qtail)
    xzero = lx0 + (lx1 - lx0) * rzero / rmax
    p.append(f'<circle class="accentfill" cx="{xzero:.1f}" cy="{ly}" r="6"/>')
    p.append(f'<line class="mutedline dashed" x1="{xzero:.1f}" y1="{ly-88}" x2="{xzero:.1f}" y2="{ly+72}"/>')
    text_box(p, xzero + 28, 305, 126, "最初の符号反転", cls="small", height=30)
    p.append(mt((lx0 + lx1) / 2, 348, [("r", "var")], size=20))
    p.append(mt(40, 205, [("C", "var"), ("(r)", "roman")], size=20))

    # --- right: Fourier response ---
    rx0, rx1 = 450, 710
    rb, rt = 312, 92
    p += [
        f'<line class="axis" x1="{rx0}" y1="{rb}" x2="{rx1}" y2="{rb}"/>',
        f'<line class="axis" x1="{rx0}" y1="{rt}" x2="{rx0}" y2="{rb}"/>',
        '<text class="panel" x="456" y="72">波数空間</text>',
    ]

    pts = []
    for i in range(260):
        u = i / 259
        # q=0 remains the global maximum, while q_spec only leaves a shoulder-scale trace.
        val = 1.0 / (1 + 4.2 * u * u) + 0.035 * math.exp(-((u - 0.30) / 0.10) ** 2)
        x = rx0 + (rx1 - rx0) * u
        y = rb - 188 * val
        pts.append((x, y))
    p.append('<polyline class="secondary" points="' + ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts) + '"/>')

    qchi_y = rb - 188 * (1.0 + 0.035 * math.exp(-9.0))
    p.append(f'<circle class="greenfill" cx="{rx0}" cy="{qchi_y:.1f}" r="7"/>')
    text_box(p, 520, 113, 142, "最大：q_χ = 0", cls="small", height=30)

    qspec_u = 0.30
    qspecx = rx0 + (rx1 - rx0) * qspec_u
    p.append(f'<line class="primary dashed thin" x1="{qspecx:.1f}" y1="{rt+30}" x2="{qspecx:.1f}" y2="{rb}"/>')
    text_box(p, qspecx + 34, 267, 132, "q_spec > 0", cls="small", height=30)
    p.append(mt((rx0 + rx1) / 2, 348, [("q", "var")], size=20))
    p.append(mt(420, 205, [("χ", "var"), ("(q)", "roman")], size=20))

    p.append('<path class="arrow-primary" d="M 365 205 L 430 205"/>')
    text_box(p, 397, 180, 118, "Fourier 変換", cls="small", height=30)
    text_box(p, 380, 410, 560, "q_spec は遠方 tail の周期、q_χ は応答全体の最大位置を表す", cls="label", height=34)

    save("real-fourier-map.svg", p)


def ising_liquid_map() -> None:
    p: list[str] = []

    # Replace the old row-by-row table with two spectral planes.  Each panel shows
    # the same qualitative event: a one-dimensional decay mode acquires a phase.
    p += [
        '<rect class="region" x="24" y="58" width="320" height="304" rx="18"/>',
        '<rect class="region" x="416" y="58" width="320" height="304" rx="18"/>',
        '<text class="panel" x="184" y="91" text-anchor="middle">Ising：転送スペクトル</text>',
        '<text class="panel" x="576" y="91" text-anchor="middle">液体論：OZ pole</text>',
    ]

    # Left: real subleading eigenvalue -> complex-conjugate pair in the mu plane.
    cx, cy = 184, 205
    p += [
        f'<line class="axis" x1="78" y1="{cy}" x2="304" y2="{cy}"/>',
        f'<line class="axis" x1="{cx}" y1="112" x2="{cx}" y2="292"/>',
        '<text class="small" x="284" y="226">Re μ</text>',
        '<text class="small" x="194" y="126">Im μ</text>',
    ]
    p.append('<circle class="inkfill" cx="252" cy="205" r="7"/>')
    for yy in (158, 252):
        p.append(f'<circle class="accentfill" cx="230" cy="{yy}" r="8"/>')
    p.append('<path class="arrow-primary" d="M 247 197 C 242 181, 237 169, 232 163"/>')
    # Compact local legend instead of labels that collide with the spectral points.
    p += [
        '<circle class="inkfill" cx="104" cy="282" r="5"/>',
        '<text class="small" x="118" y="287">単調減衰</text>',
        '<circle class="accentfill" cx="218" cy="282" r="6"/>',
        '<text class="small" x="233" y="287">減衰振動</text>',
    ]
    p.append(mt(184, 329, [("μ", "var"), (" = ρ · exp(", "roman"), ("±iq", "var"), (")", "roman")], size=19))

    # Right: imaginary-axis pole -> off-axis pair in the complex-k plane.
    kx, ky = 576, 205
    p += [
        f'<line class="axis" x1="470" y1="{ky}" x2="696" y2="{ky}"/>',
        f'<line class="axis" x1="{kx}" y1="112" x2="{kx}" y2="292"/>',
        '<text class="small" x="676" y="226">Re k</text>',
        '<text class="small" x="586" y="126">Im k</text>',
    ]
    p.append('<circle class="inkfill" cx="576" cy="151" r="7"/>')
    p.append('<circle class="accentfill" cx="624" cy="166" r="8"/>')
    p.append('<circle class="accentfill" cx="528" cy="166" r="8"/>')
    p.append('<path class="arrow-primary" d="M 584 153 C 598 154, 610 159, 618 163"/>')
    p += [
        '<circle class="inkfill" cx="496" cy="282" r="5"/>',
        '<text class="small" x="510" y="287">純虚数 pole</text>',
        '<circle class="accentfill" cx="618" cy="282" r="6"/>',
        '<text class="small" x="633" y="287">複素 pole 対</text>',
    ]
    p.append(mt(576, 329, [("k", "var"), ("p", "roman"), (" = ±", "roman"), ("q", "var"), (" + i", "roman"), ("α", "var")], size=19))

    p.append('<path class="arrow-primary" d="M 350 205 L 410 205"/>')
    text_box(p, 380, 180, 112, "同じ構造", cls="small", height=30)
    text_box(p, 380, 403, 610, "軸上の支配モードが複素対へ移ると、遠方相関は単調減衰から減衰振動へ変わる", cls="label", height=34)

    save("ising-liquid-correspondence.svg", p)


if __name__ == "__main__":
    real_fourier_map()
    ising_liquid_map()
