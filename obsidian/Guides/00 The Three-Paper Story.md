---
type: guide
series: ATDM database testing papers
order: 0
tags: [guide, database-testing, csi5137, atdm]
---

# The Three-Paper Story

## What this series is about

This notebook studies three 2025 papers about testing database systems:

1. [[Papers/01 CODDTest|CODDTest]]
2. [[Papers/02 DDLCheck|DDLCheck]]
3. [[Papers/03 WriteCheck|WriteCheck]]

At first, they appear to test completely different things.

- CODDTest tests SQL expressions and query evaluation.
- DDLCheck tests schema evolution and hidden schema state.
- WriteCheck tests concurrent transactions.

The useful connection is deeper:

> **All three papers need a way to detect wrong behavior without already knowing the correct answer.**

That is the [[Concepts/Shared/01 Test Oracle|test-oracle problem]].

A database can return a normal-looking result, maintain a normal-looking schema, or successfully commit transactions while still being wrong. Crashes are easy to notice. Silent logic errors are not.

The three papers solve that problem by constructing a second execution that should be **equivalent** to the first one and comparing what happens.

See [[Concepts/Shared/04 Equivalence-Based Testing|Equivalence-Based Testing]].

## The common pattern

    construct two executions
    that should mean the same thing
              ↓
         execute both
              ↓
      compare observable behavior
              ↓
       mismatch = bug candidate

Each paper contributes a different argument for why two executions should agree.

### CODDTest

CODDTest evaluates an expression and replaces the expression with the value it produced.

    original query O
          ≡
    folded query F

If substituting an expression by its already-computed value changes the query result, something is inconsistent.

### DDLCheck

DDLCheck builds the same visible database schema through two different histories.

    evolved database db_gen
          ≡
    directly constructed db_syn

If the same later SQL behaves differently, the construction history has leaked into semantics.

### WriteCheck

WriteCheck executes transactions concurrently and infers a corresponding serial execution.

    concurrent schedule H_con
          ≡
    inferred serial H_ser

Under the paper's WSS assumptions, the write effects should produce the same final database state.

# Paper 1 — CODDTest: change the expression

CODDTest starts with the easiest level to visualize: one SQL query.

Imagine a query contains an expression φ. For the current database, evaluate φ separately:

    φ → Rφ

Now put Rφ back into the original query.

    O = original query containing φ
    F = same query with φ replaced by Rφ

Expected:

    result(O) = result(F)

The transformation uses [[Concepts/CODDTest/04 Constant Folding|Constant Folding]] and [[Concepts/CODDTest/05 Constant Propagation|Constant Propagation]].

The broader testing strategy is [[Concepts/Shared/03 Metamorphic Testing|Metamorphic Testing]].

The technique becomes more complicated when an expression depends on the current row. That leads to:

- [[Concepts/CODDTest/07A Independent Expressions|Independent Expressions]]
- [[Concepts/CODDTest/07B Dependent Expressions|Dependent Expressions]]
- [[Concepts/CODDTest/10 SQL CASE and Row Mapping|SQL CASE and Row Mapping]]

Our representative MySQL reproduction is #111241, where a scalar-subquery form and its constant-substituted form disagree.

Full guide:

[[Guides/01 Understanding CODDTest]]

# Paper 2 — DDLCheck: change the history

DDLCheck moves from query expressions to database structure.

A database schema evolves:

    CREATE
      ↓
    ALTER
      ↓
    DROP
      ↓
    RENAME
      ↓
    final schema

This is [[Concepts/DDLCheck/02 Schema Evolution|Schema Evolution]].

The final visible schema may look correct while the DBMS keeps additional [[Concepts/DDLCheck/04 Schema-Related Information|Schema-Related Information]] such as foreign-key metadata, system catalogs, statistics, hidden columns, storage information, and optimizer metadata.

DDLCheck deliberately creates two paths.

    seq_gen
      ↓
    CREATE / ALTER / DROP / RENAME / ...
      ↓
    db_gen

and:

    final schema
      ↓
    seq_syn
      ↓
    db_syn

The two are intended to be [[Concepts/DDLCheck/06 Equivalent Databases|Equivalent Databases]].

Then DDLCheck runs the same later SQL against both:

    db_gen ── q ──→ behavior A
    db_syn ── q ──→ behavior B

