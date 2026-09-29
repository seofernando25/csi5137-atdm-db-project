# Independent and Dependent Expressions

This is the main technical complication after the basic CODDTest idea.

## Independent expression

An expression is **independent** when it does not depend on values from an outer query row.

Examples:

- LENGTH('abc') > 5
- a non-correlated subquery such as SELECT MIN(c0) FROM t0

Under a fixed database state, one constant or constant list can represent the result.

## Dependent expression

A **dependent expression** references outer-context columns and can evaluate differently for each row.

Example: c0 + c1 > 0.

| c0 | c1 | result |
|---:|---:|---|
| -1 | 1 | false |
| 1 | 2 | true |

One global constant is not enough. CODDTest therefore builds a row-to-result mapping and represents it using [[10 SQL CASE and Row Mapping|CASE]].

## How Algorithm 1 classifies them

The generated expression comes with the set of referenced outer columns.

- no referenced outer columns → independent;
- one or more referenced outer columns → dependent.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=6]]  
Independent expressions: [[PDFs/CODDTest_SIGMOD2025.pdf#page=7]]  
Dependent expressions: [[PDFs/CODDTest_SIGMOD2025.pdf#page=8]]
