"""Refine the four key correspondence/structure diagrams in the R=2 Ising note.

This script intentionally imports the shared SVG helpers from ising_r2_visuals so
palette, typography, dark-mode behavior, and output dimensions remain identical.
It overwrites selected conceptual figures after the base visual generator runs.
"""
from __future__ import annotations

import math

from ising_r2_visuals import save, text_box, mt, kappa_disorder, kappa_lifshitz


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

    p += [
        '<rect class="region" x="24" y="58" width="320" height="304" rx="18"/>',
        '<rect class="region" x="416" y="58" width="320" height="304" rx="18"/>',
        '<text class="panel" x="184" y="91" text-anchor="middle">Ising：転送スペクトル</text>',
        '<text class="panel" x="576" y="91" text-anchor="middle">液体論：OZ pole</text>',
    ]

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
    p += [
        '<circle class="inkfill" cx="104" cy="282" r="5"/>',
        '<text class="small" x="118" y="287">単調減衰</text>',
        '<circle class="accentfill" cx="218" cy="282" r="6"/>',
        '<text class="small" x="233" y="287">減衰振動</text>',
    ]
    p.append(mt(184, 329, [("μ", "var"), (" = ρ · exp(", "roman"), ("±iq", "var"), (")", "roman")], size=19))

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


def information_channel() -> None:
    """Show directly that R=2 turns wall variables into a conditional channel."""
    p: list[str] = []
    text_box(p, 380, 34, 600, "R = 2 では、隣の壁の有無が次の壁の確率を変える", cls="panel", height=32)

    # Two parallel spin chains; the lower bond variables make the probabilistic
    # difference explicit without relying on prose alone.
    for side, x0 in enumerate((48, 408)):
        panel_x = 24 if side == 0 else 384
        title = "R = 1：独立な壁" if side == 0 else "R = 2：相関する壁"
        p.append(f'<rect class="region" x="{panel_x}" y="60" width="352" height="300" rx="18"/>')
        p.append(f'<text class="panel" x="{panel_x+176}" y="91" text-anchor="middle">{title}</text>')

        spins = [1, 1, -1, -1, 1, 1]
        xs = [x0 + i * 50 for i in range(len(spins))]
        y_spin = 145
        for i, (x, s) in enumerate(zip(xs, spins)):
            if i < len(xs) - 1:
                p.append(f'<line class="inkline" x1="{x+15}" y1="{y_spin}" x2="{xs[i+1]-15}" y2="{y_spin}"/>')
            p.append(f'<circle class="node" cx="{x}" cy="{y_spin}" r="14"/>')
            p.append(f'<text class="text" x="{x}" y="{y_spin+6}" text-anchor="middle">{"+" if s > 0 else "−"}</text>')

        bond_x = [(xs[i] + xs[i + 1]) / 2 for i in range(len(xs) - 1)]
        tau = [spins[i] * spins[i + 1] for i in range(len(spins) - 1)]
        y_tau = 245
        p.append(f'<text class="small" x="{panel_x+26}" y="{y_tau+5}">壁変数 τᵢ</text>')
        for j, (x, t) in enumerate(zip(bond_x, tau)):
            cls = "accentfill" if t < 0 else "node2"
            if t < 0:
                p.append(f'<circle class="accentfill" cx="{x}" cy="{y_tau}" r="9"/>')
            else:
                p.append(f'<circle class="node2" cx="{x}" cy="{y_tau}" r="7"/>')
            if j < len(bond_x) - 1:
                if side == 0:
                    p.append(f'<line class="mutedline dashed" x1="{x+10}" y1="{y_tau}" x2="{bond_x[j+1]-10}" y2="{y_tau}"/>')
                else:
                    p.append(f'<line class="secondary" x1="{x+10}" y1="{y_tau}" x2="{bond_x[j+1]-10}" y2="{y_tau}"/>')

        # Highlight one adjacent pair as the local channel.
        x1, x2 = bond_x[1], bond_x[2]
        p.append(f'<circle fill="none" stroke-width="3" class="secondary" cx="{x1}" cy="{y_tau}" r="15"/>')
        p.append(f'<circle fill="none" stroke-width="3" class="secondary" cx="{x2}" cy="{y_tau}" r="15"/>')

        if side == 0:
            text_box(p, panel_x + 176, 315, 292, "P(τᵢ₊₁ | τᵢ) = P(τᵢ₊₁)", cls="small", height=32)
        else:
            text_box(p, panel_x + 176, 315, 300, "P(τᵢ₊₁ | τᵢ) ≠ P(τᵢ₊₁)", cls="small", height=32)

    p.append('<path class="arrow-primary" d="M 365 212 L 395 212"/>')
    text_box(p, 380, 190, 112, "J₂ を加える", cls="small", height=30)
    text_box(p, 380, 405, 610, "熱雑音そのものではなく、熱的反転の並び方に1ステップの記憶が生まれる", cls="label", height=34)
    save("information-channel.svg", p)