Expected:

    A = B

Our strongest example is MySQL #114904: a parent table is renamed from t0 to t2; the visible foreign key shows t2; a later valid INSERT fails because stale internal information still refers to t0; directly creating the final schema makes the INSERT succeed.

See [[Concepts/DDLCheck/24 MySQL 114904 Walkthrough|MySQL #114904 Walkthrough]].

Full guide:

[[Guides/02 Understanding DDLCheck]]

# Paper 3 — WriteCheck: change the schedule

WriteCheck moves to concurrency.

The same transactions can interleave in many ways:

    T1 BEGIN
    T2 BEGIN
    T1 UPDATE
    T2 UPDATE
    T1 COMMIT
    T2 COMMIT

This is a [[Concepts/WriteCheck/04 Transaction Schedules|Transaction Schedule]].

The difficult question is:

> What final database state should this concurrent execution produce?

WriteCheck proposes [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)|Write-Specific Serializability]], or WSS.

    concurrent schedule
            ↓
      final database A

should agree with:

    corresponding serial schedule
            ↓
      final database B

The challenge is choosing the serial schedule.

WriteCheck uses the [[Concepts/WriteCheck/14 FCRFS Serial Pattern|FCRFS Serial Pattern]]: First Commit/Rollback First Scheduled.

A transaction that finishes earlier in the observed concurrent execution is placed earlier in the inferred serial execution.

WriteCheck must also distinguish what statements were submitted from what the DBMS actually executed after blocking, resumption, deadlocks, and aborts.

See [[Concepts/WriteCheck/22 Submitted Order vs Actual Schedule|Submitted Order vs Actual Schedule]].

Our class project includes a representative transaction-bug replay on MySQL #104833. The runnable reproduction uses Troc's testcase and MVCC oracle, not a direct WriteCheck run. See [[Concepts/WriteCheck/32 Project Reproduction - MySQL 104833|Project Reproduction — MySQL #104833]].

Full guide:

[[Guides/03 Understanding WriteCheck]]

# The progression

The papers move through three increasingly large units of DBMS behavior.

    CODDTest
    expression / query
          ↓
    DDLCheck
    schema / history
          ↓
    WriteCheck
    transactions / concurrency

| Paper | What changes? | What should remain equivalent? |
|---|---|---|
| CODDTest | Representation of an expression | Query result |
| DDLCheck | History used to build the schema | Later database behavior |
| WriteCheck | Concurrent vs inferred serial schedule | Write effects / final database state |

What each paper manufactures as its reference:

| Paper | Reference execution |
|---|---|
| CODDTest | Folded query F |
| DDLCheck | Synthesized database db_syn |
| WriteCheck | FCRFS serial schedule H_ser |

# Where the papers differ

The common pattern does not mean the papers are interchangeable. Each equivalence depends on different assumptions.

## CODDTest

The replacement must preserve semantics under a fixed database state. Potential trouble includes NULL semantics, floating point, and context dependence.

See [[Concepts/CODDTest/18 False Positives and Floating Point|False Positives and Floating Point]].

## DDLCheck

The two databases need a useful definition of equivalent visible schemas, and later SQL must be deterministic enough for comparison.

See [[Concepts/DDLCheck/25 Limitations and Scope|DDLCheck Limitations and Scope]].

## WriteCheck

The serial oracle depends on assumptions about how write conflicts are recognized and handled. Real DBMSs can intentionally use more permissive semantics such as [[Concepts/WriteCheck/27 Semi-Consistent Reads|Semi-Consistent Reads]] and different [[Concepts/WriteCheck/28 Gap Locks|Gap-Lock]] behavior.

# How to read this series

Read:

1. **This guide**
2. [[Guides/01 Understanding CODDTest]]
3. [[Guides/02 Understanding DDLCheck]]
4. [[Guides/03 Understanding WriteCheck]]
5. [[Guides/04 Three Papers, One Testing Idea]]

The Guides pages are designed to be read linearly.

The Concepts pages are for deeper explanation of individual terms.

The Papers pages are reference sheets with metadata, results, reading pointers, and links.

The original PDFs remain in PDFs/.

## Next

[[Guides/01 Understanding CODDTest|Part 1 — Understanding CODDTest]]
