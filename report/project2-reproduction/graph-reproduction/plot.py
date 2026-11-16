"""Plot reproduced CODDTest MaxDepth sweeps next to published Fig 2.
Primary: SQLite 3.42.0.0, 10 threads (raw/metrics_sqlite.txt). Supplementary: MySQL 8.0.32, 1 thread (raw/metrics.txt)."""
import re, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = Path(__file__).resolve().parent
def load(name, secs):
    rows = [{k: int(v) for k, v in re.findall(r"(\w+)=(\d+)", l)} for l in (D / "raw" / name).read_text().splitlines()]
    return {"depth": [r["depth"] for r in rows],
            "us": [r["query_nanos"] / r["queries"] / 1000 for r in rows],
            "tests": [r["completed"] for r in rows],
            "tps": [r["completed"] / secs for r in rows]}
S = load("metrics_sqlite.txt", 40)
M = load("metrics.txt", 35)
pd = list(range(1, 16, 2))
pus = [49, 58, 74, 98, 138, 207, 330, 535]
ptests = [1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12]
BLUE, ORANGE, GREY = "#0072B2", "#D55E00", "#888888"
norm = lambda y: [v / y[0] for v in y]
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
for a, key, pub, ttl in ((ax[0][0], "us", pus, "Fig 2a: time per query (relative to depth 1)"),
                         (ax[0][1], "tests", ptests, "Fig 2b: completed tests (relative to depth 1)")):
    a.plot(pd, norm(pub), color=BLUE, lw=2.5, marker="o", ms=4, label="published (read off)")
    a.plot(S["depth"], norm(S[key]), color=ORANGE, lw=2.5, marker="s", ms=4, label="reproduced: SQLite 3.42.0.0, 10 thr x 40 s")
    a.plot(M["depth"], norm(M[key]), color=GREY, lw=1.5, ls="--", marker="^", ms=4, label="supplementary: MySQL 8.0.32, 1 thr x 35 s")
    a.set_xlabel("MaxDepth"); a.set_xticks(pd); a.set_title(ttl, fontsize=10); a.grid(axis="y", color="#DDD"); a.legend(fontsize=7)
ax[1][0].plot(S["depth"], S["us"], color=ORANGE, lw=2.5, marker="s", ms=4); ax[1][0].set_ylabel("µs per query (SQLite, absolute)")
ax[1][1].plot(S["depth"], S["tps"], color=ORANGE, lw=2.5, marker="s", ms=4); ax[1][1].set_ylabel("completed tests per second (SQLite, absolute)")
for a in ax[1]:
    a.set_xlabel("MaxDepth"); a.set_xticks(pd); a.grid(axis="y", color="#DDD"); a.set_title("Reproduced (SQLite), absolute", fontsize=10)
fig.tight_layout(); fig.savefig(D / "fig2_reproduction.png", dpi=160)
summ = {"sqlite": S, "mysql": M,
        "sqlite_time_ratio_15_vs_1": S["us"][-1] / S["us"][0], "sqlite_tests_change_pct": 100 * (S["tests"][-1] / S["tests"][0] - 1),
        "published_text": {"time_ratio": 9.91, "tests_change_pct": -89.4}}
(D / "raw" / "summary.json").write_text(json.dumps(summ, indent=1))
print(json.dumps({k: v for k, v in summ.items() if k.startswith("sqlite_")}), S["us"], S["tests"])
