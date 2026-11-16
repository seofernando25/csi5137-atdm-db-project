---
type: guide
series: ATDM database testing papers
order: 4
tags: [guide, synthesis, database-testing, csi5137, atdm]
---

# Three Papers, One Testing Idea

This is the synthesis guide for:

- [[Guides/01 Understanding CODDTest|CODDTest]];
- [[Guides/02 Understanding DDLCheck|DDLCheck]];
- [[Guides/03 Understanding WriteCheck|WriteCheck]];
- Radar (metadata removal; MySQL #110125: indexed_rows=1 vs raw_rows=0). No dedicated guide yet.

The goal is not to repeat each paper.

The goal is to understand why these four papers belong in one presentation.

# 1. Start with the oracle problem

All four papers test DBMS behavior that can fail silently.

A query can return the wrong rows.

A schema can look correct while hidden metadata is stale.

Transactions can commit while leaving the wrong database state.

That gives us one shared question:

> **How can an automated tester know the DBMS is wrong when it does not already know the correct answer?**

That is the [[Concepts/Shared/01 Test Oracle|Test Oracle]] problem.

The shared answer is [[Concepts/Shared/04 Equivalence-Based Testing|Equivalence-Based Testing]].

Instead of precomputing one perfect answer, construct another execution whose behavior should be equivalent.

    execution A
        ≡
    execution B
        ↓
    run both
        ↓
    compare
        ↓
    disagreement = bug candidate

# 2. CODDTest — equivalent query semantics

CODDTest works at the smallest level: an expression inside a query.

Start with expression φ.

Use an auxiliary query to evaluate it:

    φ → Rφ

Then compare:

    original query O containing φ

against:

    folded query F containing Rφ

Expected:

    result(O) = result(F)

The transformation uses:

- [[Concepts/CODDTest/04 Constant Folding|Constant Folding]];
- [[Concepts/CODDTest/05 Constant Propagation|Constant Propagation]].

The overall strategy is [[Concepts/Shared/03 Metamorphic Testing|Metamorphic Testing]].

### What CODDTest manufactures

A **folded query**.

### What remains invariant

The **query result**.

### Main bug surface

Query-expression / optimizer / semantic logic bugs.

### Project example

MySQL #111241:

    folded value = 1
    constant form = row 1
    subquery form = empty

Equivalent query forms disagree.

# 3. DDLCheck — equivalent schema semantics

DDLCheck moves up one level.

The object being changed is the **history used to construct a database schema**.

One path is complex:

    seq_gen
      ↓
    CREATE → ALTER → DROP → RENAME → ...
      ↓
    db_gen

The second path is synthesized from the final visible schema:

    final schema
      ↓
    direct construction seq_syn
      ↓
    db_syn

Expected:

    schema(db_gen) = schema(db_syn)

Then execute the same later SQL q:

    behavior(db_gen, q)
          =
    behavior(db_syn, q)

### What DDLCheck manufactures

A **directly constructed equivalent database**.

### What remains invariant

Later observable database behavior:

- errors;
- query results;
- resulting data state.

### Main bug surface

Schema-evolution / metadata / downstream optimizer logic.

### Project example

MySQL #114904:

    visible foreign key → t2

but stale internal metadata still remembers:

    t0

The evolved schema rejects a valid INSERT while the directly created schema accepts it.

# 4. WriteCheck — equivalent transaction effects

WriteCheck moves to concurrent execution.

The tester observes:

    actual concurrent schedule H_con

Then infers:

    corresponding serial schedule H_ser

using [[Concepts/WriteCheck/14 FCRFS Serial Pattern|FCRFS]].

Under [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)|WSS]], the expected relation is:

    final_state(H_con)
          =
    final_state(H_ser)

### What WriteCheck manufactures

An **inferred serial execution**.

### What remains invariant

The relevant write effects / final database state.

### Main bug surface

Transaction-processing / concurrency-control logic.

### Project example

Our MySQL #104833 replay shows:

    observed state
    [10, 1, 10, 20, 10, 20]

versus:

    Troc MVCC oracle
    [10, 20, 10, 20, 10, 20]

Important: our runnable demonstration uses Troc's testcase and MVCC oracle rather than a direct WriteCheck run.

# 5. One table that connects everything

| Question | CODDTest | DDLCheck | WriteCheck |
|---|---|---|---|
| DBMS layer | Query / expression | Schema / history | Transactions / concurrency |
| Original object | Query O | Evolved db_gen | Concurrent H_con |
| Constructed reference | Folded query F | Direct db_syn | Serial H_ser |
| Transformation | Replace expression by evaluated value | Rebuild same visible schema directly | Infer FCRFS serial order |
| Invariant | Same query result | Same later behavior | Same final write state |
| Main bug surface | Query logic | Schema-related logic | Transaction logic |
| Key boundary | Expression substitution semantics | Schema equivalence | Write-conflict assumptions |

This is the central comparison for the presentation.

# 6. The progression in scale

The papers form a natural progression.

## Expression

CODDTest asks:

