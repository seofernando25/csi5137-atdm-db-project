# Independent and Dependent Expressions

This page is the comparison. Read the two child notes for the details.

| | [[07A Independent Expressions|Independent]] | [[07B Dependent Expressions|Dependent]] |
|---|---|---|
| Uses outer-row columns? | No | Yes |
| Result | One constant or constant list | May differ per row |
| Folding | Evaluate once | Evaluate for each relevant row/context |
| Propagation | Direct constant replacement | Row-to-result mapping |
| Common example | Non-correlated subquery | Correlated subquery |

## Quick test

Ask:

> Can I evaluate φ without knowing the current outer row?

If **yes**, φ is independent.

If **no**, φ is dependent.

## Why this split matters

The basic CODDTest idea is easy for independent expressions.

Dependent expressions are where the technique becomes more interesting because one global constant is not enough.

## Continue

- [[07A Independent Expressions]]
- [[07B Dependent Expressions]]
- [[10 SQL CASE and Row Mapping]]
