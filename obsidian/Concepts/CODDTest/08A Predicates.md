# Predicates

## In one sentence

A **predicate** is an SQL expression used as a condition.

## Examples

    x > 10
    name IS NULL
    a IN (1, 2, 3)

## Where predicates appear

Common contexts include:

- WHERE
- JOIN ... ON
- HAVING
- UPDATE conditions
- DELETE conditions

## Why CODDTest cares

CODDTest commonly generates an expression φ and places it inside a predicate of an original query.

It then folds φ and constructs an equivalent folded predicate.

## Don't confuse it with

A predicate is not necessarily just TRUE or FALSE in SQL.

Because of NULL, it can also evaluate to UNKNOWN.

See [[08B SQL Three-Valued Logic]].

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]
