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
    fig, axes = plt.subplots(1, 4, figsize=(7.0, 1.75), sharex=True)
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


def fig_depth():
    """CODDTest depth sweep (expression-only, one 24 h run per setting), indexed to MaxDepth 1.
    Curve values read off the published Figs. 2 and 3; end labels use the paper's exact text."""
    us = [49, 58, 74, 98, 138, 207, 330, 535]
    tests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]
    plans = [7.8, 6.4, 5.05, 4.25, 3.28, 2.64, 1.74, 1.18]
    fig, ax = plt.subplots(figsize=(W, 2.05))
    ax.axhline(1, color="#9A9A9A", lw=0.8, zorder=1)
    ax.axvline(3, color="#BDBDBD", lw=0.7, ls=(0, (2, 2)), zorder=1)
    ax.text(3.2, 0.072, "SQLancer default", fontsize=6.6, color="#6E6E6D", va="bottom")
    series = [(us, ORANGE, ORANGE_TXT, "time per query  ×9.9"),
              (tests, BLUE, BLUE, "tests completed  −89%"),
              (plans, "#56A0D3", "#2B6CB0", "unique plans  −85%")]
    for ys, col, tcol, lab in series:
        rel = [v / ys[0] for v in ys]
        ax.plot(DEPTH, rel, color=col, marker="o", mec="white", mew=0.6, zorder=3)
        end_label(ax, DEPTH[-1], rel[-1], lab, tcol, dx=6, fontsize=7.2, fontweight="bold")
    ax.set_yscale("log")
    ax.set_ylim(0.07, 16)
    ax.set_yticks([0.1, 0.25, 0.5, 1, 2, 5, 10])
    ax.set_yticklabels(["0.1×", "0.25×", "0.5×", "1×", "2×", "5×", "10×"])
    ax.minorticks_off()
    ax.set_xlim(0.5, 15.5)
    ax.set_xticks(DEPTH)
    ax.set_xlabel("MaxDepth (maximum expression nesting)")
    ax.set_ylabel("relative to depth 1")
    save(fig, "fig_depth")


def fig_ablation():
    """a: Radar on TiDB, cumulative unique bugs with and without guidance (read off Fig. 7).
    b: every with/without ablation pair the papers report (DDLCheck Table 3, Radar Table 3)."""
    rt = [0.05, 0.1, 0.25, 0.4, 0.6, 0.9, 1.0, 1.05, 1.15, 1.5, 1.6, 1.9, 2.6, 4.2, 4.4, 5.8, 7.1,
          10.8, 12.0]
    rb = list(range(2, 20)) + [19]
    qt = [0.0, 0.05, 0.1, 0.5, 0.6, 1.7, 1.9, 2.5, 4.3, 5.0, 11.4, 11.9, 12.0]
    qb = list(range(1, 13)) + [12]
    fig, (a, b) = plt.subplots(2, 1, figsize=(W, 3.25), gridspec_kw=dict(height_ratios=[1.35, 1]))
    a.step([0] + rt, [0] + rb, where="post", color=BLUE, lw=1.6)
    a.step([0] + qt, [0] + qb, where="post", color=GREY, lw=1.6)
    end_label(a, 12, 19, "guided  19", BLUE, fontweight="bold", fontsize=7.4)
    end_label(a, 12, 12, "random  12", "#5A5A59", fontweight="bold", fontsize=7.4)
    a.annotate("gap opens within\nthe first two hours", xy=(1.9, 13), xytext=(3.6, 4.2),
               fontsize=6.8, color="#4A4A49",
               arrowprops=dict(arrowstyle="-", color="#8A8A8A", lw=0.6, shrinkB=2))
    a.set_xlim(0, 12)
    a.set_ylim(0, 21)
    a.set_xticks(range(0, 13, 2))
    a.set_xlabel("hours on TiDB", labelpad=1)
    panel_title(a, "a", "Radar, cumulative unique bugs")
    rows = [("DDLCheck filter, 6 DBMSs, 24 h each", 5, 8), ("Radar guidance, 5 DBMSs, 12 h each", 14, 22),
            ("Radar guidance, TiDB alone", 12, 19)]
    for i, (lab, lo, hi) in enumerate(rows):
        y = len(rows) - 1 - i
        b.plot([lo, hi], [y, y], color="#C9C9C9", lw=2.2, solid_capstyle="round", zorder=1)
        b.scatter([lo], [y], s=30, color=GREY, zorder=2, lw=0)
        b.scatter([hi], [y], s=30, color=BLUE, zorder=2, lw=0)
        b.annotate(f"{lo}", (lo, y), xytext=(-5, 0), textcoords="offset points", ha="right",
                   va="center", fontsize=7, color="#5A5A59")
        b.annotate(f"{hi}", (hi, y), xytext=(5, 0), textcoords="offset points", ha="left",
                   va="center", fontsize=7, color=BLUE, fontweight="bold")
        b.text(0, y + 0.3, lab, fontsize=6.8, color="#3F3F3E", va="bottom")
    b.set_yticks([])
    b.set_xlim(0, 25)
    b.set_ylim(-0.45, len(rows) - 0.05)
    b.grid(axis="y", visible=False)
    b.grid(axis="x", color="#E3E3E3", lw=0.6)
    b.set_xlabel("unique bugs without (grey) and with (blue)", labelpad=1)
    panel_title(b, "b", "Ablation pairs reported in the papers")
    fig.subplots_adjust(hspace=0.62, left=0.09, right=0.80)
    save(fig, "fig_ablation")


