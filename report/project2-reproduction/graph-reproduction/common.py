import re
from pathlib import Path
import numpy as np
D = Path(__file__).resolve().parent
PD = np.arange(1, 16, 2)
PUB_US = np.array([49, 58, 74, 98, 138, 207, 330, 535.])          # read off Fig 2a
PUB_TESTS = np.array([1.15, 1.00, 0.87, 0.72, 0.54, 0.37, 0.22, 0.12])  # x1e9, read off Fig 2b
SEEDS = {1: "raw/metrics_sqlite_seed1.txt", 2: "raw_s2/metrics_sqlite.txt", 3: "raw_s3/metrics_sqlite.txt"}
def load():
    us, tests = [], []
    for s, f in SEEDS.items():
        p = D / f
        if not p.exists():
            continue
        rows = [{k: int(v) for k, v in re.findall(r"(\w+)=(\d+)", l)} for l in p.read_text().splitlines()]
        if len(rows) < 8:
            continue
        us.append([r["query_nanos"] / r["queries"] / 1000 for r in rows])
        tests.append([r["completed"] for r in rows])
    return np.array(us), np.array(tests, float)
