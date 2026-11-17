"""Build the data figures as vector PDFs in one style. Run: python3 make_data_figures.py

Values are read off the published figures or copied from the papers' tables; the captions in
sec_b.tex name each source.
"""

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


def end_label(ax, x, y, text, color, dx=5, dy=0, **kw):
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", va="center",
                ha="left", color=color, annotation_clip=False, **kw)


def fig2():
    """CODDTest depth sweep: cost per query and completed tests against MaxDepth."""
    us = [49, 58, 74, 98, 138, 207, 330, 535]
    tests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]
    fig, (a, b) = plt.subplots(2, 1, figsize=(W, 3.5), sharex=True)
    a.plot(DEPTH, us, color=ORANGE, marker="o", mec="white", mew=0.6)
    b.plot(DEPTH, tests, color=BLUE, marker="o", mec="white", mew=0.6)
    a.set_ylim(0, 620)
    b.set_ylim(0, 1.3)
    panel_title(a, "a", "Execution time per query (µs)")
    panel_title(b, "b", "Completed tests in 24 h (billions)")
    end_label(a, DEPTH[-1], us[-1], f"{us[-1]} µs", ORANGE_TXT)
    end_label(b, DEPTH[-1], tests[-1], f"{tests[-1]:.2f} B", BLUE)
    b.set_xticks(DEPTH)
    b.set_xlabel("MaxDepth (expression nesting)")
    a.tick_params(axis="x", length=0)
    fig.subplots_adjust(hspace=0.45)
    save(fig, "fig2")


def fig3():
    """CODDTest: unique query plans against MaxDepth in the fixed-budget run."""
    plans = [7800, 6400, 5050, 4250, 3280, 2640, 1740, 1180]
    fig, ax = plt.subplots(figsize=(W, 2.2))
    ax.plot(DEPTH, plans, color=BLUE, marker="o", mec="white", mew=0.6)
    ax.fill_between(DEPTH, plans, color=BLUE, alpha=0.08, lw=0)
    ax.set_ylim(0, 8800)
    ax.set_xticks(DEPTH)
    ax.set_xlabel("MaxDepth (nesting depth)")
    ax.set_ylabel("Unique query plans")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v / 1000:.0f}k" if v else "0"))
    save(fig, "fig3")


def fig4():
    """24-hour efficiency: tests run against unique plans reached, per oracle configuration."""
    rows = [  # name, tests (millions), unique plans, is CODDTest, label offset (points)
        ("NoREC", 2086.6, 172_808, False, (-6, 7)),
        ("TLP", 976.2, 137_743, False, (6, 6)),
        ("DQE", 441.4, 486, False, (6, 0)),
        ("CODDTest", 497.1, 2_577_603, True, (6, -2)),
        ("expressions only", 1423.1, 7_399, True, (6, 0)),
        ("subqueries only", 423.3, 2_755_619, True, (-6, 0)),
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
    for build in (fig2, fig3, fig4, fig5):
        build()
