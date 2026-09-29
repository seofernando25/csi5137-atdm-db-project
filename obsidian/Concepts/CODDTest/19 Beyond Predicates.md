# Language Features Beyond Predicates

CODDTest's introductory explanation focuses on expressions used in [[08 Predicates and Three-Valued Logic|predicates]], but the paper extends the same idea beyond predicates.

The paper discusses testing contexts involving:

- INSERT;
- common table expressions, or CTEs;
- derived tables;
- table-value constructors.

## Generalization

The technique is broader than replacing a Boolean expression with TRUE or FALSE.

The deeper rule is:

> Evaluate a query component under a fixed state, construct an equivalent constant representation, and compare behavior.

## Why this matters

This broader scope supports the paper's argument that CODDTest can expose bugs involving SQL language features that other test oracles do not naturally exercise.

Paper Section 3.4: [[PDFs/CODDTest_SIGMOD2025.pdf#page=10]]
