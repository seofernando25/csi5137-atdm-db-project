"""Recreate report figures 1-5 from values read off the published papers' figures.

Values marked "read off" are visual estimates; only numbers printed in the
papers' text or labels are exact. Run: python make_figures.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
DPI = 200

# Okabe-Ito colorblind-safe palette.
BLUE, ORANGE, GREEN, PURPLE, VERMILLION, SKY, YELLOW = (
    "#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9", "#F0E442")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelsize": 12,
    "legend.frameon": False,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


def stacked_hbar(ax, rows, colors, min_label_pct=6.0):
    """rows: list of (row_label, [(segment_label, width_pct), ...])."""
    for y, (_, segs) in enumerate(rows):
        left = 0.0
        for i, (label, width) in enumerate(segs):
            ax.barh(y, width, left=left, height=0.6, color=colors[i % len(colors)],
                    edgecolor="white", linewidth=0.8)
            if width >= min_label_pct:
                ax.text(left + width / 2, y, label, ha="center", va="center", fontsize=10)
            else:
                ax.text(left + width / 2, y + 0.42, label, ha="center", va="bottom", fontsize=9)
            left += width
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of test cases (%)")


# Fig 1: triggering-condition distributions (WriteCheck). Percentages printed in
# the original are exact; the remaining segment widths fill the remainder of 100%.
# Tail label of row (b) is partly illegible in the original ("50+" as read).
def fig1():
    rows = [
        ("(a) Tables", [("1 (96.9%)", 96.9), ("2", 3.1)]),
        ("(b) Rows", [("0 (12.1%)", 12.1), ("1-5 (84.9%)", 84.9), ("", 2.0), ("", 1.0)]),  # tail labels drawn at right edge below
        ("(c) Transactions", [("1 (12.5%)", 12.5), ("2 (56.2%)", 56.2), ("3 (21.9%)", 21.9),
                              ("4", 3.1), ("5", 6.3)]),
        ("(d) Statements", [("1 (45.3%)", 45.3), ("2-3 (26.7%)", 26.7), ("4-5 (24.0%)", 24.0),
                            ("6-10", 4.0)]),
    ]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    stacked_hbar(ax, rows, [BLUE, VERMILLION, GREEN, PURPLE, SKY])
    # Row (b) tail segments are too narrow for inside labels; label them at the right edge.
    ax.text(101.5, 1 - 0.14, "5", ha="left", va="center", fontsize=10)
    ax.text(101.5, 1 + 0.14, "50+", ha="left", va="center", fontsize=10)
    ax.set_xlim(0, 108)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel("Share of test cases (%)")
    save(fig, "fig1.png")


# Fig 2: CODDTest expression-depth experiment. Curves are read off; the text
# figures (9.91x time increase, 89.4% fewer tests) are not reproduced exactly.
def fig2():
    depth = list(range(1, 16, 2))
    exec_us = [49, 58, 74, 98, 138, 207, 330, 535]          # read off, microseconds
    tests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]  # read off, x10^9
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4))
    a.plot(depth, exec_us, color=BLUE, lw=3, marker="o", ms=4)
    a.set_xlabel(r"$\it{MaxDepth}$")
    a.set_ylabel("Execution time per query (µs)")
    a.set_xticks(depth)
    b.plot(depth, tests, color=BLUE, lw=3, marker="o", ms=4)
    b.set_xlabel("MaxDepth")
    b.set_ylabel("Completed tests (×10$^9$)")
    b.set_xticks(depth)
    b.set_ylim(0, 1.25)
    for ax in (a, b):
        ax.grid(axis="y", color="#DDDDDD", lw=0.8)
        ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig2.png")


# Fig 3: unique query plans vs MaxDepth (fixed-budget run). Values read off.
def fig3():
    depth = list(range(1, 16, 2))
    plans = [7800, 6400, 5050, 4250, 3280, 2640, 1740, 1180]
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.plot(depth, plans, color=BLUE, lw=3, marker="o", ms=4)
    ax.set_xlabel("MaxDepth")
    ax.set_ylabel("Unique query plans")
    ax.set_xticks(depth)
    ax.set_ylim(0, 8500)
    ax.grid(axis="y", color="#DDDDDD", lw=0.8)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig3.png")


# Fig 4: DDLCheck bug-revealing statements per DBMS. Counts printed in the
# original; per-DBMS totals are the sums of the printed segments.
def fig4():
    types = ["CREATE TABLE", "ALTER TABLE", "INSERT", "REPLACE", "SELECT"]
    colors = [VERMILLION, YELLOW, PURPLE, ORANGE, SKY]
    data = [
        ("MySQL", [1, 0, 1, 0, 12]),
        ("MariaDB", [1, 1, 1, 1, 3]),
        ("CockroachDB", [0, 0, 0, 0, 1]),
        ("TiDB", [0, 0, 0, 0, 7]),
        ("Total (29 bugs)", [2, 1, 2, 1, 23]),
    ]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    for y, (_, counts) in enumerate(data):
        left = 0
        for c, n, col in zip(counts, range(len(types)), colors):
            if counts[n] == 0:
                continue
            ax.barh(y, counts[n], left=left, height=0.6, color=col,
                    edgecolor="white", linewidth=0.8)
            ax.text(left + counts[n] / 2, y, str(counts[n]), ha="center", va="center", fontsize=11)
            left += counts[n]
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels([d[0] for d in data])
    ax.invert_yaxis()
    ax.set_xlabel("Number of bug-revealing statements")
    ax.set_xlim(0, 30)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colors]
    ax.legend(handles, types, ncol=5, loc="lower center", bbox_to_anchor=(0.45, 1.0),
              fontsize=10, handlelength=1.2, columnspacing=1.2)
    fig.tight_layout()
    save(fig, "fig4.png")


# Fig 5: Radar vs Radar_rand unique bugs over 12 h on TiDB. Curves are read off;
# final counts (19 and 12) are the values shown in the original.
def fig5():
    radar_t = [0.05, 0.1, 0.25, 0.4, 0.6, 0.9, 1.0, 1.05, 1.15, 1.5, 1.6, 1.9,
               2.6, 4.2, 4.4, 5.8, 7.1, 10.8]
    radar_b = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    rand_t = [0.0, 0.05, 0.1, 0.5, 0.6, 1.7, 1.9, 2.5, 4.3, 5.0, 11.4, 11.9]
    rand_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(radar_t, radar_b, color=BLUE, lw=2, marker="o", ms=5, label="Radar")
    ax.plot(rand_t, rand_b, color=ORANGE, lw=2, marker="o", ms=5,
            label="Radar$_{rand}$ (no metadata-oriented optimization)")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Unique bugs")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 20)
    ax.set_xticks(range(0, 13, 2))
    ax.grid(color="#DDDDDD", lw=0.8)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", fontsize=9)
    fig.tight_layout()
    save(fig, "fig5.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
