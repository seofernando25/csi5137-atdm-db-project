# SQL CASE and Row Mapping

SQL CASE expresses conditional values.

A simple mental model is:

IF condition A → value A  
ELSE IF condition B → value B  
ELSE → value C

## Why CODDTest uses CASE

A dependent expression may have a different folded value for each outer row.

Suppose:

| c0 | c1 | φ |
|---:|---:|---:|
| -1 | 1 | 0 |
| 1 | 2 | 1 |

CODDTest needs to encode:

- row (-1, 1) → 0
- row (1, 2) → 1

It can represent that mapping with a CASE expression.

## Mental model

CASE acts like a lookup table:

outer-row values → evaluated result of φ

This is how CODDTest performs per-row constant propagation for [[07 Independent and Dependent Expressions|dependent expressions]].

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]