def fig_units():
    """One square per reported bug. Sources: CODDTest Table 1; DDLCheck Table 2;
    Radar Table 2 and Sec. 4.2; WriteCheck Table 2 and Sec. 6.2."""
    LIGHT = "#A9CDE8"
    rows = [  # paper, target, other confirmed, not confirmed, target label, raw-report note
        ("CODDTest", 24, 21, 0, "logic", ""),
        ("DDLCheck", 21, 8, 5, "schema", ""),
        ("Radar", 30, 8, 4, "metadata", "from 1,663 raw reports"),
        ("WriteCheck", 11, 2, 9, "new critical", "from 101 raw violations"),
    ]
    per_row, sz, gap = 23, 1.0, 0.24
    fig, ax = plt.subplots(figsize=(W, 2.45))
    y0 = 0
    for paper, tgt, oth, unc, tlab, note in rows:
        cells = ["t"] * tgt + ["o"] * oth + ["u"] * unc
        for k, c in enumerate(cells):
            cx = (k % per_row) * (sz + gap)
            cy = y0 - (k // per_row) * (sz + gap)
            if c == "u":
                ax.add_patch(plt.Rectangle((cx, cy), sz, sz, fc="white", ec="#9A9A9A", lw=0.6))
            else:
                ax.add_patch(plt.Rectangle((cx, cy), sz, sz, lw=0,
                                           fc=BLUE if c == "t" else LIGHT))
        n = len(cells)
        ax.text(-0.9, y0 + sz / 2 - (0.62 if n > per_row else 0), paper, ha="right", va="center",
                fontsize=7.6, fontweight="bold")
        ax.text(per_row * (sz + gap) + 0.4, y0 + sz / 2, f"{n}", ha="left", va="center",
                fontsize=8, fontweight="bold", color=INK)
        lab = f"{tgt} {tlab}" + (f" · {note}" if note else "")
        rows_used = (n - 1) // per_row + 1
        ax.text(0, y0 - rows_used * (sz + gap) + 0.12, lab, ha="left", va="top", fontsize=6.6,
                color="#4A4A49", style="italic")
        y0 -= rows_used * (sz + gap) + 2.75
    for (lx, fc, ec, lab) in ((0, BLUE, "none", "target class"), (10.0, LIGHT, "none", "other confirmed"),
                              (22.2, "white", "#9A9A9A", "unconfirmed")):
        ax.add_patch(plt.Rectangle((lx, 2.4), sz, sz, fc=fc, ec=ec, lw=0.6))
        ax.text(lx + sz + 0.4, 2.4 + sz / 2, lab, va="center", fontsize=6.8)
    ax.set_xlim(-7.4, per_row * (sz + gap) + 2.4)
    ax.set_ylim(y0 + 1.6, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "fig_units")


def fig_trigger():
    """WriteCheck Fig. 2: triggering conditions of its 32 studied WSS violations. Shares read
    from the figure labels; rows are per initial table, statements per transaction."""
    axes_rows = [
        ("Tables per case", [("1", 96.9), ("2", 3.1)]),
        ("Rows per table", [("0", 12.1), ("1–5", 84.9), ("6–50", 2.0), ("50+", 1.0)]),
        ("Transactions per case", [("1", 12.5), ("2", 56.2), ("3", 21.9), ("4", 3.1), ("5", 6.3)]),
        ("Statements per transaction", [("1", 45.3), ("2–3", 26.7), ("4–5", 24.0), ("6–10", 4.0)]),
    ]
    shades = ["#08519C", "#3182BD", "#6BAED6", "#9ECAE1", "#C6DBEF"]
    fig, ax = plt.subplots(figsize=(W, 1.55))
    for r, (name, parts) in enumerate(axes_rows):
        y = len(axes_rows) - 1 - r
        x = 0
        for k, (lab, v) in enumerate(parts):
            ax.barh(y, v, left=x, height=0.62, color=shades[k], lw=0.6, edgecolor="white")
            if v >= 9:
                txt = f"{lab}: {v:.0f}%" if v >= 18 else lab
                ax.text(x + v / 2, y, txt, ha="center", va="center", fontsize=6.7,
                        color="white" if k < 2 else INK)
            x += v
        ax.text(-2, y, name, ha="right", va="center", fontsize=7)
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, len(axes_rows) - 0.5)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"])
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)
    fig.subplots_adjust(left=0.36, right=0.98)
    save(fig, "fig_trigger")


