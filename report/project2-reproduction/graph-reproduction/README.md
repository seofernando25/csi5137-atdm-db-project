# CODDTest Fig 2 (MaxDepth sweep): reproduction

**Result.** SQLite 3.42.0, 10 threads, 40 s per depth, MaxDepth 1, 3, ..., 15, three seeds (1, 2, 3). From depth 1 to 15:

| | Reproduced (mean; per-seed range) | Published |
|---|---|---|
| Completed tests | -88.6% (-88.3 to -88.9) | -89.4% |
| Time per query | x5.58 (x5.48 to x5.78) | x9.91 (read-off curve about x10.9) |

Both curves have the published shape (monotonic fall in tests, monotonic rise in time per query). The test-count change matches within about 1 point. The time-per-query rise is about 56% of the published factor. A 40 s budget gives a trend check, not the paper's 24 h absolute numbers. Seed-to-seed spread is small (error bars in the plot are min-max over 3 seeds).

![comparison](fig2_reproduction.png)

Mean over 3 seeds:

| depth | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|---|---|
| us/query | 99.3 | 122.9 | 133.0 | 156.9 | 192.5 | 262.4 | 378.3 | 554.1 |
| completed tests / 40 s | 1,074,383 | 884,767 | 754,843 | 644,810 | 493,472 | 328,855 | 206,357 | 122,216 |

Published read-off: 49 to 535 us; tests 1.15 to 0.12 x10^9 (24 h x 10 threads). Absolute numbers are not comparable: different hardware and budget, and our time per query is the wall time of the oracle's own queries including result fetching in Java.

