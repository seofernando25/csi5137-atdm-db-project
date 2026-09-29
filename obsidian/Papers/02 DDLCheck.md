---
type: paper
title: Detecting Schema-Related Logic Bugs in Relational DBMSs via Equivalent Database Construction
authors: [Jiansen Song, Wensheng Dou, Yingying Zheng, Yu Gao, Ziyu Cui, Wei Wang, Jun Wei]
venue: PVLDB
year: 2025
tags: [paper, ddlcheck, schema-evolution, dbms-testing]
---

# DDLCheck — Detecting Schema-Related Logic Bugs via Equivalent Database Construction

**PDF:** [[PDFs/DDLCheck_PVLDB2025.pdf]]
**Venue:** PVLDB 18(7), 2025
**Public PDF:** https://www.vldb.org/pvldb/vol18/p2281-song.pdf

## One-sentence thesis

DDLCheck tests schema evolution by creating two databases with the **same visible final schema through different DDL histories**, then executing the same later SQL and checking that they behave identically.

## Problem

DBMSs maintain more than the schema users can see.

During [[Concepts/DDLCheck/02 Schema Evolution|schema evolution]], operations such as ALTER, DROP, RENAME, index changes, and constraint changes also update hidden [[Concepts/DDLCheck/04 Schema-Related Information|schema-related information]].

A bug can leave that hidden state stale even when the final visible schema appears correct.

## Core construction

### Complex generated path

    seq_gen
      ↓
    CREATE / ALTER / DROP / RENAME / ...
      ↓
    db_gen

### Simple synthesized path

Inspect the final schema of db_gen:

    final visible schema S
      ↓
    CREATE / CREATE VIEW / necessary ALTER
      ↓
    seq_syn
      ↓
    db_syn

Expected:

    schema(db_gen) = schema(db_syn)

## Oracle

Run the same statement q on both:

    db_gen ── q ──→ behavior A
    db_syn ── q ──→ behavior B

Expected:

    behavior A = behavior B

DDLCheck compares:

- errors;
- SELECT results;
- resulting database states.

See [[Concepts/DDLCheck/14 DDLCheck Oracle]].

## Concepts to know

### Foundations

- [[Concepts/DDLCheck/01 Database Schema]]
- [[Concepts/DDLCheck/02 Schema Evolution]]
- [[Concepts/DDLCheck/03 DDL DML and DQL]]
- [[Concepts/DDLCheck/04 Schema-Related Information]]
- [[Concepts/DDLCheck/05 Schema-Related Logic Bugs]]

### Oracle and construction

- [[Concepts/DDLCheck/06 Equivalent Databases]]
- [[Concepts/DDLCheck/07 DDL Sequences]]
- [[Concepts/DDLCheck/08 Generated and Synthesized DDL Sequences]]
- [[Concepts/DDLCheck/09 DDLCheck Architecture]]
- [[Concepts/DDLCheck/10 DDL Sequence Generation]]
- [[Concepts/DDLCheck/12 DDL Sequence Synthesis]]
- [[Concepts/DDLCheck/13 Schema Introspection and System Catalogs]]
- [[Concepts/DDLCheck/14 DDLCheck Oracle]]

### Optimization

- [[Concepts/DDLCheck/16 Database Schema Transition Graph (DSTG)]]
- [[Concepts/DDLCheck/17 Table Structure Equivalence]]
- [[Concepts/DDLCheck/18 Interesting DDL Sequences]]

### Failure analysis

- [[Concepts/DDLCheck/15 Schema Bug Categories]]
- [[Concepts/DDLCheck/20 Bug-Revealing Statements]]
- [[Concepts/DDLCheck/21 Root Causes of Schema Bugs]]
- [[Concepts/DDLCheck/22 Bug Report Reduction]]

## Evaluation

The authors evaluate DDLCheck on:

- MySQL;
- PostgreSQL;
- SQLite;
- MariaDB;
- CockroachDB;
- TiDB.

They report:

- 34 submitted bugs;
- 29 confirmed as previously unknown;
- 9 fixed at the time described in the paper.

See [[Concepts/DDLCheck/23 Evaluation and Findings]].

## Our reproduction — MySQL #114904

This is an especially clean example of the paper's thesis.

A foreign key initially references table t0.

The parent is renamed to t2.

The **visible schema** says the foreign key references t2.

But a later valid INSERT fails, and the error exposes stale internal information still referencing t0.

The directly created equivalent schema accepts the same INSERT.

See [[Concepts/DDLCheck/24 MySQL 114904 Walkthrough]].

Repository:

    repro/ddlcheck_114904.sh
    results/ddlcheck_114904.txt

## Paper reading pointers

- Motivation / example: [[PDFs/DDLCheck_PVLDB2025.pdf#page=1]]
- Background: [[PDFs/DDLCheck_PVLDB2025.pdf#page=3]]
- Architecture and generation: [[PDFs/DDLCheck_PVLDB2025.pdf#page=4]]
- Sequence synthesis: [[PDFs/DDLCheck_PVLDB2025.pdf#page=5]]
- Bug detection and DSTG: [[PDFs/DDLCheck_PVLDB2025.pdf#page=6]]
- DSTG equivalence: [[PDFs/DDLCheck_PVLDB2025.pdf#page=7]]
- Evaluation: [[PDFs/DDLCheck_PVLDB2025.pdf#page=8]]
- Bug analysis / #114904: [[PDFs/DDLCheck_PVLDB2025.pdf#page=10]]

## Questions to be able to answer

- What is the difference between visible schema and schema-related information?
- Why do seq_gen and seq_syn need to produce equivalent databases?
- What exactly does DDLCheck compare?
- Why is DDL generation stateful?
- Why does synthesis need system catalogs?
- What problem does the DSTG solve?
- What makes two table structures equivalent?
- What is a bug-revealing statement?
- Why does #114904 validate DDLCheck's central idea?

## Final synthesis

[[Concepts/DDLCheck/26 How DDLCheck Fits Together]]
