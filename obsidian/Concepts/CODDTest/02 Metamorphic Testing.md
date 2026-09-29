# Metamorphic Testing

## In one sentence

**Metamorphic testing** tests software by transforming an input into a related input whose output should have a known relationship to the original output.

## Tiny example

Suppose we cannot calculate the correct answer for input I.

We can still do:

    input I  → output O
    input I' → output O'

if we know how O and O' should relate.

## Why CODDTest cares

CODDTest does not know the correct answer to an arbitrary SQL query.

Instead it creates:

- original query O;
- transformed, folded query F.

The two queries should return the same result.

So the test becomes:

    result(O) ?= result(F)

## The key term

The expected relationship between the two outputs is called a [[03 Metamorphic Relation|metamorphic relation]].

## Don't confuse it with

**Differential testing** often compares different implementations running the same input.

Metamorphic testing can test **one implementation** by comparing related inputs.

## Related

- [[01 Test Oracle]]
- [[03 Metamorphic Relation]]
- [[16 Existing Oracles - TLP NoREC PQS DQE]]

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]
