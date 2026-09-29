# Bug Report Reduction

## In one sentence

DDLCheck simplifies a generated failure until the remaining DDL history and SQL statements are close to the smallest case that still reproduces the bug.

## Why reduction matters

A generated test might contain:

    10 DDL statements
    + many test statements
    + one final failing statement

A developer does not want to debug all of that if most statements are irrelevant.

## Reduction targets

DDLCheck reduces:

- the generated DDL sequence seq_gen;
- the testing statements executed before the failure;
- the bug-revealing statement itself.

seq_syn can then be synthesized again from the reduced seq_gen.

## Basic strategy

Try removing something:

    remove statement
          ↓
    does bug still occur?
       /        \
     yes        no
      ↓          ↓
    keep      restore
    removed

Repeat until further simplification stops preserving the bug.

## Shared concept

See [[Concepts/Shared/09 Test Case Reduction|Test Case Reduction]].

## Why this helped our project

The published #114904 case is small enough that its stale-reference behavior can be explained on one slide and reproduced with a short script.
