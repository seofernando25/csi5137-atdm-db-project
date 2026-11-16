#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTAINER="${MYSQL_CONTAINER:-csi5137-atdm-mysql8032}"
RUN_ID="${REPRO_ID:-$(date +%Y%m%d%H%M%S)_$$}"
INDEXED_DB="radar110125_indexed_${RUN_ID}"
RAW_DB="radar110125_raw_${RUN_ID}"
OUT="$ROOT/results/radar_110125.latest.txt"
mkdir -p "$ROOT/results"

mysql_exec() {
  docker exec "$CONTAINER" mysql -h127.0.0.1 -uroot -proot "$@"
}

# Radar's two worlds: db has an index on the column, rawDb does not.
# Data and query text are identical; only the metadata differs, so the
# returned row counts must agree.
mysql_exec -e "
CREATE DATABASE $INDEXED_DB;
USE $INDEXED_DB;
CREATE TABLE t0 (c0 DOUBLE ZEROFILL);
CREATE INDEX i0 ON t0 (c0 DESC);
INSERT INTO t0 (c0) VALUES (0);
" >/dev/null 2>&1

mysql_exec -e "
CREATE DATABASE $RAW_DB;
USE $RAW_DB;
CREATE TABLE t0 (c0 DOUBLE ZEROFILL);
INSERT INTO t0 (c0) VALUES (0);
" >/dev/null 2>&1

QUERY="SELECT COUNT(*) FROM t0 WHERE (IFNULL(-1123870957, '')) IN (t0.c0);"
indexed_rows="$(mysql_exec "$INDEXED_DB" -Nse "$QUERY" 2>/dev/null)"
raw_rows="$(mysql_exec "$RAW_DB" -Nse "$QUERY" 2>/dev/null)"

{
  echo "=== Radar / MySQL #110125 ==="
  echo "version=$(mysql_exec -Nse 'SELECT VERSION();' 2>/dev/null)"
  echo "indexed_rows=$indexed_rows"
  echo "raw_rows=$raw_rows"

  if [ "$indexed_rows" = "1" ] && [ "$raw_rows" = "0" ]; then
    echo "PASS: MySQL #110125 reproduced."
  else
    echo "FAIL: expected indexed_rows=1 and raw_rows=0."
    exit 1
  fi
} | tee "$OUT"
