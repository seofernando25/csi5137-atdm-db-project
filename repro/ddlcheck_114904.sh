#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTAINER="${MYSQL_CONTAINER:-db-paper-mysql8032}"
RUN_ID="${REPRO_ID:-$(date +%Y%m%d%H%M%S)_$$}"
EVOLVED_DB="ddl114904_evolved_${RUN_ID}"
DIRECT_DB="ddl114904_direct_${RUN_ID}"
OUT="$ROOT/results/ddlcheck_114904.latest.txt"
mkdir -p "$ROOT/results"

mysql_exec() {
  docker exec "$CONTAINER" mysql -h127.0.0.1 -uroot -proot "$@"
}

mysql_exec -e "
CREATE DATABASE $EVOLVED_DB;
USE $EVOLVED_DB;
CREATE TABLE t0 (c2 FLOAT8, PRIMARY KEY (c2));
CREATE TABLE t1 (c1 FLOAT8 UNIQUE, FOREIGN KEY (c1) REFERENCES t0(c2) ON UPDATE CASCADE);
ALTER TABLE t0 RENAME AS t2, ALGORITHM COPY;
INSERT INTO t2 (c2) VALUES (1);
" >/dev/null

visible_schema="$(mysql_exec "$EVOLVED_DB" -Nse 'SHOW CREATE TABLE t1;' 2>/dev/null)"

set +e
evolved_error="$(mysql_exec "$EVOLVED_DB" -e 'INSERT INTO t1 (c1) VALUES (1);' 2>&1)"
evolved_rc=$?
set -e

mysql_exec -e "
CREATE DATABASE $DIRECT_DB;
USE $DIRECT_DB;
CREATE TABLE t2 (c2 FLOAT8, PRIMARY KEY (c2));
CREATE TABLE t1 (c1 FLOAT8 UNIQUE, FOREIGN KEY (c1) REFERENCES t2(c2) ON UPDATE CASCADE);
INSERT INTO t2 (c2) VALUES (1);
INSERT INTO t1 (c1) VALUES (1);
" >/dev/null
direct_value="$(mysql_exec "$DIRECT_DB" -Nse 'SELECT c1 FROM t1;' 2>/dev/null)"

{
  echo "=== DDLCheck / MySQL #114904 ==="
  echo "version=$(mysql_exec -Nse 'SELECT VERSION();' 2>/dev/null)"
  echo "visible_schema=$visible_schema"
  echo "evolved_insert_exit=$evolved_rc"
  echo "evolved_insert_error=$evolved_error"
  echo "direct_schema_inserted_value=${direct_value:-<empty>}"

  if [ "$evolved_rc" -ne 0 ] \
     && printf '%s' "$visible_schema" | grep -Fq 'REFERENCES `t2`' \
     && printf '%s' "$evolved_error" | grep -Fq 'REFERENCES `t0`' \
     && [ "$direct_value" = "1" ]; then
    echo "PASS: MySQL #114904 reproduced."
  else
    echo "FAIL: DDLCheck mismatch was not reproduced."
    exit 1
  fi
} | tee "$OUT"
