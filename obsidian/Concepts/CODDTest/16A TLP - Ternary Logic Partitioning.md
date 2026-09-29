# TLP — Ternary Logic Partitioning

## In one sentence

TLP partitions a query according to the three possible outcomes of a predicate and checks that recombining the partitions preserves the original result.

## Core partition

For predicate p:

    p
    NOT p
    p IS NULL

These correspond to SQL's TRUE, FALSE, and UNKNOWN cases.

## Tiny mental example

Instead of querying all rows at once, query:

1. rows where p is true;
2. rows where p is false;
3. rows where p is unknown.

Together, the partitions should account for the same logical population as the original query.

## Why CODDTest compares against it

TLP's oracle is tied strongly to predicate partitioning and [[08B SQL Three-Valued Logic|three-valued logic]].

CODDTest instead transforms an arbitrary selected expression by folding and propagation.

## Don't confuse it with

TLP does not need to know the correct result either. It is also a metamorphic-testing technique.
