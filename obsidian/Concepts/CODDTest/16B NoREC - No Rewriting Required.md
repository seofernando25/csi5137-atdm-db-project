# NoREC — No Rewriting Required

## In one sentence

NoREC checks query correctness by comparing a normal optimized query with an equivalent form that makes predicate evaluation more explicit.

## Core intuition

A DBMS optimizer may incorrectly transform a WHERE predicate.

NoREC constructs an alternate computation—often based on explicitly evaluating the predicate and comparing counts—so the two equivalent executions can be checked against each other.

## Why CODDTest compares against it

Both techniques look for wrong-result bugs without a known expected answer.

The transformation is different:

- NoREC changes how the predicate/result is computed;
- CODDTest evaluates an expression and substitutes its computed value.

## Don't confuse it with

NoREC is not simply "disable the optimizer."

Its strength comes from constructing a logically equivalent query form whose result can be compared to the original.
