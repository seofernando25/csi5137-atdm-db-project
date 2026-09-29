# Predicates and Three-Valued Logic

These concepts are related but distinct.

## Predicate

A [[08A Predicates|predicate]] is a SQL condition such as x > 10 or name IS NULL.

## Three-valued logic

[[08B SQL Three-Valued Logic|SQL three-valued logic]] means predicates can evaluate to:

- TRUE
- FALSE
- UNKNOWN / NULL

## Why they belong together in CODDTest

CODDTest frequently embeds generated expressions inside predicates.

To preserve semantics when folding and propagating those expressions, it must respect SQL's NULL/UNKNOWN behavior.

## Continue

- [[08A Predicates]]
- [[08B SQL Three-Valued Logic]]
