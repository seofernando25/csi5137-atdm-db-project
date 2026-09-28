#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTAINER="${MYSQL_CONTAINER:-db-paper-mysql8032}"
RUN_ID="${REPRO_ID:-$(date +%Y%m%d%H%M%S)_$$}"
DB="codd111241_${RUN_ID}"
OUT="$ROOT/results/coddtest_111241.latest.txt"
mkdir -p "$ROOT/results"

mysql_exec() {
  docker exec "$CONTAINER" mysql -h127.0.0.1 -uroot -proot "$@"
}

mysql_exec -e "CREATE DATABASE $DB; USE $DB; CREATE TABLE t0(c0 BOOL); INSERT INTO t0 VALUES (true);" >/dev/null

folded="$(mysql_exec "$DB" -Nse 'SELECT MIN(t0.c0) FROM t0;' 2>/dev/null)"
constant_form="$(mysql_exec "$DB" -Nse "SELECT t0.c0 FROM t0 WHERE (('0') NOT REGEXP ((((t0.c0)) NOT LIKE (CASE t0.c0 WHEN 76 THEN 0.7 ELSE t0.c0 END ))) AND (t0.c0 IN ((1))));" 2>/dev/null)"
subquery_form="$(mysql_exec "$DB" -Nse "SELECT t0.c0 FROM t0 WHERE (('0') NOT REGEXP ((((t0.c0)) NOT LIKE (CASE t0.c0 WHEN 76 THEN 0.7 ELSE t0.c0 END ))) AND (t0.c0 IN (SELECT MIN(t0.c0) FROM t0 )));" 2>/dev/null)"

{
  echo "=== CODDTest / MySQL #111241 ==="
  echo "version=$(mysql_exec -Nse 'SELECT VERSION();' 2>/dev/null)"
  echo "folded_value=${folded:-<empty>}"
  echo "constant_form=${constant_form:-<empty>}"
  echo "subquery_form=${subquery_form:-<empty>}"

  if [ "$folded" = "1" ] && [ "$constant_form" = "1" ] && [ -z "$subquery_form" ]; then
    echo "PASS: MySQL #111241 reproduced."
  else
    echo "FAIL: expected folded=1, constant_form=1, subquery_form=<empty>."
    exit 1
  fi
} | tee "$OUT"
