#!/usr/bin/env bash
# Usage: run_sweep_sqlite.sh <patched-sqlancer-target-dir> <seconds-per-depth> <outdir>
# SQLite via sqlite-jdbc 3.42.0.0, 10 threads, CODDTest expression model.
set -u
T=$1; SECS=${2:-40}; OUT=$3; mkdir -p "$OUT"
for d in 1 3 5 7 9 11 13 15; do
  W=$(mktemp -d)
  docker run --rm --user "$(id -u)" -v "$T":/t -v "$W":/w -w /w eclipse-temurin:17-jre \
    java -jar /t/sqlancer-2.0.0.jar --num-threads 10 --timeout-seconds "$SECS" --random-seed 1 \
    --num-tries 1000000 --max-expression-depth "$d" \
    sqlite3 --oracle CODDTest --coddtest-model expression 2>&1 | grep '^METRICS' | sed 's/ ignores=.*//' | sed "s/^/depth=$d /" | tee -a "$OUT/metrics_sqlite.txt"
  rm -rf "$W" 2>/dev/null
done
