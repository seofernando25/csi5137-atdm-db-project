# Metamorphic Testing

## In one sentence

**Metamorphic testing** derives a follow-up input from an existing input and checks a known relationship between their outputs.

## Tiny model

    input I  → output O
    input I' → output O'

The tester may not know the exact correct value of O, but it knows how O and O' should relate.

## CODDTest

CODDTest explicitly uses metamorphic testing:

    original query O
        ≡
    folded query F

The expected relationship is equality of results.

## DDLCheck connection

DDLCheck is best described in our notebook more generally as **equivalence-based testing**: two schema histories produce equivalent visible schemas and should behave equivalently.

That is closely related to the metamorphic-testing mindset, but we should not relabel the authors' technique more strongly than the paper does.

## Related

- [[04 Equivalence-Based Testing]]
- [[01 Test Oracle]]
