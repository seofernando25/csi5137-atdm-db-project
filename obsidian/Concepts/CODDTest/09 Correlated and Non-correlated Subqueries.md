# Correlated and Non-correlated Subqueries

## Non-correlated subquery

A non-correlated subquery does not reference the outer query.

Example conceptually:

SELECT rows FROM t1  
WHERE x > (SELECT AVG(x) FROM t2)

The inner query can be evaluated independently of each outer row.

This naturally fits CODDTest's [[07 Independent and Dependent Expressions|independent-expression]] case.

## Correlated subquery

A correlated subquery references columns from the outer query.

Example conceptually:

For each student, calculate the average score of that student's class.

The result depends on the current outer row, so the expression can produce a different value for different rows.

This is a [[07 Independent and Dependent Expressions|dependent expression]].

## Why subqueries matter

Subqueries are both:

1. an important SQL feature that can contain DBMS logic bugs;
2. a reason that simply replacing an expression with one global constant is not enough.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]
