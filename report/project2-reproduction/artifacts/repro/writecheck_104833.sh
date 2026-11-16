#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTAINER="${MYSQL_CONTAINER:-csi5137-atdm-mysql8032}"
RUN_ID="${REPRO_ID:-$(date +%Y%m%d%H%M%S)_$$}"
TROC_DIR="$ROOT/.deps/Troc"
OUT="$ROOT/results/writecheck_104833.latest.txt"
mkdir -p "$ROOT/results"

if [ ! -f "$TROC_DIR/target/troc-1.0-SNAPSHOT.jar" ]; then
  echo "Pinned Troc build not found; run scripts/setup.sh first." >&2
  exit 1
fi

set +e
docker run --rm \
  --network "container:$CONTAINER" \
  -v "$ROOT:/repo" \
  -w /repo/.deps/Troc \
  maven:3.9.11-eclipse-temurin-17 \
  java -jar target/troc-1.0-SNAPSHOT.jar \
    --dbms mysql \
    --host 127.0.0.1 \
    --port 3306 \
    --username root \
    --password root \
    --db "troc104833_${RUN_ID}" \
    --table t \
    --set-case \
    --case-file /repo/repro/writecheck_104833.case.txt \
  >"$OUT" 2>&1
runner_rc=$?
set -e

cat "$OUT"

if grep -Fq 'Error: Inconsistent final database state' "$OUT" \
   && grep -Fq 'FinalState: [10, 1, 10, 20, 10, 20]' "$OUT" \
   && grep -Fq 'FinalState: [10, 20, 10, 20, 10, 20]' "$OUT"; then
  echo "PASS: MySQL #104833 reproduced (runner exit=$runner_rc)."
else
  echo "FAIL: expected WriteCheck/Troc final-state mismatch was not observed." >&2
  exit 1
fi
