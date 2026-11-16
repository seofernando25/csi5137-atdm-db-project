#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$ROOT/scripts/setup.sh"

tests=(
  "coddtest_111241.sh"
  "ddlcheck_114904.sh"
  "writecheck_104833.sh"
  "radar_110125.sh"
)

passed=0
for test in "${tests[@]}"; do
  echo
  echo "============================================================"
  echo "Running $test"
  echo "============================================================"
  if "$ROOT/repro/$test"; then
    passed=$((passed + 1))
  else
    echo "FAILED: $test" >&2
    exit 1
  fi
done

echo
echo "PASS: $passed/${#tests[@]} representative MySQL bugs reproduced on MySQL 8.0.32."
