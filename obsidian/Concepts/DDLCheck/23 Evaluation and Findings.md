# DDLCheck Evaluation and Findings

## In one sentence

The evaluation asks whether DDLCheck finds real schema-related bugs and whether its sequence-diversity optimization improves testing efficiency.

## Systems

The paper evaluates six relational DBMSs:

- MySQL;
- PostgreSQL;
- SQLite;
- MariaDB;
- CockroachDB;
- TiDB.

## Headline bug results

The authors report:

- 34 submitted bugs;
- 29 confirmed as previously unknown;
- 9 fixed at the time reported in the paper.

Among the confirmed bugs, the paper analyzes both schema-related logic bugs and crashes.

## What revealed the bugs?

The authors report bug-revealing statements across multiple categories:

- DDL;
- DML;
- SELECT.

A notable finding is that many schema-evolution bugs become visible later through SELECT statements.

## Complex histories matter

The paper reports that most confirmed schema-related bugs were triggered by the complex generated DDL sequence rather than only by the simple synthesized construction.

That supports the motivation for explicitly testing **schema evolution**, not just final CREATE statements.

## Optimization result

Using DSTG-based filtering allowed DDLCheck to test more unique schema histories and detect unique bugs more quickly than its comparison variants.

## Presentation takeaway

> Different construction histories are not merely redundant ways to reach a schema; they exercise distinct internal DBMS maintenance paths.

Paper evaluation begins: [[PDFs/DDLCheck_PVLDB2025.pdf#page=8]]
