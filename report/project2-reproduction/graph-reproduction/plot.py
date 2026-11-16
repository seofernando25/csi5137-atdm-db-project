"""Mean with min-max over seeds (SQLite 3.42.0.0, 10 threads x 40 s) vs published Fig 2 read-off."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import *
us, tests = load()
n = len(us)
BLUE, ORANGE = "#0072B2", "#D55E00"
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
def err(a, y):
    return a.errorbar(PD, y.mean(0), yerr=[y.mean(0) - y.min(0), y.max(0) - y.mean(0)], color=ORANGE, lw=2.5, marker="s", ms=4, capsize=3)
for col, (y, pub, name) in enumerate(((us, PUB_US, "time per query"), (tests, PUB_TESTS, "completed tests"))):
    a = ax[0][col]
    a.plot(PD, pub / pub[0], color=BLUE, lw=2.5, marker="o", ms=4, label="published (read off)")
    r = y / y[:, [0]]
    a.errorbar(PD, r.mean(0), yerr=[r.mean(0) - r.min(0), r.max(0) - r.mean(0)], color=ORANGE, lw=2.5, marker="s", ms=4, capsize=3, label=f"reproduced: mean, min-max of {n} seeds")
    a.set_title(f"Fig 2{'ab'[col]}: {name} (relative to depth 1)", fontsize=10); a.legend(fontsize=8)
    b = ax[1][col]; err(b, y)
    b.set_ylabel("µs per query" if col == 0 else "completed tests per 40 s")
    b.set_title(f"Reproduced {name}, absolute", fontsize=10)
for a in ax.flat:
    a.set_xlabel("MaxDepth"); a.set_xticks(PD); a.grid(axis="y", color="#DDD")
fig.suptitle("CODDTest Fig 2 reproduction: SQLite 3.42.0, 10 threads x 40 s per depth, SQLancer PR #1054", fontsize=10)
fig.tight_layout(); fig.savefig(D / "fig2_reproduction.png", dpi=160)
print(n, "seeds; time ratio per seed", (us[:, -1] / us[:, 0]).round(2), "tests change % per seed", (100 * (tests[:, -1] / tests[:, 0] - 1)).round(1))
print("mean us", us.mean(0).round(1), "mean tests", tests.mean(0).round(0))
