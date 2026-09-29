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

Then execute the same later SQL on both.

Core concepts:

- [[DDLCheck/02 Schema Evolution]]
- [[DDLCheck/04 Schema-Related Information]]
- [[DDLCheck/06 Equivalent Databases]]
- [[DDLCheck/14 DDLCheck Oracle]]

## WriteCheck — transaction level

    concurrent schedule
         ↓
    observed final state

Compare against an execution/state oracle expected by the concurrency model.

The detailed WriteCheck concept graph will be added next.

## Shared pattern

    construct two things
    that should be equivalent
             ↓
         execute both
             ↓
          compare
             ↓
      mismatch = bug candidate

See [[Shared/04 Equivalence-Based Testing]].

## Progression through the DBMS

    expression semantics
            ↓
       schema state
            ↓
    transaction behavior

This progression is the main narrative connecting the three papers in the presentation.
