# Original, Auxiliary, and Folded Queries

## In one sentence

CODDTest uses three query roles: **A evaluates the expression, O contains the original expression, and F contains the evaluated replacement**.

## A — Auxiliary query

Purpose: compute the selected expression φ.

Example:

    SELECT MIN(c0) FROM t0

Suppose A returns 1.

## O — Original query

O contains φ in its original form.

Conceptually:

    SELECT ...
    WHERE x IN (SELECT MIN(c0) FROM t0)

## F — Folded query

F replaces φ with the evaluated result Rφ.

Conceptually:

    SELECT ...
    WHERE x IN (1)

## Why CODDTest cares

The entire oracle becomes:

    A computes Rφ
           ↓
    O contains φ      F contains Rφ
           ↓                 ↓
       result O     ?=    result F

If O and F disagree, [[03 Metamorphic Relation|the metamorphic relation]] is violated.

## Don't confuse them

- A is not compared against O.
- A exists to compute the replacement value.
- O and F are the two queries whose results are compared.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=5]]
