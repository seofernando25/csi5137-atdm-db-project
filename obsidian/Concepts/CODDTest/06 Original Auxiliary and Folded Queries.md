# Original, Auxiliary, and Folded Queries

CODDTest uses three query roles.

## A — Auxiliary query

Purpose: evaluate selected expression φ.

Example: SELECT MIN(c0) FROM t0.

Suppose the result is 1.

## O — Original query

Contains φ in its original form, for example a predicate containing the MIN subquery.

## F — Folded query

Contains the evaluated result Rφ instead of φ.

## Flow

A → evaluate φ → Rφ

O contains φ → result O  
F contains Rφ → result F

Expected relation: result O = result F.

If they disagree, [[03 Metamorphic Relation|the metamorphic relation]] is violated.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=5]]