## Setup and what differs from the clone's defaults
- Clone: `github.com/DerZc/sqlancer` commit `3045badb83098ace249a6d5cc2f1cd3bed37b888` (sqlancer PR #1054), in `/tmp/claude-1000/ext/coddtest` (not committed).
- Oracle: `sqlite3 --oracle CODDTest --coddtest-model expression`, `--num-threads 10 --num-tries 1000000 --random-seed {1,2,3}`, `--max-expression-depth d`. Java 17 (`eclipse-temurin:17-jre`).
- Changes against the clone's defaults (all in `metrics.patch`):
  1. `pom.xml`: sqlite-jdbc `3.47.2.0` to `3.42.0.0`. This is the only intended version change.
  2. `pom.xml`: `failOnWarning` true to false (ecj warnings otherwise abort the build). No effect on behavior.
  3. `SQLite3ToStringVisitor` (CASE-mapping visitor, ~line 623): `constant.toString()` replaced by `visit(constant)`. Before this fix the SQL contained `(INT) 1` and `(BINARY) x'41d6'`, which SQLite rejects, and 0 tests completed.
  4. Counters in `SQLite3CODDTestOracle` (attempts, completed, queries, query nanos). The tool's own "Executed N queries" counter stays 0 for this oracle. "Completed" counts `check()` calls that return normally (not ignored, not a mismatch AssertionError; mismatches are not counted).
- Verified SQLite version: running `SELECT sqlite_version()` through the sqlancer jar's own classpath (manifest lists `lib/sqlite-jdbc-3.42.0.0.jar`) returns **3.42.0**. This matches the paper's SQLite 3.42.0.0 release. A stale `sqlite-jdbc-3.47.2.0.jar` also sits in `target/lib` from the first build but is not on the manifest classpath.
- The paper's exact SQLancer snapshot is unknown. The PR snapshot above may differ from it.

## Commands
```
# build (in the clone, with metrics.patch applied)
docker run --rm -v $PWD:/w -v /tmp/claude-1000/ext/m2:/root/.m2 -w /w maven:3.9.11-eclipse-temurin-17 \
  mvn -q -DskipTests -Dcheckstyle.skip -Dpmd.skip -Dspotbugs.skip package
./run_sweep_sqlite.sh /tmp/claude-1000/ext/coddtest/target 40 raw_s1    # seed 1 (stored as raw/metrics_sqlite_seed1.txt)
SEED=2 ./run_sweep_sqlite.sh /tmp/claude-1000/ext/coddtest/target 40 raw_s2
SEED=3 ./run_sweep_sqlite.sh /tmp/claude-1000/ext/coddtest/target 40 raw_s3
/usr/bin/python3.14 plot.py          # fig2_reproduction.png
/usr/bin/python3.14 scaling_fit.py   # fits.json, fits.md, fig_scaling.png
/tmp/claude-1000/venv-pysr/bin/python pysr_fit.py   # pysr_results.json
```
Seeds ran sequentially, one sweep at a time (about 6 min each). Seed 1 was run earlier with the same settings; its output is `raw/metrics_sqlite_seed1.txt`.

## Deviations
- 40 s per depth vs 24 h; 3 seeds vs one 24 h run.
- Fig 3 (unique query plans) was not attempted.
- The oracle's mismatch (bug) count was not instrumented for SQLite.

## Scaling fits (`scaling_fit.py`, `fits.md`, `fits.json`, `fig_scaling.png`)
Models: linear a+b*d, power a*d^b, exponential a*exp(b*d), exponential+constant a*exp(b*d)+c, quadratic. Each is fit to the curve relative to depth 1, by least squares in log space (40 random restarts). AIC = n ln(RSS/n) + 2k on log residuals. With n = 8 points per curve, model selection is weak: an AIC gap under about 2 to 4 should not be read as a preference, and the 3-parameter forms have only 5 degrees of freedom.

| curve | best by AIC | parameters (relative to depth 1) | RMSE(log) |
|---|---|---|---|
| ours, time per query | exp+const | 0.125*exp(0.241*d) + 0.901 | 0.034 |
| published, time per query | exp+const | 0.197*exp(0.263*d) + 0.753 | 0.010 |
| ours, completed tests | quadratic | 1.106 - 0.0877*d + 0.00142*d^2 | 0.045 |
| published, completed tests | quadratic | 1.138 - 0.0873*d + 0.00121*d^2 | 0.048 |

- Time per query: both curves are best described as a constant plus an exponential in depth. The fitted growth rate is 0.241 per depth level ours vs 0.263 published, which is within 10%. Pure exponential (rate 0.118 ours, 0.172 published), quadratic, linear and power-law forms fit worse (power-law exponent 0.56 ours, 0.82 published, RMSE 0.29 and 0.39, clearly poor). The exp+const form wins by 16 AIC (ours) and 39 AIC (published) over the next form.
- Completed tests: quadratic, exp+const (exponent -0.044 ours, -0.035 published) and linear (slope -0.058 ours, -0.062 published per depth level, relative to depth 1) are within about 6 AIC of each other. The data does not separate them. The decline is close to linear in both our and the published curve, and our slope and the published slope agree within 6%. The exp+const tests fit has a negative constant, so it is a saturating-decline form with limited meaning.
- Ours vs published agree on the form family for both panels. The fitted parameters of the tests curve agree closely. The time curve differs in amplitude (our constant offset 0.90 vs 0.75, a smaller exponential part), which is the missing factor in the x5.6 vs x9.9 rise.
- The published values are visual read-offs, so their fitted parameters carry read-off error of at least a few percent.

## PySR symbolic regression (`pysr_fit.py`, `pysr_log.txt`, `pysr_results.json`)
PySR ran (venv `/tmp/claude-1000/venv-pysr`, Julia auto-installed). Settings: binary ops + - * /, unary exp log, maxsize 9, 15 populations, serial, seed 0, 55 s per curve, target = curve relative to depth 1, x = MaxDepth, loss = MSE. Best by PySR's default score, with the Pareto front in `pysr_log.txt`:

| curve | PySR best equation (relative y) | complexity-5 or simpler Pareto point |
|---|---|---|
| ours, time per query | 0.1155*exp(0.2466*x) + 0.9194 | exp(0.105*x), loss 0.21 |
| published, time per query | 0.1824*exp(0.2678*x) + 0.7883 | exp(0.152*x), loss 0.67 |
| ours, completed tests | -0.0611*x + exp(0.0562/x) | -0.0636*x + 1.034, loss 4.7e-4 |
| published, completed tests | exp(x/(x - 19.68)) + 0.0467 | -0.0662*x + 1.072, loss 2.7e-4 |

Time per query: PySR independently finds exponential + constant for both curves, with rates 0.247 (ours) and 0.268 (published), and offsets 0.92 and 0.79. These match the scipy exp+const fit (0.241, 0.263). Completed tests: the simplest accurate Pareto point is a straight line for both curves (slope -0.064 ours, -0.066 published per depth level, relative to depth 1). The higher-complexity equations (`exp(x/(x - 19.68))`, `exp(0.056/x)`) lower the loss slightly but have no interpretable meaning with 8 points; treat them as overfitting. Again, 8 points per curve means these are descriptive fits, not evidence of the true mechanism.
