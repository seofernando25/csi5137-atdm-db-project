# DQE — Differential Query Execution

## In one sentence

DQE checks whether equivalent predicate behavior remains consistent across different SQL statement types.

## Core intuition

A predicate used in contexts such as:

- SELECT
- UPDATE
- DELETE

should retain compatible semantics.

If the predicate appears to identify one set of rows in SELECT but affects a different set in UPDATE or DELETE, there may be a DBMS bug.

## Why CODDTest compares against it

DQE changes the **statement context** around a predicate.

CODDTest changes an **expression inside the query** by replacing it with its evaluated result.

These transformations expose different bug classes.

## Don't confuse it with

DQE is not the same as DQP (Differential Query Plans).

DQE varies execution through SQL statement contexts; DQP compares different query plans for the same query.
