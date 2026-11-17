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
NOTE = "values read off the published figure"


def note(ax, text=NOTE):
    ax.text(0.995, 0.02, text, transform=ax.transAxes, ha="right", va="bottom",
            fontsize=6.5, style="italic", color=GREY)


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf")
    plt.close(fig)


def luminance_text(c):
    r, g, b = matplotlib.colors.to_rgb(c)
    return "white" if 0.299 * r + 0.587 * g + 0.114 * b < 0.62 else "black"


# ---------- fig1 ----------
def fig1():
    rows = [
        ("(a) Tables", [("1 (96.9%)", 96.9), ("2", 3.1)]),
        ("(b) Rows", [("0 (12.1%)", 12.1), ("1–5 (84.9%)", 84.9), ("6–50", 2.0), ("50+", 1.0)]),
        ("(c) Transactions", [("1 (12.5%)", 12.5), ("2 (56.2%)", 56.2), ("3 (21.9%)", 21.9), ("4", 3.1), ("5", 6.3)]),
        ("(d) Statements", [("1 (45.3%)", 45.3), ("2–3 (26.7%)", 26.7), ("4–5 (24.0%)", 24.0), ("6–10", 4.0)]),
    ]
    cols = [BLUE, ORANGE, GREEN, PURPLE, GREY]
    fig, ax = plt.subplots(figsize=(W, 2.5))
    # leader offsets (dx, dy) in data units for narrow segments, keyed by (row, seg)
    lead = {(0, 1): (6, 0), (1, 0): (-1, 0.52), (1, 2): (-1, -0.52), (1, 3): (6.5, 0), (2, 0): (-1, 0.52),
            (2, 3): (-2, -0.52), (3, 2): (0, -0.52), (3, 3): (6.5, 0)}
    for y, (_, segs) in enumerate(rows):
        left = 0.0
        for i, (lab, w) in enumerate(segs):
            c = cols[i]
            ax.barh(y, w, left=left, height=0.5, color=c, edgecolor="white", linewidth=0.6)
            mid = left + w / 2
            if (y, i) in lead:
                dx, dy = lead[(y, i)]
                tx, ty = mid + dx, y + dy
                ax.annotate(lab, xy=(mid, y + (0.25 if dy < 0 else 0)), xytext=(tx, ty),
                            ha="center", va="center", fontsize=8,
                            arrowprops=dict(arrowstyle="-", lw=0.5, color=GREY,
                                            shrinkA=1, shrinkB=0))
            else:
                ax.text(mid, y, lab, ha="center", va="center", fontsize=8, color=luminance_text(c))
            left += w
    ax.set_yticks(range(4)); ax.set_yticklabels([r[0] for r in rows])
    ax.invert_yaxis(); ax.set_xlim(0, 112); ax.set_ylim(3.85, -0.75)
    ax.set_xticks(range(0, 101, 20))
    ax.set_xlabel("Share of test cases (%)")
    ax.grid(False); ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color="#DDDDDD", lw=0.6)
    note(ax, NOTE + "; row (b) tail labels uncertain")
    ax.texts[-1].set_position((0.995, 0.0))
    save(fig, "fig1")


DEPTH = list(range(1, 16, 2))


def lineplot_axes(ax, xlabel="MaxDepth (nesting depth of generated expressions)"):
    ax.set_xticks(DEPTH); ax.set_xlabel(xlabel)


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
    note(a, NOTE); note(b, NOTE)
    a.texts[-1].set_position((0.02, 0.88)); a.texts[-1].set_va("top"); a.texts[-1].set_ha("left")
    b.texts[-1].set_position((0.98, 0.88)); b.texts[-1].set_va("top")
    fig.tight_layout(h_pad=0.8)
    save(fig, "fig2")


# ---------- fig3 ----------
def fig3():
    plans = [7800, 6400, 5050, 4250, 3280, 2640, 1740, 1180]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    ax.plot(DEPTH, plans, color=BLUE, marker="o")
    lineplot_axes(ax, "MaxDepth (nesting depth)"); ax.set_ylabel("Unique query plans (count)"); ax.set_ylim(0, 8800)
    note(ax)
    save(fig, "fig3")


# ---------- fig4 ----------
def fig4():
    types = ["CREATE TABLE", "ALTER TABLE", "INSERT", "REPLACE", "SELECT"]
    cols = [GARNET, GREEN, PURPLE, ORANGE, BLUE]
    data = [("MySQL", [1, 0, 1, 0, 12]), ("MariaDB", [1, 1, 1, 1, 3]),
            ("CockroachDB", [0, 0, 0, 0, 1]), ("TiDB", [0, 0, 0, 0, 7]),
            ("All DBMSs (29 bugs)", [2, 1, 2, 1, 23])]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    for y, (_, cnt) in enumerate(data):
        left = 0
        for n, c in enumerate(cnt):
            if not c:
                continue
            ax.barh(y, c, left=left, height=0.55, color=cols[n], edgecolor="white", linewidth=0.6)
            ax.text(left + c / 2, y, str(c), ha="center", va="center", fontsize=8,
                    color=luminance_text(cols[n]))
            left += c
        ax.text(left + 0.4, y, f"{left}", ha="left", va="center", fontsize=8, fontweight="bold")
    ax.set_yticks(range(5)); ax.set_yticklabels([d[0] for d in data])
    ax.invert_yaxis(); ax.set_xlim(0, 31)
    ax.axhline(3.5, color=GREY, lw=0.6, ls=":")
    ax.set_xlabel("Bug-revealing statements (count; bold = DBMS total)")
    ax.grid(False); ax.grid(axis="x", color="#DDDDDD", lw=0.6); ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.legend([plt.Rectangle((0, 0), 1, 1, color=c) for c in cols], types, ncol=3, loc="lower center",
              bbox_to_anchor=(0.5, 1.0), handlelength=0.9, columnspacing=0.9, handletextpad=0.4,
              fontsize=7)
    save(fig, "fig4")


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
    note(ax)
    save(fig, "fig5")


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5):
        f()
