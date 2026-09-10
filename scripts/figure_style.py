"""Shared Matplotlib figure style for HaSuNo0620.github.io.

Figure Style v1.2 prioritizes browser readability: large mathematical labels,
large legends, heavy data/theory strokes, and transparent figures that visually
belong to the page.
"""
from __future__ import annotations

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
            "xtick.labelsize": FONT_SIZE["tick"],
            "ytick.labelsize": FONT_SIZE["tick"],
            "axes.labelsize": FONT_SIZE["axis"],
            "legend.fontsize": FONT_SIZE["legend"],
            "legend.frameon": False,
            "font.family": "sans-serif",
            "font.sans-serif": [
                "Noto Sans JP",
                "Hiragino Sans",
                "Yu Gothic",
                "DejaVu Sans",
            ],
            "mathtext.fontset": "stix",
            "mathtext.default": "it",
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
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(COLORS["ink"])
    ax.spines["bottom"].set_color(COLORS["ink"])
    ax.tick_params(axis="both", which="major", length=5.5, width=1.4)
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


def direct_label(ax, x: float, y: float, text: str, *, color=None, **kwargs):
    defaults = {
        "fontsize": FONT_SIZE["annotation"],
        "color": color or COLORS["ink"],
        "ha": "left",
        "va": "center",
    }
    defaults.update(kwargs)
    return ax.text(x, y, text, **defaults)


def panel_label(ax, label: str, *, x: float = 0.01, y: float = 0.99) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=FONT_SIZE["panel"],
        fontweight="semibold",
        color=COLORS["ink"],
    )


def save_figure(fig, path: str | Path, *, dpi: int = 180, close: bool = True) -> Path:
    _, plt = _mpl()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, transparent=True, bbox_inches="tight", pad_inches=0.08)
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
