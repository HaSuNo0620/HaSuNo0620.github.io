"""Shared Matplotlib figure style for HaSuNo0620.github.io.

The site treats figures as part of the page rather than as white paper panels.
Use transparent SVG output and semantic line styles documented in
`docs/figure-style.md`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt


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

LINEWIDTH = {
    "primary": 2.4,
    "secondary": 1.8,
    "reference": 1.0,
    "axis": 1.0,
    "grid": 0.7,
    "errorbar": 1.0,
}

MARKERSIZE = 5.5

# Use line style as well as color so figures remain interpretable without color.
SERIES_STYLES = (
    {"linestyle": "-", "linewidth": 2.4},
    {"linestyle": "--", "linewidth": 1.8},
    {"linestyle": ":", "linewidth": 1.8},
    {"linestyle": "-.", "linewidth": 1.8},
)


def apply_site_style() -> None:
    """Apply the global plotting defaults for the site."""
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
            "grid.alpha": 0.55,
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "axes.labelsize": 14,
            "legend.fontsize": 12,
            "legend.frameon": False,
            "font.family": "sans-serif",
            "font.sans-serif": [
                "Noto Sans JP",
                "Hiragino Sans",
                "Yu Gothic",
                "DejaVu Sans",
            ],
            "text.color": COLORS["ink"],
            "lines.solid_capstyle": "round",
            "lines.dash_capstyle": "round",
            "svg.fonttype": "none",
        }
    )


def new_figure(*, size: str = "standard", constrained_layout: bool = True):
    """Create a site-style figure and a single axes.

    Parameters
    ----------
    size:
        One of ``standard``, ``wide``, or ``tall``.
    """
    apply_site_style()
    sizes = {
        "standard": FIGSIZE,
        "wide": FIGSIZE_WIDE,
        "tall": FIGSIZE_TALL,
    }
    if size not in sizes:
        raise ValueError(f"unknown figure size: {size!r}")
    return plt.subplots(figsize=sizes[size], constrained_layout=constrained_layout)


def style_axes(
    ax,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    grid: bool = True,
    zero_x: bool = False,
    zero_y: bool = False,
) -> None:
    """Apply axis labels and the standard minimal axis treatment."""
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(COLORS["ink"])
    ax.spines["bottom"].set_color(COLORS["ink"])

    ax.tick_params(axis="both", which="major", length=4, width=0.9)
    ax.grid(grid, which="major")
    ax.grid(False, which="minor")

    if zero_x:
        ax.axvline(0, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":", zorder=0)
    if zero_y:
        ax.axhline(0, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":", zorder=0)


def plot_exact(ax, x, y, *, label: str | None = None, **kwargs):
    """Plot the primary exact/theory curve."""
    defaults = {
        "color": COLORS["accent"],
        "lw": LINEWIDTH["primary"],
        "ls": "-",
        "label": label,
    }
    defaults.update(kwargs)
    return ax.plot(x, y, **defaults)


def plot_approx(ax, x, y, *, label: str | None = None, **kwargs):
    """Plot an approximation, asymptote, or fit."""
    defaults = {
        "color": COLORS["green"],
        "lw": LINEWIDTH["secondary"],
        "ls": "--",
        "label": label,
    }
    defaults.update(kwargs)
    return ax.plot(x, y, **defaults)


def plot_data(
    ax,
    x,
    y,
    *,
    yerr=None,
    label: str | None = None,
    marker: str = "o",
    **kwargs,
):
    """Plot simulation or measured data as markers, optionally with errors."""
    defaults = {
        "fmt": marker,
        "ms": MARKERSIZE,
        "color": COLORS["ink"],
        "mec": COLORS["ink"],
        "mfc": COLORS["paper"],
        "elinewidth": LINEWIDTH["errorbar"],
        "capsize": 2.5,
        "linestyle": "none",
        "label": label,
    }
    defaults.update(kwargs)
    return ax.errorbar(x, y, yerr=yerr, **defaults)


def shade_uncertainty(ax, x, lower, upper, *, color: str | None = None, alpha: float = 0.15, **kwargs):
    """Draw a low-emphasis confidence/uncertainty band."""
    return ax.fill_between(
        x,
        lower,
        upper,
        color=color or COLORS["accent"],
        alpha=alpha,
        linewidth=0,
        **kwargs,
    )


def direct_label(ax, x: float, y: float, text: str, *, color: str | None = None, **kwargs):
    """Add a small direct curve label; prefer this to a legend when practical."""
    defaults = {
        "fontsize": 12,
        "color": color or COLORS["ink"],
        "ha": "left",
        "va": "center",
    }
    defaults.update(kwargs)
    return ax.text(x, y, text, **defaults)


def panel_label(ax, label: str, *, x: float = 0.01, y: float = 0.99) -> None:
    """Place a standard panel label such as ``(a)`` in the upper-left."""
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=13,
        fontweight="semibold",
        color=COLORS["ink"],
    )


def save_figure(fig, path: str | Path, *, dpi: int = 180, close: bool = True) -> Path:
    """Save a transparent figure. SVG is preferred for plots and diagrams."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        path,
        dpi=dpi,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.06,
    )
    if close:
        plt.close(fig)
    return path


def apply_series_styles(lines: Iterable, *, color: str | None = None) -> None:
    """Apply repeated dash patterns to a collection of line artists."""
    for i, line in enumerate(lines):
        style = SERIES_STYLES[i % len(SERIES_STYLES)]
        line.set_linestyle(style["linestyle"])
        line.set_linewidth(style["linewidth"])
        if color is not None:
            line.set_color(color)


# Apply defaults on import so small scripts can use plt directly if desired.
apply_site_style()
