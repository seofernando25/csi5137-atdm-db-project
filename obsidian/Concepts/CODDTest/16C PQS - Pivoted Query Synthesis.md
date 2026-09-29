# PQS — Pivoted Query Synthesis

## In one sentence

PQS chooses a known **pivot row** and synthesizes a query that should include that row.

## Core intuition

If the tester knows a specific row should satisfy a generated predicate, then:

    generated query → must contain pivot row

If the DBMS omits that row, the query result is wrong.

## Why this is different

PQS creates a **known expected property** of the result.

CODDTest instead compares two semantically equivalent complete executions.

## Extra machinery

PQS needs its own mechanism for evaluating generated expressions so it can construct predicates that are known to be true for the pivot row.

## Why CODDTest compares against it

Both target DBMS logic bugs, but they solve the oracle problem in different ways:

- PQS: manufacture a known row that must appear;
- CODDTest: manufacture an equivalent folded query.
