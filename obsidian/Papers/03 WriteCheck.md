---
type: paper
title: Simple Testing Can Expose Most Critical Transaction Bugs
authors: [Ziyu Cui, Wensheng Dou, Yu Gao, Rui Yang, Yingying Zheng, Jiansen Song, Yuan Feng, Jun Wei]
venue: PVLDB
year: 2025
tags: [paper, writecheck, transactions, serializability, dbms-testing]
---

# WriteCheck — Simple Testing Can Expose Most Critical Transaction Bugs

[[Guides/03 Understanding WriteCheck|Narrative guide]]

**Full title:** Simple Testing Can Expose Most Critical Transaction Bugs: Understanding and Detecting Write-Specific Serializability Violations in Database Systems

**PDF:** [[PDFs/WriteCheck_PVLDB2025.pdf]]

**Venue:** PVLDB 18(8), 2025

**Public PDF:** https://www.vldb.org/pvldb/vol18/p2547-cui.pdf

## One-sentence thesis

WriteCheck proposes **write-specific serializability (WSS)** as a simple transaction-testing oracle: an actual concurrent schedule should produce the same final database state as the corresponding serial schedule inferred from the observed transaction completion order.

## Problem

A concurrent workload produces some final database state.

But without already knowing the expected state, how can an automated tester decide whether that state is correct?

Existing verification/testing approaches may:

- focus only on claimed isolation-level anomalies;
- assume simple key-value operations;
- require multiple compatible DBMSs;
- infer complex statement dependencies;
- support limited SQL features.

WriteCheck tries to build a simpler oracle.

## Core idea

Generate a concurrent execution:

    initial database
          ↓
    transactions + submitted order
          ↓
    actual concurrent schedule H_con
          ↓
    observed final state A

Then infer a serial reference execution:

    actual schedule H_con
          ↓
    FCRFS serial pattern
          ↓
    serial schedule H_ser
          ↓
    replay from same initial database
          ↓
    serial final state B

Expected under WSS:

    A = B

A mismatch is a WSS violation.

See [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)]].

## Why the serial order is not arbitrary

If we simply tried every serial order, a buggy concurrent state might accidentally match one of them.

WriteCheck needs a serial order justified by the actual concurrent execution.

The paper's empirical study identifies:

**FCRFS — First Commit/Rollback First Scheduled**

If one transaction completes before another in the concurrent schedule, it comes first in the inferred serial schedule.

See [[Concepts/WriteCheck/14 FCRFS Serial Pattern]].

## tx-WSS and stmt-WSS

The paper defines two versions:

- **tx-WSS** — preserve complete explicit transactions;
- **stmt-WSS** — replay surviving DQL/DML statements individually as autocommit transactions.

See [[Concepts/WriteCheck/12 Transaction-Level and Statement-Level WSS]].

## Concepts to know

### Transaction foundations

- [[Concepts/WriteCheck/01 Transactions and ACID]]
- [[Concepts/WriteCheck/02 Explicit and Autocommit Transactions]]
- [[Concepts/WriteCheck/03 Read and Write Operations]]
- [[Concepts/WriteCheck/04 Transaction Schedules]]
- [[Concepts/WriteCheck/05 Concurrent and Serial Schedules]]
- [[Concepts/WriteCheck/06 Transaction Test Cases]]
- [[Concepts/WriteCheck/07 Critical Transaction Bugs]]
- [[Concepts/WriteCheck/08 Isolation Levels]]
- [[Concepts/WriteCheck/09 Concurrency Control Modes]]
- [[Concepts/WriteCheck/10 Write-Write Conflicts]]

### WSS

- [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)]]
- [[Concepts/WriteCheck/12 Transaction-Level and Statement-Level WSS]]
- [[Concepts/WriteCheck/13 WSS vs Other Serializability Notions]]
- [[Concepts/WriteCheck/14 FCRFS Serial Pattern]]
- [[Concepts/WriteCheck/15 Happens-Before Relation]]
- [[Concepts/WriteCheck/16 WSS Correctness Assumption]]
- [[Concepts/WriteCheck/17 Read-Dependent Writes]]

### Testing workflow

- [[Concepts/WriteCheck/18 Small-Scope Hypothesis]]
- [[Concepts/WriteCheck/19 Deterministic Triggering]]
- [[Concepts/WriteCheck/20 WriteCheck Architecture]]
- [[Concepts/WriteCheck/21 Transaction Groups and Submitted Order]]
- [[Concepts/WriteCheck/22 Submitted Order vs Actual Schedule]]
- [[Concepts/WriteCheck/23 Transaction Execution Protocol]]
- [[Concepts/WriteCheck/24 Blocking Aborts and Deadlocks]]
- [[Concepts/WriteCheck/25 Inferring the Serial Oracle]]
- [[Concepts/WriteCheck/26 Final-State Comparison]]

