"""Generate figures for the consumer-choice / price-competition notes."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.optimize import root

from figure_style import (
    COLORS,
    LINEWIDTH,
    new_figure,
    save_figure,
    style_axes,
    style_legend,
)

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "public" / "figures" / "nash-bertrand-price-competition"
PQ_DIR = ROOT / "public" / "figures" / "price-quality-choice"


def capacity_residual_demand() -> None:
    c = 100.0
    n = 140
    k_a = 100
    p_a = 120.0
    vmax = 180.0

    p_b = np.linspace(100, 190, 901)
    q_b = np.where(p_b <= p_a, n, np.where(p_b <= vmax, n - k_a, 0))
    profit = (p_b - c) * q_b

    fig, ax = new_figure()
    ax.plot(p_b, profit, color=COLORS["accent"], lw=LINEWIDTH["primary"])
    ax.axvline(p_a, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":")
    ax.axvline(vmax, color=COLORS["green"], lw=LINEWIDTH["secondary"], ls="--")
    ax.scatter([120, 180], [2800, 3200], s=75, facecolor=COLORS["paper"], edgecolor=COLORS["ink"], linewidth=2)
    style_axes(ax, xlabel=r"Bの価格 $p_B$ [円]", ylabel=r"Bの利潤 $\pi_B$ [円]")
    ax.set_xlim(100, 190)
    ax.set_ylim(0, 3500)
    save_figure(fig, NB_DIR / "capacity-residual-demand.svg")


def differentiated_model():
    market = 1000.0
    alpha, beta, lam = 0.1, 1.0, 1.0
    q_a, q_b = 9.0, 7.0
    c_a, c_b = 55.0, 40.0

    def shares(p_a, p_b, qa=q_a, qb=q_b):
        e_a = np.exp(beta * qa - alpha * p_a)
        e_b = np.exp(beta * qb - alpha * p_b)
        den = 1.0 + e_a + e_b
        return e_a / den, e_b / den, 1.0 / den

    def equilibrium():
        def f(x):
            s_a, s_b, _ = shares(x[0], x[1])
            return [
                x[0] - c_a - lam / (alpha * (1 - s_a)),
                x[1] - c_b - lam / (alpha * (1 - s_b)),
            ]
        return root(f, [75, 57]).x

    p_a_star, p_b_star = equilibrium()

    def br_a(p_b):
        grid = np.linspace(45, 95, 1400)
        s_a, _, _ = shares(grid, p_b)
        return grid[np.argmax(market * (grid - c_a) * s_a)]

    def br_b(p_a):
        grid = np.linspace(35, 85, 1400)
        _, s_b, _ = shares(p_a, grid)
        return grid[np.argmax(market * (grid - c_b) * s_b)]

    p_b_grid = np.linspace(45, 75, 180)
    p_a_grid = np.linspace(60, 85, 180)
    r_a = np.array([br_a(p) for p in p_b_grid])
    r_b = np.array([br_b(p) for p in p_a_grid])

    fig, ax = new_figure(size="tall")
    ax.plot(p_b_grid, r_a, color=COLORS["accent"], lw=LINEWIDTH["primary"], label="Aのbest response")
    ax.plot(r_b, p_a_grid, color=COLORS["green"], lw=LINEWIDTH["secondary"], ls="--", label="Bのbest response")
    ax.scatter([p_b_star], [p_a_star], s=90, facecolor=COLORS["paper"], edgecolor=COLORS["ink"], linewidth=2.2, zorder=5)
    style_axes(ax, xlabel=r"Bの価格 $p_B$", ylabel=r"Aの価格 $p_A$")
    style_legend(ax, loc="upper left")
    save_figure(fig, NB_DIR / "best-response-intersection.svg")

    theta = beta / alpha
    z_a = p_a_star - theta * q_a
    z_b = p_b_star - theta * q_b

    fig, ax = new_figure()
    x = np.arange(2)
    width = 0.32
    ax.bar(x - width / 2, [p_a_star, p_b_star], width=width, color=COLORS["accent"], label=r"実価格 $p_i$")
    ax.bar(x + width / 2, [z_a, z_b], width=width, color=COLORS["green"], label=r"品質調整後 $Z_i$")
    ax.axhline(0, color=COLORS["muted"], lw=LINEWIDTH["reference"], ls=":")
    ax.set_xticks(x, ["A", "B"])
    style_axes(ax, xlabel="商品", ylabel="価格・品質調整価格")
    style_legend(ax, loc="upper right")
    save_figure(fig, NB_DIR / "price-vs-quality-adjusted-price.svg")


def price_quality_choice() -> None:
    market = 1000.0
    alpha, beta, lam = 0.1, 1.0, 1.0
    q_b = 5.0

    def cost(q):
        return 20.0 + q**2

    def shares(p_a, p_b, q_a, qb=q_b):
        e_a = np.exp(beta * q_a - alpha * p_a)
        e_b = np.exp(beta * qb - alpha * p_b)
        den = 1.0 + e_a + e_b
        return e_a / den, e_b / den

    def price_equilibrium(q_a, guess=(58, 58)):
        def f(x):
            s_a, s_b = shares(x[0], x[1], q_a)
            return [
                x[0] - cost(q_a) - lam / (alpha * (1 - s_a)),
                x[1] - cost(q_b) - lam / (alpha * (1 - s_b)),
            ]
        return root(f, guess).x

    q_grid = np.linspace(1.5, 8.5, 141)
    profit = []
    guess = (58, 58)
    for q_a in q_grid:
        p_a, p_b = price_equilibrium(q_a, guess)
        guess = (p_a, p_b)
        s_a, _ = shares(p_a, p_b, q_a)
        profit.append(market * (p_a - cost(q_a)) * s_a)

    q_star = beta / alpha / 2.0
    p_a, p_b = price_equilibrium(q_star)
    s_a, _ = shares(p_a, p_b, q_star)
    pi_star = market * (p_a - cost(q_star)) * s_a

    fig, ax = new_figure()
    ax.plot(q_grid, profit, color=COLORS["accent"], lw=LINEWIDTH["primary"])
    ax.axvline(q_star, color=COLORS["green"], lw=LINEWIDTH["secondary"], ls="--")
    ax.scatter([q_star], [pi_star], s=90, facecolor=COLORS["paper"], edgecolor=COLORS["ink"], linewidth=2.2, zorder=5)
    style_axes(ax, xlabel=r"Aの品質 $q_A$", ylabel=r"Aの利潤 $\pi_A$")
    save_figure(fig, PQ_DIR / "quality-choice-profit.svg")


if __name__ == "__main__":
    capacity_residual_demand()
    differentiated_model()
    price_quality_choice()
