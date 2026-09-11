"""Shared Matplotlib figure style for HaSuNo0620.github.io.

Figure Style v1.5 makes theme intent explicit at figure creation time and leaves
postprocess_figures.py as the final CI safety net.  Text remains SVG text
(svg.fonttype='none') so labels can be recolored reliably.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

COLORS = {
    "paper": "#f3efe6",
    "paper2": "#ebe5d9",
    "ink": "#171714",
    "muted": "#716d64",
    "line": "#cbc3b5",
    "accent": "#5866e9",
    "green": "#39705a",
}

DARK_COLORS = {
    "paper": "#1c1c19",
    "paper2": "#272720",
    "ink": "#f0eadf",
    "muted": "#a8a196",
    "line": "#4a4740",
    "accent": "#99a2ff",
    "green": "#8bc4a9",
}

FIGSIZE = (7.6, 4.4)
FIGSIZE_WIDE = (7.6, 3.6)
FIGSIZE_TALL = (7.6, 5.2)

FONT_SIZE = {
    "axis": 19,
    "tick": 16,
    "legend": 18,
    "annotation": 17,
    "panel": 18,
}

LINEWIDTH = {
    "primary": 4.5,
    "secondary": 3.6,
    "reference": 2.0,
    "axis": 1.8,
    "grid": 1.1,
    "errorbar": 1.8,
    "legend_sample": 5.0,
}

MARKERSIZE = 8.5

SERIES_STYLES = (
    {"linestyle": "-", "linewidth": 4.5},
    {"linestyle": "--", "linewidth": 3.6},
    {"linestyle": ":", "linewidth": 3.6},
    {"linestyle": "-.", "linewidth": 3.6},
)


def _mpl():
    """Import matplotlib lazily so palette tokens can be used without it."""
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    return mpl, plt


def _make_svg_theme_aware(path: Path) -> None:
    """Replace palette literals with CSS variables and embed dark-mode values."""
    if path.suffix.lower() != ".svg":
        return

    svg = path.read_text(encoding="utf-8")
    replacements = {
        COLORS["paper"]: "var(--figure-paper)",
        COLORS["paper2"]: "var(--figure-paper2)",
        COLORS["ink"]: "var(--figure-ink)",
        COLORS["muted"]: "var(--figure-muted)",
        COLORS["line"]: "var(--figure-line)",
        COLORS["accent"]: "var(--figure-accent)",
        COLORS["green"]: "var(--figure-green)",
    }
    for source, target in replacements.items():
        svg = re.sub(re.escape(source), target, svg, flags=re.I)

    # Third-party Matplotlib defaults sometimes sneak pure black into text/path style.
    svg = re.sub(
        r"(?i)(fill|stroke)\s*:\s*(?:#000000|#000(?![0-9a-f])|black)",
        r"\1:var(--figure-ink)",
        svg,
    )
    svg = re.sub(
        r"(?i)(fill|stroke)=(['\"])(?:#000000|#000(?![0-9a-f])|black)\2",
        r"\1=\2var(--figure-ink)\2",
        svg,
    )

    theme_css = f"""<style id="matplotlib-figure-theme">
