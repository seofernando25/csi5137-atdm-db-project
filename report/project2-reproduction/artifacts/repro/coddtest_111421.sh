#!/usr/bin/env bash
set +e

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

DOCKER=docker
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/results/coddtest_111421.latest.txt"
DB="codd111421_$(date +%Y%m%d%H%M%S)_$$"

{
  echo "=== CODDTest / MySQL #111421 ==="
  "$DOCKER" exec csi5137-atdm-mysql8032 mysql -h127.0.0.1 -uroot -proot -Nse "SELECT VERSION();"

  echo
  echo "Expected bug: CREATE TABLE with CHECK(true) is rejected."
  "$DOCKER" exec csi5137-atdm-mysql8032 mysql -h127.0.0.1 -uroot -proot -e "
  CREATE DATABASE $DB;
  USE $DB;
  CREATE TABLE t0(c1 NUMERIC CHECK (true));
  "
  STATUS=$?
  echo "mysql_exit_status=$STATUS"
} 2>&1 | tee "$OUT"
