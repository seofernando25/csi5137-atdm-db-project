"""Build all data figures (vector PDF, one style). Run: /usr/bin/python3.14 make_data_figures.py

fig1-fig5: values read off the published figures (exact where printed in the
papers).
"""
import json, sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
plt.style.use(HERE / "paper.mplstyle")

BLUE, ORANGE, GREEN, PURPLE, GREY, GARNET = "#2B6CB0", "#D9822B", "#2F855A", "#8E5EA2", "#7A7A7A", "#8F001A"
W = 3.3


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf")
    plt.close(fig)


def luminance_text(c):
    r, g, b = matplotlib.colors.to_rgb(c)
    return "white" if 0.299 * r + 0.587 * g + 0.114 * b < 0.62 else "black"


# ---------- fig2 ----------
def fig2():
    us = [49, 58, 74, 98, 138, 207, 330, 535]
    tests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]
    fig, (a, b) = plt.subplots(2, 1, figsize=(W, 4.4))
    a.plot(DEPTH, us, color=BLUE, marker="o"); a.set_ylabel("Execution time per query (µs)")
    b.plot(DEPTH, tests, color=BLUE, marker="o"); b.set_ylabel("Completed tests (×10$^9$)")
    b.set_ylim(0, 1.3); a.set_ylim(0, 600)
    for ax, l in ((a, "(a)"), (b, "(b)")):
        lineplot_axes(ax, "" if l == "(a)" else "MaxDepth (expression nesting)")
        ax.text(-0.02, 1.04, l, transform=ax.transAxes, fontweight="bold", ha="right")
    a.tick_params(axis="x", labelbottom=False, length=0)
    fig.tight_layout(h_pad=0.8)
    save(fig, "fig2")


# ---------- fig3 ----------
def fig3():
    plans = [7800, 6400, 5050, 4250, 3280, 2640, 1740, 1180]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    ax.plot(DEPTH, plans, color=BLUE, marker="o")
    lineplot_axes(ax, "MaxDepth (nesting depth)"); ax.set_ylabel("Unique query plans (count)"); ax.set_ylim(0, 8800)
    save(fig, "fig3")


# ---------- fig5 ----------
def fig5():
    rt = [0.05, 0.1, 0.25, 0.4, 0.6, 0.9, 1.0, 1.05, 1.15, 1.5, 1.6, 1.9, 2.6, 4.2, 4.4, 5.8, 7.1, 10.8]
    rt = rt + [12.0]
    rb = list(range(2, 20)) + [19]
    qt = [0.0, 0.05, 0.1, 0.5, 0.6, 1.7, 1.9, 2.5, 4.3, 5.0, 11.4, 11.9]
    qb = list(range(1, 13))
    fig, ax = plt.subplots(figsize=(W, 3.0))
    ax.plot(rt, rb, color=BLUE, marker="o", label="Radar")
    ax.plot(qt, qb, color=ORANGE, marker="s", clip_on=False, label="Radar$_{rand}$")
    ax.plot([12, 12], [19, 19]); 
    ax.lines[-1].remove()
    for t, b, c in ((rt[-1], 19, BLUE), (qt[-1], 12, ORANGE)):
        ax.annotate(str(b), (t, b), xytext=(5, 0), textcoords="offset points", va="center", color=c, fontweight="bold")
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 21); ax.set_xticks(range(0, 13, 2))
    ax.set_xlabel("Time on TiDB (hours)"); ax.set_ylabel("Unique bugs found (count)")
    ax.grid(axis="x", color="#DDDDDD", lw=0.6)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.98))
    save(fig, "fig5")


if __name__ == "__main__":
    for f in (fig2, fig3, fig5):
        f()
