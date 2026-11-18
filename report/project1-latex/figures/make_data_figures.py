"""Build the data figures as vector PDFs in one style. Run: python3 make_data_figures.py

Values are read off the published figures or copied from the papers' tables; the captions in
sec_b.tex name each source.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
plt.style.use(HERE / "paper.mplstyle")

# Palette from the image-review skill; *_TXT variants pass 4.5:1 on white for text.
BLUE, ORANGE, GREY, INK = "#0072B2", "#D55E00", "#8A8A8A", "#2D2D2C"
ORANGE_TXT = "#A84800"
W = 3.3  # column width in inches
DEPTH = [1, 3, 5, 7, 9, 11, 13, 15]


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf")
    plt.close(fig)


def panel_title(ax, letter, text):
    ax.text(0, 1.06, letter, transform=ax.transAxes, fontweight="bold", fontsize=8.5,
            ha="left", va="bottom")
    ax.annotate(text, (0, 1.06), xycoords="axes fraction", xytext=(10, 0),
                textcoords="offset points", fontsize=8, va="bottom", ha="left")


def end_label(ax, x, y, text, color, dx=5, dy=0, ha="left", **kw):
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", va="center",
                ha=ha, color=color, annotation_clip=False, **kw)


def fig_depth():
    """CODDTest depth sweep (expression-only, 24 h each): cost per query rises while completed
    tests and unique plans fall. Values read off the published Figs. 2 and 3."""
    us = [49, 58, 74, 98, 138, 207, 330, 535]
    tests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]
    plans = [7.8, 6.4, 5.05, 4.25, 3.28, 2.64, 1.74, 1.18]
    fig, (a, b, c) = plt.subplots(3, 1, figsize=(W, 3.55), sharex=True)
    for ax, ys, col in ((a, us, ORANGE), (b, tests, BLUE), (c, plans, BLUE)):
        ax.plot(DEPTH, ys, color=col, marker="o", mec="white", mew=0.6)
        ax.fill_between(DEPTH, ys, color=col, alpha=0.07, lw=0)
    a.set_ylim(0, 640)
    b.set_ylim(0, 1.35)
    c.set_ylim(0, 9.2)
    a.set_yticks([0, 200, 400, 600])
    b.set_yticks([0, 0.5, 1.0])
    c.set_yticks([0, 4, 8])
    panel_title(a, "a", "Time per query (µs) rises")
    panel_title(b, "b", "Completed tests in 24 h (billions) fall")
    panel_title(c, "c", "Unique query plans (thousands) fall too")
    end_label(a, DEPTH[-1], us[-1], "535\n×9.9", ORANGE_TXT, dx=5, dy=-2)
    end_label(b, DEPTH[-1], tests[-1], "0.12\n−89%", BLUE, dx=5, dy=4)
    end_label(c, DEPTH[-1], plans[-1], "1.2k", BLUE, dx=5, dy=2)
    c.set_xlim(0.4, 17.2)
    for ax in (a, b):
        ax.tick_params(axis="x", length=0)
    c.set_xticks(DEPTH)
    c.set_xlabel("MaxDepth (maximum expression nesting)")
    fig.subplots_adjust(hspace=0.62)
    save(fig, "fig_depth")


def fig_homeset():
    """Known-bug capability studies: share of each paper's bug set that each tool reaches.
    Sources: CODDTest Table 2, DDLCheck Table 4, Radar Table 5, WriteCheck Table 3."""
    panels = [
        ("CODDTest", "its 24 logic bugs", 24, "manual",
         [("CODDTest", 24, True), ("TLP", 12, False), ("NoREC", 11, False), ("DQE", 4, False)]),
        ("DDLCheck", "its 21 schema bugs", 21, "conceptual",
         [("DDLCheck", 21, True), ("Radar", 13, False), ("DQP", 9, False), ("NoREC", 0, False)]),
        ("Radar", "its 30 metadata bugs", 30, "conceptual",
         [("Radar", 30, True), ("NoREC", 13, False), ("DQE", 8, False), ("MutaSQL", 5, False),
          ("TLP", 3, False)]),
        ("WriteCheck", "29 bugs, 13 its own", 29, "test cases",
         [("WriteCheck", 29, True), ("DT²", 23, False), ("TxCheck", 16, False),
          ("Troc", 14, False), ("Elle, Cobra, Emme", 0, False)]),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(7.0, 1.95), sharex=True)
    for ax, (paper, sub, n, how, rows) in zip(axes, panels):
        names = [r[0] for r in rows][::-1]
        vals = [r[1] for r in rows][::-1]
        own = [r[2] for r in rows][::-1]
        y = range(len(rows))
        ax.barh(y, [100] * len(rows), color="#F1F1F1", height=0.62, lw=0)
        ax.barh(y, [100 * v / n for v in vals], height=0.62, lw=0,
                color=[BLUE if o else GREY for o in own])
        for yi, v, o in zip(y, vals, own):
            share = 100 * v / n
            if o:
                ax.text(share - 3, yi, f"{v}/{n}", va="center", ha="right", fontsize=7,
                        color="white", fontweight="bold")
            else:
                ax.text(share + 3, yi, f"{v}/{n}", va="center", ha="left", fontsize=7,
                        color=INK)
        ax.set_yticks(list(y))
        ax.set_yticklabels(names, fontsize=7)
        for lab, o in zip(ax.get_yticklabels(), own):
            if o:
                lab.set_color(BLUE)
                lab.set_fontweight("bold")
        ax.set_xlim(0, 100)
        ax.set_xticks([0, 50, 100])
        ax.set_xticklabels(["0", "50", "100%"])
        ax.grid(axis="y", visible=False)
        ax.grid(axis="x", color="#E3E3E3", lw=0.6)
        ax.spines["bottom"].set_visible(False)
        ax.tick_params(axis="x", length=0)
        ax.set_title(paper, fontsize=8, loc="left", fontweight="bold", pad=14, x=-0.02)
        ax.text(-0.02, 1.03, f"{sub}; {how}", transform=ax.transAxes, fontsize=6.6,
                style="italic", color="#5A5A59", va="bottom")
    fig.subplots_adjust(wspace=1.0, left=0.085, right=0.985, top=0.78, bottom=0.12)
    save(fig, "fig_homeset")


def fig_funnel():
    """Reporting stages of each discovery campaign. Circle area grows with the count (sqrt);
    the ring marks the number each abstract leads with. Sources: CODDTest Table 1, DDLCheck
    Table 2, Radar Sec. 4.2 and Table 2, WriteCheck Table 2."""
    stages = ["Raw\nreports", "Unique,\nsubmitted", "Confirmed\n(any kind)", "New, target\nbug class"]
    rows = [  # paper, counts per stage (None = not reported), headline stage index, target label
        ("CODDTest", [None, 45, 45, 24], 1, "logic"),
        ("DDLCheck", [None, 34, 29, 21], 1, "schema"),
        ("Radar", [1663, 42, 38, 30], 1, "metadata"),
        ("WriteCheck", [101, 22, 13, 11], 1, "critical txn"),
    ]
    fig, ax = plt.subplots(figsize=(W, 2.45))
    for r, (paper, counts, head, target) in enumerate(rows):
        y = len(rows) - 1 - r
        xs = [i for i, c in enumerate(counts) if c is not None]
        ax.plot(xs, [y] * len(xs), color="#D5D5D5", lw=1.1, zorder=1)
        for i, c in enumerate(counts):
            if c is None:
                ax.scatter(i, y, s=30, facecolor="white", edgecolor="#9A9A9A", lw=0.8,
                           linestyle=(0, (2, 1.5)), zorder=2)
                ax.annotate("n/r", (i, y), xytext=(6, 0), textcoords="offset points",
                            va="center", fontsize=6.6, color="#5A5A59", style="italic")
                continue
            size = 18 * (1 + math.log10(c)) ** 2
            rad = (size / math.pi) ** 0.5
            ax.scatter(i, y, s=size, color="white", lw=0, zorder=2)
            ax.scatter(i, y, s=size, color=BLUE, alpha=0.95 if i == 3 else 0.5, lw=0, zorder=2)
            if i == head:
                ring = (rad + 3.2) ** 2 * math.pi
                ax.scatter(i, y, s=ring, facecolor="none", edgecolor=INK, lw=0.9, zorder=3)
            ax.annotate(f"{c:,}", (i, y), xytext=(0, rad + (5 if i == head else 2)),
                        textcoords="offset points", va="bottom", ha="center", fontsize=7.2,
                        fontweight="bold" if i == head else "normal", color=INK)
        ax.annotate(target, (3, y), xytext=(9, 0), textcoords="offset points", ha="left",
                    va="center", fontsize=6.6, color="#5A5A59", style="italic")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=7.5)
    ax.set_xticks(range(len(stages)))
    ax.set_xticklabels(stages, fontsize=7)
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0, pad=2)
    ax.set_xlim(-0.4, 4.05)
    ax.set_ylim(-0.4, len(rows) - 0.35)
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    save(fig, "fig_funnel")


def fig4():
    """24-hour efficiency: tests run against unique plans reached, per oracle configuration."""
    rows = [  # name, tests (millions), unique plans, is CODDTest, label offset (points)
        ("NoREC", 2086.6, 172_808, False, (-6, 7)),
        ("TLP", 976.2, 137_743, False, (6, 6)),
        ("DQE", 441.4, 486, False, (6, 0)),
        ("CODDTest", 497.1, 2_577_603, True, (7, -7)),
        ("expressions only", 1423.1, 7_399, True, (6, 0)),
        ("subqueries only", 423.3, 2_755_619, True, (-6, 6)),
    ]
    fig, ax = plt.subplots(figsize=(W, 2.45))
    for name, tests, plans, ours, (dx, dy) in rows:
        color = BLUE if ours else GREY
        ax.scatter(tests, plans, s=34 if ours else 26, color=color, edgecolor="white", lw=0.7,
                   zorder=3)
        ha = "right" if dx < 0 else "left"
        ax.annotate(name, (tests, plans), xytext=(dx, dy), textcoords="offset points",
                    ha=ha, va="center", fontsize=7.5, color=BLUE if ours else INK,
                    fontweight="bold" if name == "CODDTest" else "normal")
    ax.set_yscale("log")
    ax.set_ylim(200, 2e7)
    ax.set_xlim(-300, 2400)
    ax.set_yticks([1e3, 1e4, 1e5, 1e6, 1e7])
    ax.set_yticklabels(["1k", "10k", "100k", "1M", "10M"])
    ax.minorticks_off()
    ax.set_xlabel("Tests run in 24 h (millions)")
    ax.set_ylabel("Unique query plans (log)")
    save(fig, "fig4")


def fig5():
    """Radar on TiDB: cumulative unique bugs over 12 hours, with and without guidance."""
    rt = [0.05, 0.1, 0.25, 0.4, 0.6, 0.9, 1.0, 1.05, 1.15, 1.5, 1.6, 1.9, 2.6, 4.2, 4.4, 5.8, 7.1,
          10.8, 12.0]
    rb = list(range(2, 20)) + [19]
    qt = [0.0, 0.05, 0.1, 0.5, 0.6, 1.7, 1.9, 2.5, 4.3, 5.0, 11.4, 11.9, 12.0]
    qb = list(range(1, 13)) + [12]
    fig, ax = plt.subplots(figsize=(W, 2.4))
    ax.step([0] + rt, [0] + rb, where="post", color=BLUE, lw=1.6)
    ax.step([0] + qt, [0] + qb, where="post", color=ORANGE, lw=1.6)
    end_label(ax, 12, 19, "Radar, 19 bugs", BLUE, fontweight="bold")
    end_label(ax, 12, 12, "Radar$_{rand}$, 12", ORANGE_TXT, fontweight="bold")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 21)
    ax.set_xticks(range(0, 13, 2))
    ax.set_xlabel("Time on TiDB (hours)")
    ax.set_ylabel("Unique bugs found")
    save(fig, "fig5")


if __name__ == "__main__":
    for build in (fig_depth, fig4, fig5, fig_homeset, fig_funnel):
        build()