def fig_dbms():
    """Where each campaign's target bugs come from. CODDTest Table 1 (logic), DDLCheck Table 2
    (schema bugs), Radar Table 2 (metadata bugs), WriteCheck Table 3 (its 13 critical bugs).
    None = DBMS not tested."""
    dbms = ["SQLite", "MySQL", "MariaDB", "PostgreSQL", "CockroachDB", "DuckDB", "TiDB"]
    rows = [("CODDTest", [6, 1, None, None, 7, 5, 5]),
            ("DDLCheck", [0, 13, 5, 0, 1, None, 2]),
            ("Radar", [2, 3, 1, None, 0, None, 24]),
            ("WriteCheck", [0, 1, 3, 0, 0, None, 9])]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("b", ["#EEF4FA", "#08519C"])
    fig, ax = plt.subplots(figsize=(W, 1.95))
    for r, (paper, vals) in enumerate(rows):
        y = len(rows) - 1 - r
        tot = sum(v for v in vals if v)
        for c, v in enumerate(vals):
            if v is None:
                ax.add_patch(plt.Rectangle((c + 0.05, y - 0.45), 0.9, 0.9, fc="white",
                                           ec="#D0D0D0", lw=0.5, hatch="////"))
                continue
            share = v / tot
            ax.add_patch(plt.Rectangle((c + 0.05, y - 0.45), 0.9, 0.9, lw=0,
                                       fc=cmap(share ** 0.7) if v else "#F4F4F4"))
            ax.text(c + 0.5, y, str(v), ha="center", va="center", fontsize=7.2,
                    color="white" if share > 0.38 else INK, fontweight="bold" if share > 0.38 else "normal")
        ax.text(len(dbms) + 0.15, y, str(tot), ha="left", va="center", fontsize=7.2, color="#4A4A49")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=7.4)
    ax.set_xticks([c + 0.5 for c in range(len(dbms))])
    ax.set_xticklabels(dbms, fontsize=6.6, rotation=35, ha="left", rotation_mode="anchor")
    ax.xaxis.tick_top()
    ax.tick_params(length=0)
    ax.set_xlim(0, len(dbms) + 0.7)
    ax.set_ylim(-0.55, len(rows) - 0.45)
    ax.grid(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.text(len(dbms) + 0.15, len(rows) - 0.2, "total", fontsize=6.4, color="#6E6E6D", va="bottom")
    save(fig, "fig_dbms")


def fig_triage():
    """Raw reports per unique bug. CODDTest Sec. 4.2 (SQLite 3.30.0, 24 h: reports 97,003 /
    103,103 / 16 / 6,990 for 27 / 27 / 6 / 25 unique bugs); Radar Sec. 4.2 (1,663 reports,
    42 unique); WriteCheck Sec. 6.2 (101 violations, 22 unique)."""
    rows = [("NoREC", "CODDTest's SQLite run", 97003, 27, False),
            ("TLP", "CODDTest's SQLite run", 103103, 27, False),
            ("CODDTest", "CODDTest's SQLite run", 6990, 25, True),
            ("EET", "CODDTest's SQLite run", 16, 6, False),
            ("Radar", "10 rounds, 5 DBMSs", 1663, 42, True),
            ("WriteCheck", "5 rounds, 6 DBMSs", 101, 22, True)]
    rows.sort(key=lambda r: -r[2] / r[3])
    fig, ax = plt.subplots(figsize=(W, 1.85))
    for i, (name, ctx, rep, uniq, ours) in enumerate(rows):
        y = len(rows) - 1 - i
        v = rep / uniq
        ax.plot([1, v], [y, y], color="#D5D5D5", lw=1.4, zorder=1, solid_capstyle="round")
        ax.scatter([v], [y], s=34, color=BLUE if ours else GREY, zorder=2, lw=0)
        ax.annotate(f"{v:,.0f}" if v >= 10 else f"{v:.1f}", (v, y), xytext=(6, 0),
                    textcoords="offset points", va="center", fontsize=7,
                    color=BLUE if ours else INK, fontweight="bold" if ours else "normal")
        ax.annotate(f"{rep:,} / {uniq}", (v, y), xytext=(36, 0), textcoords="offset points",
                    va="center", fontsize=6.3, color="#6E6E6D")
    ax.set_xscale("log")
    ax.set_xlim(1, 3e5)
    ax.set_xticks([1, 10, 100, 1000, 10000])
    ax.set_xticklabels(["1", "10", "100", "1k", "10k"])
    ax.minorticks_off()
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=7.4)
    for lab, r in zip(ax.get_yticklabels(), rows[::-1]):
        if r[4]:
            lab.set_color(BLUE)
            lab.set_fontweight("bold")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color="#E3E3E3", lw=0.6)
    ax.tick_params(axis="x", length=0)
    ax.set_xlabel("raw reports per unique bug (log scale)", labelpad=2)
    save(fig, "fig_triage")


if __name__ == "__main__":
    for build in (fig_depth, fig4, fig_ablation, fig_homeset, fig_units, fig_trigger, fig_dbms, fig_triage):
        build()
