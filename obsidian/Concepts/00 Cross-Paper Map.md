# Cross-Paper Concept Map

## One problem, three levels

All three papers need a [[Shared/01 Test Oracle|test oracle]] for DBMS behavior that may look valid even when it is wrong.

Their common strategy is to construct a second execution whose behavior is constrained by semantics.

## CODDTest — expression level

    expression φ
         ↓ evaluate
    constant result Rφ

Compare:

    original query O
         ≡
    folded query F

Core concepts:

- [[CODDTest/04 Constant Folding]]
- [[CODDTest/05 Constant Propagation]]
- [[CODDTest/03 Metamorphic Relation]]

## DDLCheck — schema-history level

    complex DDL history
         ↓
    visible schema S

Compare against:

    direct construction of S

Then execute the same later SQL on both databases.

Core concepts:

- [[DDLCheck/02 Schema Evolution]]
- [[DDLCheck/04 Schema-Related Information]]
- [[DDLCheck/06 Equivalent Databases]]
- [[DDLCheck/14 DDLCheck Oracle]]

## WriteCheck — transaction-schedule level

    submitted transaction interleaving
         ↓
    actual concurrent schedule H_con
         ↓
    observed final state

Infer:

    FCRFS serial schedule H_ser
         ↓
    serial final state

Compare:

    state(H_con)
         ≡
    state(H_ser)

Core concepts:

- [[WriteCheck/11 Write-Specific Serializability (WSS)]]
- [[WriteCheck/14 FCRFS Serial Pattern]]
- [[WriteCheck/22 Submitted Order vs Actual Schedule]]
- [[WriteCheck/26 Final-State Comparison]]

## Shared pattern

    construct two executions
    that should be equivalent
             ↓
         execute both
             ↓
          compare
             ↓
      mismatch = bug candidate

See [[Shared/04 Equivalence-Based Testing]].

## What each paper manufactures

| Paper | What it constructs as the reference |
|---|---|
| CODDTest | Folded query F |
| DDLCheck | Directly synthesized database db_syn |
| WriteCheck | FCRFS serial schedule H_ser |

## Progression through the DBMS

    expression semantics
            ↓
       schema history
            ↓
    transaction behavior

That progression is the main narrative connecting the three papers in the presentation.

## Reproduction note

Our three MySQL demonstrations all use MySQL 8.0.32.

For WriteCheck, the executable project replay uses Troc's testcase and MVCC oracle, so it should be presented as a **representative transaction-bug replay**, not as a direct rerun of WriteCheck.