> If an expression already evaluated to a value, can I substitute that value without changing the query result?

## Schema

DDLCheck asks:

> If two histories produce the same visible schema, should future behavior depend on which history happened?

## Transaction

WriteCheck asks:

> If a concurrent execution corresponds to this serial write order, should the final database state differ?

So the story moves outward through the DBMS:

    expression
        ↓
      schema
        ↓
    transaction

At every level, the tester manufactures an equivalent alternative.

# 7. The reference becomes harder to construct

There is another progression.

## CODDTest reference

Relatively local:

    φ → Rφ

Then substitute Rφ.

## DDLCheck reference

Requires reconstructing an entire schema.

The tester must:

- inspect system catalogs;
- understand constraints;
- order dependencies;
- handle foreign keys.

## WriteCheck reference

Depends on runtime concurrency behavior.

The tester must:

- distinguish submitted vs actual schedule;
- track blocking;
- track aborts and commits;
- infer a valid serial ordering.

The papers therefore solve increasingly difficult oracle-construction problems while preserving the same high-level philosophy.

# 8. Every oracle has assumptions

Equivalence-based testing only works when the proposed equivalence is valid.

This gives us a second shared theme:

> **The oracle's assumptions matter as much as the transformation.**

## CODDTest

Potential boundary cases include:

- NULL semantics;
- floating point;
- context-dependent expressions;
- database-state changes.

See [[Concepts/CODDTest/18 False Positives and Floating Point|False Positives and Floating Point]].

## DDLCheck

Potential boundaries include:

- how schema equivalence is defined;
- nondeterministic later SQL;
- DBMS-specific catalog behavior;
- incomplete feature coverage.

See [[Concepts/DDLCheck/25 Limitations and Scope|DDLCheck Limitations and Scope]].

## WriteCheck

The correctness argument depends on [[Concepts/WriteCheck/16 WSS Correctness Assumption|Assumption 1]].

Mechanisms such as:

- [[Concepts/WriteCheck/27 Semi-Consistent Reads|Semi-Consistent Reads]];
- [[Concepts/WriteCheck/28 Gap Locks|Gap-Lock Differences]]

can place real DBMS behavior outside the oracle's assumption.

That can produce developer-classified false positives.

The general lesson is:

> An oracle can judge correctness only relative to a semantic contract.

# 9. All four also need good test generation

An oracle does not help if the tester never generates interesting inputs.

CODDTest uses [[Concepts/Shared/11 SQLancer|SQLancer]] to generate database states, expressions, and queries.

DDLCheck uses [[Concepts/Shared/07 Stateful Test Generation|Stateful Test Generation]] and [[Concepts/Shared/08 Grammar-Based Test Generation|Grammar-Based Test Generation]] to create valid evolution histories.

WriteCheck generates small transaction groups and randomized statement orders, motivated by the [[Concepts/WriteCheck/18 Small-Scope Hypothesis|Small-Scope Hypothesis]].

So every paper really solves two problems:

    What should I test?

and:

    How do I know whether the result is wrong?

The second question is what makes these papers especially coherent as a set.

# 10. Why one MySQL baseline is useful for our project

The papers evaluate multiple DBMSs and different versions.

For the class project, we use one shared baseline:

    MySQL 8.0.32

That gives us three demonstrations at three DBMS layers:

    MySQL 8.0.32
        │
        ├── query/expression inconsistency
        │   CODDTest #111241
        │
        ├── schema-history inconsistency
        │   DDLCheck #114904
        │
        └── transaction-state inconsistency
            project replay #104833

This should not be presented as evidence that MySQL is more buggy than another DBMS.

The point is methodological:

> Three different oracle constructions expose three different correctness surfaces in one mature system.

# 11. What the audience should remember

A good 25-minute presentation should leave the audience with three levels of memory.

## Level 1 — one sentence

> When we do not know the right answer, construct another execution that should be equivalent and compare them.

## Level 2 — one transformation per paper

    CODDTest:
    expression → constant

    DDLCheck:
    evolved schema → direct schema

    WriteCheck:
    concurrent schedule → serial schedule

## Level 3 — one concrete bug per paper

    CODDTest #111241
    equivalent query forms disagree

    DDLCheck #114904
    visible rename succeeds, stale FK metadata remains

    transaction #104833
    concurrent final state disagrees with oracle state

If those three layers are clear, the presentation feels like one research story rather than three unrelated paper summaries.

# Final map

    TEST ORACLE PROBLEM
            │
            ▼
    EQUIVALENCE-BASED TESTING
       /         |          \
      /          |           \
     ▼           ▼            ▼
  CODDTest    DDLCheck     WriteCheck

  query       schema       transaction
  meaning     history      schedule

  O ≡ F       db_gen ≡     H_con ≡
              db_syn       H_ser

      \          |          /
       \         |         /
        ▼        ▼        ▼
      compare observable behavior
                 ↓
       mismatch = bug candidate

That is the three-paper story.

## Previous

[[Guides/03 Understanding WriteCheck|Part 3 — Understanding WriteCheck]]

## Return home

[[00 Home]]
