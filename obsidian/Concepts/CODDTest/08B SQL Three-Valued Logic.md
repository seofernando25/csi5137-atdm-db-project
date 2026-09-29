# SQL Three-Valued Logic

## In one sentence

SQL conditions can evaluate to **TRUE, FALSE, or UNKNOWN**, rather than only TRUE or FALSE.

## Tiny example

    NULL = NULL

does not evaluate to TRUE.

It evaluates to UNKNOWN.

## Why CODDTest cares

CODDTest transforms expressions while expecting the query's semantics to remain unchanged.

If the transformation mishandles NULL/UNKNOWN behavior, the test could report a mismatch caused by the transformation itself instead of a DBMS bug.

## Connection to TLP

[[16A TLP - Ternary Logic Partitioning|TLP]] explicitly uses SQL's three logical outcomes:

- p
- NOT p
- p IS NULL

## Don't confuse it with

UNKNOWN is not the same as FALSE.

That distinction is fundamental in SQL predicates.

## Related

- [[08A Predicates]]
- [[18 False Positives and Floating Point]]
