# Dependent Expressions

## In one sentence

A **dependent expression** uses values from the outer query context, so its result can be different for different rows.

## Tiny example

Suppose:

    φ = c0 + c1 > 0

and the table contains:

| c0 | c1 | φ |
|---:|---:|---:|
| -1 | 1 | 0 |
| 1 | 2 | 1 |

There is no single global constant for φ.

## Why CODDTest cares

CODDTest must preserve the result **for each relevant row**.

So instead of:

    φ → 1

it needs a mapping:

    (-1, 1) → 0
    ( 1, 2) → 1

CODDTest represents that mapping using [[10 SQL CASE and Row Mapping|SQL CASE]].

## Correlated subqueries

A correlated subquery is a common dependent expression because it refers to columns from the outer query.

See [[09 Correlated and Non-correlated Subqueries]].

## Don't confuse it with

A dependent expression is not necessarily nondeterministic.

It can be fully deterministic while still producing different values for different outer rows.

## Related

- [[07 Independent and Dependent Expressions]]
- [[10 SQL CASE and Row Mapping]]
- [[13 Algorithmic Sketch]]

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=8]]
