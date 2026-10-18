# CSI 5137 — ATDM Database Testing Project

Class project for **CSI 5137 — Advanced Topics in Databases and Data Management**.

The project studies four recent DBMS testing papers and reproduces representative bugs on **MySQL 8.0.32**.

## Papers

| Paper | Main idea | Reproduction |
|---|---|---|
| **CODDTest** — *Constant Optimization Driven Database System Testing* (SIGMOD/PACMMOD 2025) | Replace an expression with its evaluated value and compare the results | MySQL [#111241](https://bugs.mysql.com/bug.php?id=111241) |
| **DDLCheck** — *Detecting Schema-Related Logic Bugs in Relational DBMSs via Equivalent Database Construction* (PVLDB 2025) | Build the same schema through different DDL histories and compare later behavior | MySQL [#114904](https://bugs.mysql.com/bug.php?id=114904) |
| **WriteCheck** — *Simple Testing Can Expose Most Critical Transaction Bugs* (PVLDB 2025) | Compare concurrent transaction behavior with a serial/oracle execution | MySQL #104833 — [Troc testcase](https://github.com/criszy/Troc/blob/a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5/cases/mysql104833.txt) |
| **Radar** — *Detecting Metadata-Related Logic Bugs in Database Systems via Raw Database Construction* (PVLDB 2024) | Strip the metadata but keep the data, then compare the same query on both databases | MySQL [#110125](https://bugs.mysql.com/bug.php?id=110125) |

The MySQL tracker entry for #104833 is currently restricted. The demo links to Troc's public testcase and uses Troc's MVCC oracle; it is not a direct execution of WriteCheck.

## Run

Requirements:

- Docker
- Git
- Docker Desktop or Colima on macOS

Run all four reproductions:

```bash
./scripts/run_all.sh
```

Expected final output:

```text
PASS: 4/4 representative MySQL bugs reproduced on MySQL 8.0.32.
```

Individual runners:

```bash
./repro/coddtest_111241.sh
./repro/ddlcheck_114904.sh
./repro/writecheck_104833.sh
./repro/radar_110125.sh
```

See [repro/README.md](repro/README.md) for the test cases, expected results, and Troc pin.

## Project files

- [papers/](papers/) — PDFs of the three papers
- [obsidian/](obsidian/) — study notes, concept pages, and reading guides
- [presentation/](presentation/) — PowerPoint, speaker notes, and rehearsal material
- [repro/](repro/) — MySQL reproduction scripts and test cases
- [results/](results/) — captured reference outputs
- [scripts/](scripts/) — setup and all-in-one runner

## Sources

- CODDTest: https://doi.org/10.1145/3709674
- CODDTest preprint: https://arxiv.org/abs/2501.11252
- DDLCheck: https://www.vldb.org/pvldb/vol18/p2281-song.pdf
- WriteCheck: https://www.vldb.org/pvldb/vol18/p2547-cui.pdf
- Radar: https://www.vldb.org/pvldb/vol17/p1884-song.pdf
- Radar artifact: https://github.com/tcse-iscas/radar
- Troc: https://github.com/criszy/Troc
