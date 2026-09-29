# Independent Expressions

## In one sentence

An **independent expression** can be evaluated without knowing values from the surrounding outer query row.

## Tiny examples

A literal expression:

    LENGTH('abc') > 5

A non-correlated subquery:

    SELECT MIN(c0) FROM t0

Neither needs an outer-row value.

## Why CODDTest cares

Because the expression is independent, CODDTest can evaluate it once and use one constant or constant list as its folded representation.

Example:

    SELECT MIN(c0) FROM t0  →  1

Then CODDTest can propagate 1 into the folded query.

## Don't confuse it with

"Independent" does **not** mean independent of the database.

A non-correlated subquery can still depend on table contents.

It means independent of the **outer query context**.

## Related

- [[07 Independent and Dependent Expressions]]
- [[09 Correlated and Non-correlated Subqueries]]
- [[04 Constant Folding]]

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=7]]