:root {{
  --figure-paper: {COLORS['paper']};
  --figure-paper2: {COLORS['paper2']};
  --figure-ink: {COLORS['ink']};
  --figure-muted: {COLORS['muted']};
  --figure-line: {COLORS['line']};
  --figure-accent: {COLORS['accent']};
  --figure-green: {COLORS['green']};
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --figure-paper: {DARK_COLORS['paper']};
    --figure-paper2: {DARK_COLORS['paper2']};
    --figure-ink: {DARK_COLORS['ink']};
    --figure-muted: {DARK_COLORS['muted']};
    --figure-line: {DARK_COLORS['line']};
    --figure-accent: {DARK_COLORS['accent']};
    --figure-green: {DARK_COLORS['green']};
  }}
}}
</style>"""
    svg_end = svg.find(">")
    if svg_end >= 0 and 'id="matplotlib-figure-theme"' not in svg:
        svg = svg[: svg_end + 1] + "\n" + theme_css + svg[svg_end + 1 :]
    path.write_text(svg, encoding="utf-8")


def apply_site_style() -> None:
    mpl, _ = _mpl()
    mpl.rcParams.update(
        {
            "figure.figsize": FIGSIZE,
            "figure.facecolor": "none",
            "figure.edgecolor": "none",
            "savefig.facecolor": "none",
            "savefig.edgecolor": "none",
            "savefig.transparent": True,
            "axes.facecolor": "none",
            "axes.edgecolor": COLORS["ink"],
            "axes.labelcolor": COLORS["ink"],
            "axes.titlecolor": COLORS["ink"],
            "axes.linewidth": LINEWIDTH["axis"],
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.axisbelow": True,
            "grid.color": COLORS["line"],
            "grid.linewidth": LINEWIDTH["grid"],
            "grid.alpha": 0.48,
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "xtick.labelcolor": COLORS["muted"],
            "ytick.labelcolor": COLORS["muted"],
            "xtick.labelsize": FONT_SIZE["tick"],
            "ytick.labelsize": FONT_SIZE["tick"],
            "axes.labelsize": FONT_SIZE["axis"],
            "legend.fontsize": FONT_SIZE["legend"],
            "legend.frameon": True,
            "legend.framealpha": 0.90,
            "legend.facecolor": COLORS["paper"],
            "legend.edgecolor": COLORS["line"],
            "legend.labelcolor": COLORS["ink"],
            "font.family": "sans-serif",
            "font.sans-serif": [
                "Noto Sans JP",
                "Hiragino Sans",
                "Yu Gothic",
                "DejaVu Sans",
            ],
            "mathtext.fontset": "stix",
            "axes.formatter.use_mathtext": True,
            "text.color": COLORS["ink"],
            "lines.linewidth": LINEWIDTH["primary"],
            "lines.markersize": MARKERSIZE,
            "lines.solid_capstyle": "round",
            "lines.dash_capstyle": "round",
            "svg.fonttype": "none",
        }
    )


def new_figure(*, size: str = "standard", constrained_layout: bool = True):
    apply_site_style()
    _, plt = _mpl()
    sizes = {"standard": FIGSIZE, "wide": FIGSIZE_WIDE, "tall": FIGSIZE_TALL}
    if size not in sizes:
        raise ValueError(f"unknown figure size: {size!r}")
    return plt.subplots(figsize=sizes[size], constrained_layout=constrained_layout)


def style_axes(ax, *, xlabel=None, ylabel=None, grid=True, zero_x=False, zero_y=False) -> None:
    """Apply explicit label/tick colors instead of relying on Matplotlib defaults."""
    if xlabel is not None:
        ax.set_xlabel(xlabel, color=COLORS["ink"])
    if ylabel is not None:
        ax.set_ylabel(ylabel, color=COLORS["ink"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(COLORS["ink"])
    ax.spines["bottom"].set_color(COLORS["ink"])
    ax.tick_params(
        axis="both",
        which="major",
        length=5.5,
        width=1.4,
        colors=COLORS["muted"],
        labelcolor=COLORS["muted"],
    )
    ax.grid(grid, which="major")
    ax.grid(False, which="minor")
    if zero_x:
        ax.axvline(0, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":", zorder=0)
    if zero_y:
        ax.axhline(0, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":", zorder=0)


def plot_exact(ax, x, y, *, label=None, **kwargs):
    defaults = {"color": COLORS["accent"], "lw": LINEWIDTH["primary"], "ls": "-", "label": label}
    defaults.update(kwargs)
    return ax.plot(x, y, **defaults)


def plot_approx(ax, x, y, *, label=None, **kwargs):
    defaults = {"color": COLORS["green"], "lw": LINEWIDTH["secondary"], "ls": "--", "label": label}
    defaults.update(kwargs)
    return ax.plot(x, y, **defaults)


def plot_data(ax, x, y, *, yerr=None, label=None, marker="o", **kwargs):
    defaults = {
        "fmt": marker,
        "ms": MARKERSIZE,
        "color": COLORS["ink"],
        "mec": COLORS["ink"],
        "mfc": COLORS["paper"],
        "elinewidth": LINEWIDTH["errorbar"],
        "capsize": 3.5,
        "linestyle": "none",
        "label": label,
    }
    defaults.update(kwargs)
    return ax.errorbar(x, y, yerr=yerr, **defaults)


def shade_uncertainty(ax, x, lower, upper, *, color=None, alpha=0.15, **kwargs):
    return ax.fill_between(x, lower, upper, color=color or COLORS["accent"], alpha=alpha, linewidth=0, **kwargs)


def style_legend(
    ax,
    *,
    loc="best",
    outside: bool = False,
    ncol: int = 1,
    dark: bool = False,
    **kwargs,
):
    palette = DARK_COLORS if dark else COLORS
    defaults = {
        "frameon": True,
        "framealpha": 0.90 if not dark else 0.86,
        "facecolor": palette["paper"],
        "edgecolor": palette["line"],
        "labelcolor": palette["ink"],
        "fontsize": FONT_SIZE["legend"],
        "handlelength": 2.6,
        "ncol": ncol,
    }
    if outside:
        defaults.update({"loc": "upper left", "bbox_to_anchor": (1.02, 1.0), "borderaxespad": 0.0})
    else:
        defaults["loc"] = loc
    defaults.update(kwargs)
    leg = ax.legend(**defaults)
    frame = leg.get_frame()
    frame.set_linewidth(1.0)
    for text in leg.get_texts():
        text.set_color(palette["ink"])
    for line in leg.get_lines():
        line.set_linewidth(max(line.get_linewidth(), LINEWIDTH["legend_sample"]))
    return leg


def annotation_box(*, dark: bool = False, alpha: float | None = None) -> dict:
    """Reusable paper-backed annotation style for labels placed over data."""
    palette = DARK_COLORS if dark else COLORS
    return {
        "boxstyle": "round,pad=0.20",
        "facecolor": palette["paper"],
        "edgecolor": palette["line"],
        "linewidth": 0.8,
        "alpha": alpha if alpha is not None else (0.82 if not dark else 0.78),
    }


def direct_label(
    ax,
    x: float,
    y: float,
    text: str,
    *,
    color=None,
    dark: bool = False,
    backdrop: bool = True,
    **kwargs,
):
    palette = DARK_COLORS if dark else COLORS
    defaults = {
        "fontsize": FONT_SIZE["annotation"],
        "color": color or palette["ink"],
        "ha": "left",
        "va": "center",
    }
    if backdrop:
        defaults["bbox"] = annotation_box(dark=dark, alpha=0.86 if not dark else 0.82)
    defaults.update(kwargs)
    return ax.text(x, y, text, **defaults)


def panel_label(ax, label: str, *, x: float = 0.01, y: float = 0.99, dark: bool = False) -> None:
    palette = DARK_COLORS if dark else COLORS
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=FONT_SIZE["panel"],
        fontweight="semibold",
        color=palette["ink"],
    )


def save_figure(fig, path: str | Path, *, dpi: int = 180, close: bool = True) -> Path:
    _, plt = _mpl()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, transparent=True, bbox_inches="tight", pad_inches=0.08)
    _make_svg_theme_aware(path)
    if close:
        plt.close(fig)
    return path


def apply_series_styles(lines: Iterable, *, color: str | None = None) -> None:
    for i, line in enumerate(lines):
        style = SERIES_STYLES[i % len(SERIES_STYLES)]
        line.set_linestyle(style["linestyle"])
        line.set_linewidth(style["linewidth"])
        if color is not None:
            line.set_color(color)
