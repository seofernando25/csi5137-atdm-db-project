"""PySR symbolic regression on curves relative to depth 1 (x = MaxDepth, y = value/value at depth 1).
Run with the venv python: /tmp/claude-1000/venv-pysr/bin/python pysr_fit.py"""
import json, sys
import numpy as np
from pysr import PySRRegressor
sys.path.insert(0, ".")
from common import *
us, tests = load()
targets = {"ours_time": us.mean(0), "pub_time": PUB_US, "ours_tests": tests.mean(0), "pub_tests": PUB_TESTS}
X = PD.reshape(-1, 1).astype(float)
out = {}
for k, v in targets.items():
    y = v / v[0]
    m = PySRRegressor(niterations=1000, timeout_in_seconds=55, binary_operators=["+", "-", "*", "/"],
                      unary_operators=["exp", "log"], maxsize=9, populations=15, parallelism="serial",
                      deterministic=True, random_state=0, verbosity=0, progress=False, temp_equation_file=True,
                      model_selection="best")
    m.fit(X, y)
    eqs = m.equations_[["complexity", "loss", "equation"]]
    out[k] = {"best": str(m.sympy()), "pareto": eqs.to_dict("records")}
    print(k, "best:", out[k]["best"]); print(eqs.to_string(index=False), flush=True)
json.dump(out, open("pysr_results.json", "w"), indent=1, default=str)
