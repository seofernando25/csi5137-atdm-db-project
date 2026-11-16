"""Fit candidate scaling laws to MaxDepth curves (ours mean over seeds, published read-off).
Fit in log space: log y = log f(d). AIC = n ln(RSS/n) + 2k on log residuals. n=8, so model selection is weak."""
import json
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import *
d = PD.astype(float)
MODELS = {
  "linear":      (lambda d, a, b: a + b * d, [1, 1]),
  "power":       (lambda d, a, b: a * d ** b, [1, 1]),
  "exp":         (lambda d, a, b: a * np.exp(b * d), [1, .1]),
  "exp+const":   (lambda d, a, b, c: a * np.exp(b * d) + c, [1, .1, 0]),
  "quadratic":   (lambda d, a, b, c: a + b * d + c * d * d, [1, 1, 0]),
}
def fit_all(y):
    from scipy.optimize import least_squares
    y = np.asarray(y, float); s = y[0]; yn = y / s          # fit on curve relative to depth 1, in log space
    rng = np.random.default_rng(0); out = {}
    for name, (f, p0) in MODELS.items():
        def res(p):
            return np.log(np.maximum(f(d, *p), 1e-9)) - np.log(yn)
        best = None
        for t in range(40):
            start = np.array(p0, float) * (1 if t == 0 else rng.lognormal(0, 1, len(p0)) * rng.choice([-1, 1], len(p0)))
            try:
                r = least_squares(res, start, max_nfev=2000)
            except Exception:
                continue
            if best is None or r.cost < best.cost:
                best = r
        p = best.x; pred = f(d, *p)
        if np.any(pred <= 0):
            out[name] = {"error": "non-positive prediction"}; continue
        rss = float(np.sum(res(p) ** 2)); n = len(d); k = len(p)
        out[name] = {"params_rel_to_depth1": p.tolist(), "rmse_log": float(np.sqrt(rss / n)),
                     "aic": float(n * np.log(rss / n) + 2 * k), "pred": (pred * s).tolist()}
    return out
us, tests = load()
data = {"ours_time_us": us.mean(0), "pub_time_us": PUB_US, "ours_tests": tests.mean(0), "pub_tests": PUB_TESTS}
res = {k: fit_all(v) for k, v in data.items()}
fig, ax = plt.subplots(2, 2, figsize=(11, 8))
for i, (k, v) in enumerate(data.items()):
    a = ax.flat[i]; a.semilogy(d, v, "ko", label="data")
    ok = {m: r for m, r in res[k].items() if "aic" in r}
    best = sorted(ok, key=lambda m: ok[m]["aic"])
    for m in best[:3]:
        a.semilogy(d, ok[m]["pred"], lw=1.8, label=f"{m} (AIC {ok[m]['aic']:.1f})")
    a.set_title(k, fontsize=10); a.set_xlabel("MaxDepth"); a.legend(fontsize=8); a.grid(color="#DDD")
fig.tight_layout(); fig.savefig(D / "fig_scaling.png", dpi=160)
for k in res:
    for m in res[k]:
        res[k][m].pop("pred", None)
(D / "fits.json").write_text(json.dumps(res, indent=1))
lines = ["# Scaling fits (fit on curve relative to depth 1; AIC on log residuals; n=8 points, weak model selection)\n"]
for k in res:
    lines.append(f"\n## {k}\n\n| model | params (a,b,c) | RMSE(log) | AIC |\n|---|---|---|---|")
    for m, r in sorted(res[k].items(), key=lambda kv: kv[1].get("aic", 1e9)):
        lines.append(f"| {m} | " + (", ".join(f"{x:.4g}" for x in r["params_rel_to_depth1"]) + f" | {r['rmse_log']:.4f} | {r['aic']:.2f} |" if "aic" in r else f"failed: {r['error']} | | |"))
(D / "fits.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