### Oracle boundary

- [[Concepts/WriteCheck/27 Semi-Consistent Reads]]
- [[Concepts/WriteCheck/28 Gap Locks]]
- [[Concepts/WriteCheck/29 Permissible WSS Violations and False Positives]]

## Empirical motivation

The authors first study 35 real-world critical transaction bugs.

Among them:

- 32, or 91.4%, have test cases violating WSS;
- all studied WSS violations use no more than five transactions;
- almost all involved transactions contain no more than five statements;
- 90.6% of studied WSS violations can be triggered deterministically by statement ordering.

These observations motivate a deliberately simple tester.

## Evaluation

WriteCheck is evaluated on:

- MySQL 8.0.32;
- PostgreSQL 15.2;
- SQLite 3.36.0;
- MariaDB 10.11.2;
- CockroachDB 22.2.5;
- TiDB 6.6.0.

The authors report:

- 101 WSS violation instances;
- 22 unique WSS violations;
- 13 confirmed critical transaction bugs;
- 11 confirmed as new critical transaction bugs;
- 9 WSS violations classified by developers as false positives.

See [[Concepts/WriteCheck/30 Evaluation and Findings]].

## False positives are conceptually important

WriteCheck's correctness argument assumes that relevant write conflicts are correctly recognized and blocked/aborted.

Some DBMS behaviors at weaker isolation levels intentionally violate that assumption.

The paper analyzes:

- [[Concepts/WriteCheck/27 Semi-Consistent Reads]];
- [[Concepts/WriteCheck/28 Gap Locks|lack of gap locks]].

These cases show that transaction write semantics are not perfectly uniform across DBMSs or isolation levels.

## Our project reproduction

Our class repository reproduces MySQL **#104833** on MySQL 8.0.32.

However:

> **The executable replay uses the upstream Troc testcase and Troc's MVCC-based oracle. It is not a rerun of WriteCheck itself.**

Observed state:

    [10, 1, 10, 20, 10, 20]

Troc MVCC oracle:

    [10, 20, 10, 20, 10, 20]

See:

[[Concepts/WriteCheck/32 Project Reproduction - MySQL 104833]]

Repository:

    repro/writecheck_104833.case.txt
    repro/writecheck_104833.sh
    results/writecheck_104833.txt

## Reading pointers

- Motivation / WSS intuition: [[PDFs/WriteCheck_PVLDB2025.pdf#page=2]]
- Formal WSS definitions: [[PDFs/WriteCheck_PVLDB2025.pdf#page=3]]
- Empirical study: [[PDFs/WriteCheck_PVLDB2025.pdf#page=4]]
- FCRFS and triggering conditions: [[PDFs/WriteCheck_PVLDB2025.pdf#page=5]]
- Correctness argument and architecture: [[PDFs/WriteCheck_PVLDB2025.pdf#page=6]]
- Actual-schedule execution protocol: [[PDFs/WriteCheck_PVLDB2025.pdf#page=7]]
- WSS detection and evaluation setup: [[PDFs/WriteCheck_PVLDB2025.pdf#page=8]]
- Main results: [[PDFs/WriteCheck_PVLDB2025.pdf#page=9]]
- False-positive analysis: [[PDFs/WriteCheck_PVLDB2025.pdf#page=10]]
- Comparison with prior work: [[PDFs/WriteCheck_PVLDB2025.pdf#page=11]]
- Discussion / conclusion: [[PDFs/WriteCheck_PVLDB2025.pdf#page=12]]

## Questions to be able to answer

- What is a transaction schedule?
- What is the difference between concurrent and serial schedules?
- What exactly does WSS require?
- Why is WSS weaker than conflict serializability?
- What is the difference between tx-WSS and stmt-WSS?
- Why is FCRFS necessary?
- What does Assumption 1 say?
- Why can submitted order differ from actual schedule?
- Why can semi-consistent reads and missing gap locks create false positives?
- Why does the paper argue small transaction test cases are enough to expose many critical bugs?
- How does our #104833 demonstration relate to the paper without being a direct WriteCheck rerun?

## Final synthesis

[[Concepts/WriteCheck/34 How WriteCheck Fits Together]]
