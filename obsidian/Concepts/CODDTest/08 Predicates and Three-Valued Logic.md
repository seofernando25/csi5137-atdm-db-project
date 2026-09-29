# Predicates and Three-Valued Logic

A SQL **predicate** is an expression used as a condition.

Examples include:

- x > 10
- name IS NULL
- a IN (1, 2, 3)

Predicates are used in WHERE, JOIN ... ON, HAVING, and other clauses.

## SQL is not ordinary Boolean logic

A SQL predicate can evaluate to:

- TRUE
- FALSE
- NULL / UNKNOWN

For example, NULL = NULL does not evaluate to TRUE; it evaluates to UNKNOWN.

## Why CODDTest cares

CODDTest often places generated expressions inside predicates and then substitutes folded values.

The transformation must preserve SQL's three-valued semantics. Otherwise the testing method itself could change the query's meaning and produce a false alarm.

Related: [[18 False Positives and Floating Point]]