def correlation_structure_map() -> None:
    """Give the three correlation regimes a clear visual hierarchy."""
    left, right, top, bottom = 96, 716, 34, 350
    xmin, xmax, ymin, ymax = 0.08, 3.0, 0.0, 0.60

    def X(x: float) -> float:
        return left + (x - xmin) / (xmax - xmin) * (right - left)

    def Y(y: float) -> float:
        return bottom - (y - ymin) / (ymax - ymin) * (bottom - top)

    p: list[str] = []
    ts = [xmin + (xmax - xmin) * i / 260 for i in range(261)]
    kd = [kappa_disorder(t) for t in ts]
    kl = [kappa_lifshitz(t) for t in ts]

    # Region fills: neutral -> blue transition regime -> green finite-q regime.
    lower = [(X(ts[0]), Y(0.0)), (X(ts[-1]), Y(0.0))] + [(X(t), Y(k)) for t, k in reversed(list(zip(ts, kd)))]
    middle = [(X(t), Y(k)) for t, k in zip(ts, kd)] + [(X(t), Y(k)) for t, k in reversed(list(zip(ts, kl)))]
    upper = [(X(ts[0]), Y(ymax)), (X(ts[-1]), Y(ymax))] + [(X(t), Y(k)) for t, k in reversed(list(zip(ts, kl)))]
    p.append('<polygon class="region" opacity=".34" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in lower) + '"/>')
    p.append('<polygon class="soft" opacity=".42" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in middle) + '"/>')
    p.append('<polygon class="greenfill" opacity=".10" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in upper) + '"/>')

    for x in (0.1, 0.5, 1, 1.5, 2, 2.5, 3):
        xx = X(x)
        p.append(f'<line class="grid" x1="{xx:.1f}" y1="{top}" x2="{xx:.1f}" y2="{bottom}"/>')
        p.append(f'<text class="small" x="{xx:.1f}" y="378" text-anchor="middle">{x:g}</text>')
    for y in (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        yy = Y(y)
        p.append(f'<line class="grid" x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}"/>')
        p.append(f'<text class="small" x="{left-12}" y="{yy+5:.1f}" text-anchor="end">{y:g}</text>')

    p.append('<polyline class="primary" points="' + ' '.join(f'{X(t):.1f},{Y(k):.1f}' for t, k in zip(ts, kd)) + '"/>')
    p.append('<polyline class="secondary dashed" points="' + ' '.join(f'{X(t):.1f},{Y(k):.1f}' for t, k in zip(ts, kl)) + '"/>')
    p += [
        f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{bottom}"/>',
        f'<line class="axis" x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}"/>',
    ]
    p.append(mt((left + right) / 2, 422, [("t", "var"), (" = k", "roman"), ("B", "roman"), ("T/J", "var"), ("₁", "roman")], size=21))
    ylab = mt(28, 205, [("κ", "var"), (" = −", "roman"), ("J", "var"), ("₂/", "roman"), ("J", "var"), ("₁", "roman")], size=21)
    p.append(ylab.replace('<text ', '<text transform="rotate(-90 28 205)" ', 1))

    # Short region labels with a clear 1 -> 2 -> 3 hierarchy.
    text_box(p, 230, 304, 230, "1  単調減衰", cls="label", height=32)
    text_box(p, 462, 224, 260, "2  遠方 tail が振動", cls="label", height=32)
    text_box(p, 510, 86, 250, "3  有限波数応答", cls="label", height=32)

    text_box(p, 585, 319, 232, "Stephenson disorder line", cls="small", height=28)
    text_box(p, 620, 151, 148, "Lifshitz line", cls="small", height=28)

    # At t=1, increasing kappa crosses the two spectral/response boundaries in order.
    xt = X(1.0)
    y0, y1 = Y(0.08), Y(0.52)
    p.append(f'<path class="arrow-primary" d="M {xt:.1f} {y0:.1f} L {xt:.1f} {y1:.1f}"/>')
    text_box(p, xt + 54, (y0 + y1) / 2, 100, "κ を増やす", cls="small", height=28)

    p.append(f'<circle class="inkfill" cx="{X(0.08):.1f}" cy="{Y(0.5):.1f}" r="6"/>')
    text_box(p, 250, 61, 300, "T = 0：κ = 1/2 基底状態境界", cls="small", height=28)
    save("correlation-structure-map.svg", p)


if __name__ == "__main__":
    real_fourier_map()
    ising_liquid_map()
    information_channel()
    correlation_structure_map()
