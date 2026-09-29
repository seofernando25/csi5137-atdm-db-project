# Metamorphic Relation

## In one sentence

A **metamorphic relation** is the rule that says how the outputs of the original and transformed inputs should relate.

## CODDTest's relation

CODDTest expects:

    E_s(O) = E_s(F)

where:

- E is the DBMS engine;
- s is a fixed [[11 Database State|database state]];
- O is the original query;
- F is the folded query.

## Tiny example

If two queries are semantically equivalent:

    original query → [1, 2]
    folded query   → [1, 2]

the relation holds.

If:

    original query → [1, 2]
    folded query   → [1]

the relation is violated.

## Why CODDTest cares

The metamorphic relation **is the oracle**.

CODDTest does not need to know which result is correct. A disagreement is already evidence that something is inconsistent.

## Don't confuse it with

A metamorphic relation is not just "two queries look similar."

It is a semantic claim that must be valid under the assumptions of the transformation.

See [[18 False Positives and Floating Point]].

## Related

- [[02 Metamorphic Testing]]
- [[11 Database State]]
- [[06 Original Auxiliary and Folded Queries]]
