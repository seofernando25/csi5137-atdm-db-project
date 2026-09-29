# Equivalence-Based Testing

## In one sentence

**Equivalence-based testing** creates two executions that should have the same semantics and treats disagreement as evidence of a bug.

## Three levels in our project

### CODDTest — expression/query level

    expression φ
    vs
    evaluated constant Rφ

### DDLCheck — schema/history level

    complex DDL history
    vs
    direct construction of the same schema

### WriteCheck — transaction level

    concurrent execution
    vs
    an oracle execution/state

## Why this is the presentation's unifying idea

The transformations are different, but the oracle shape is the same:

    construct equivalent alternatives
              ↓
        execute both
              ↓
          compare
              ↓
      mismatch = bug candidate

## Related

- [[01 Test Oracle]]
- [[03 Metamorphic Testing]]
