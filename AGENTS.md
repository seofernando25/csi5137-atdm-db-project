# AGENTS.md

## Scope

Work only inside:

```text
~/Projects/csi5137-atdm-db-project
```

This is the class project repository for **CSI 5137 — Advanced Topics in Databases and Data Management (ATDM)**.

It reproduces one MySQL bug for each of four database-testing papers:

- CODDTest / MySQL #111241
- DDLCheck / MySQL #114904
- WriteCheck / MySQL #104833
- Radar / MySQL #110125

All four are verified on **MySQL 8.0.32**.

## Reproduction contract

Primary command:

```bash
./scripts/run_all.sh
```

A successful run must end with:

```text
PASS: 4/4 representative MySQL bugs reproduced on MySQL 8.0.32.
```

Do not claim success from build completion alone. Each runner must assert the bug-specific mismatch.

## Environment

Container:

```text
name: csi5137-atdm-mysql8032
image: mysql:8.0.32
platform: linux/amd64
host port: 3307
user/password: root/root
```

`scripts/setup.sh` may start Colima on macOS if Docker is installed but the daemon is not running.

## Pinned dependency

WriteCheck #104833 is replayed with the upstream Troc artifact pinned to:

```text
a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5
```

`scripts/setup.sh` recreates it under `.deps/Troc` and builds it in `maven:3.9.11-eclipse-temurin-17`.

Do not commit `.deps/` or any of the exploratory upstream clones at the repository root.

## Bug oracles

### CODDTest #111241

Expected:

```text
folded scalar value = 1
constant-substituted query => row 1
scalar-subquery query => empty
```

The mismatch is the bug.

### DDLCheck #114904

Expected:

- evolved schema visibly references renamed table `t2`;
- insert into child table fails;
- error references stale table `t0`;
- directly-created equivalent schema accepts the insert.

### WriteCheck #104833

Exact case file:

```text
repro/writecheck_104833.case.txt
```

Expected observed final state:

```text
[10, 1, 10, 20, 10, 20]
```

Expected oracle final state:

```text
[10, 20, 10, 20, 10, 20]
```

Expected detector message:

```text
Error: Inconsistent final database state
```

### Radar #110125

Two databases hold the same data with different metadata: the indexed copy has `CREATE INDEX i0 ON t0 (c0 DESC)`, the raw copy does not. Data and query text are identical.

Expected:

```text
indexed_rows=1
raw_rows=0
```

The raw copy's empty result is correct; the indexed copy's single row is the bug. `DOUBLE ZEROFILL` is deprecated since 8.0.17 and MySQL only fixed the defect in 26.7.0, so all 8.0.x releases are affected.

## Repository hygiene

Commit:

- `README.md`, `AGENTS.md`
- `compose.yaml`
- `scripts/`
- `repro/`
- small captured reference outputs in `results/`
- `papers/README.md`

Do not commit:

- cloned upstream repos
- `.deps/`
- Maven `target/` directories
- logs
- downloaded PDFs
- `.DS_Store`

## Presentation framing

Do not present these results as evidence that MySQL is generally more buggy than other DBMSs.

The shared research idea is:

```text
different execution + same expected semantics
                 ↓
           compare results
                 ↓
       mismatch = bug oracle
```

Use one minimized testcase per paper rather than attempting to repeat the papers' full fuzzing campaigns.
