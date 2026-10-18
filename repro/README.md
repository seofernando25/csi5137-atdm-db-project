# Reproductions

All four main cases run against **MySQL 8.0.32**.

Run setup first if needed:

```bash
./scripts/setup.sh
```

Or run the full suite from the repository root:

```bash
./scripts/run_all.sh
```

## CODDTest — MySQL #111241

Runner:

```bash
./repro/coddtest_111241.sh
```

The testcase evaluates a scalar subquery to `1` and compares the original query with a constant-substituted form.

Expected result:

```text
folded_value=1
constant_form=1
subquery_form=<empty>
PASS: MySQL #111241 reproduced.
```

The two query forms should be equivalent, so the disagreement is the reproduced CODDTest-style oracle violation.

An additional CODDTest bug, MySQL [#111421](https://bugs.mysql.com/bug.php?id=111421), is available in `coddtest_111421.sh`.

## DDLCheck — MySQL #114904

Runner:

```bash
./repro/ddlcheck_114904.sh
```

The evolved schema:

1. creates parent table `t0`;
2. creates child table `t1` with a foreign key to `t0`;
3. renames `t0` to `t2`.

The visible schema says the foreign key references `t2`, but a valid insert fails and the error still refers to stale table `t0`.

The same insert succeeds when the equivalent final schema is created directly.

Expected final line:

```text
PASS: MySQL #114904 reproduced.
```

## Radar — MySQL #110125

Runner:

```bash
./repro/radar_110125.sh
```

Radar compares two databases that hold the same data but different metadata. The testcase uses two copies of one table: `t0` with an index on `c0`, and the raw copy without it. Both hold the same single row and receive the same query text.

Indexed copy and raw copy must return the same result. They do not:

```text
SELECT COUNT(*) FROM t0 WHERE (IFNULL(-1123870957, '')) IN (t0.c0);
```

Expected result:

```text
version=8.0.32
indexed_rows=1
raw_rows=0
PASS: MySQL #110125 reproduced.
```

The raw copy returns no rows, which is correct, because no column value equals the negative constant. The indexed copy returns the row: the index range scan treats the out-of-range comparison as possible instead of impossible. MySQL confirmed the bug as S1 (Critical) and only fixed it in 26.7.0, so every 8.0.x release, including the pinned 8.0.32, is affected.

`DOUBLE ZEROFILL` is deprecated since MySQL 8.0.17, which is part of why the report stayed open for years. The reproduction keeps it because the paper's testcase uses it; the underlying fault is the indexed unsigned `DOUBLE` compared against a negative string-typed constant.

## Transaction replay — MySQL #104833

Runner:

```bash
./repro/writecheck_104833.sh
```

Case file:

```text
repro/writecheck_104833.case.txt
```

The replay uses the upstream **Troc** testcase and Troc's MVCC-based oracle. This is not a direct execution of the WriteCheck implementation.

Upstream testcase: https://github.com/criszy/Troc/blob/a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5/cases/mysql104833.txt

Submitted schedule:

```text
1-1-2-2-1-2
```

Observed concurrent final state:

```text
[10, 1, 10, 20, 10, 20]
```

MVCC oracle state:

```text
[10, 20, 10, 20, 10, 20]
```

Troc reports:

```text
Error: Inconsistent final database state
```

The runner checks for both states and the inconsistency message.

## Troc version

The setup script fetches this pinned Troc commit:

```text
a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5
```

It is built in a Maven container and stored under `.deps/Troc`.
