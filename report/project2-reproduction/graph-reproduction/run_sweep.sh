#!/usr/bin/env bash
# Usage: run_sweep.sh <patched-sqlancer-target-dir> <seconds-per-depth> <outdir>
# Needs the MySQL 8.0.32 container on 127.0.0.1:3307 (root/root).
set -u
T=$1; SECS=${2:-35}; OUT=$3; mkdir -p "$OUT"
for d in 1 3 5 7 9 11 13 15; do
  W=$(mktemp -d); 
  docker run --rm --user "$(id -u)" --network host -v "$T":/t -v "$W":/w -w /w eclipse-temurin:17-jre \
    java -jar /t/sqlancer-2.0.0.jar --num-threads 1 --timeout-seconds "$SECS" --random-seed 1 \
    --num-tries 1000000 --max-expression-depth "$d" --host 127.0.0.1 --port 3307 --username root --password root \
    mysql --oracle CODDTest --coddtest-model expression 2>&1 | grep '^METRICS' | sed "s/^/depth=$d /" | tee -a "$OUT/metrics.txt"
  rm -rf "$W" 2>/dev/null
done
