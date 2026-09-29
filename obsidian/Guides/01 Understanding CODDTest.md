---
type: guide
series: ATDM database testing papers
order: 1
paper: CODDTest
tags: [guide, coddtest, metamorphic-testing, dbms-testing]
---

# Understanding CODDTest

**Paper:** [[Papers/01 CODDTest|Constant Optimization Driven Database System Testing]]

**PDF:** [[PDFs/CODDTest_SIGMOD2025.pdf]]

## 1. The problem: how do we know a query result is wrong?

Suppose a DBMS executes a generated query and returns:

    42

Did the DBMS behave correctly?

For arbitrary generated SQL, the tester usually does not already know the right answer. This is the [[Concepts/Shared/01 Test Oracle|Test Oracle]] problem.

A crash is easy to recognize:

    query → crash

A [[Concepts/Shared/02 Logic Bugs|Logic Bug]] is harder:

    query → plausible-looking result

The system may return a normal value even when that value is wrong.

CODDTest avoids implementing an independent SQL evaluator. Instead, it asks:

> Can we create another query that should mean the same thing and compare the two?

That is the central idea.

## 2. Metamorphic testing

The broader strategy is [[Concepts/Shared/03 Metamorphic Testing|Metamorphic Testing]].

Instead of requiring one known answer, the tester constructs two related inputs whose outputs should obey a known relation.

For CODDTest:

    original query O
          ↓
       result O

and:

    transformed query F
          ↓
       result F

The expected [[Concepts/CODDTest/03 Metamorphic Relation|Metamorphic Relation]] is:

    result(O) = result(F)

If they differ, something is inconsistent.

The rest of the paper explains how to construct F safely.

## 3. Constant folding

Consider a compiler expression:

    3 + 5

A compiler can evaluate it:

    3 + 5 → 8

This is [[Concepts/CODDTest/04 Constant Folding|Constant Folding]].

CODDTest borrows that idea for SQL.

Suppose expression φ is:

    SELECT MIN(c0) FROM t0

and, for the current database, the result is:

    1

CODDTest treats 1 as the folded result Rφ.

This is only valid relative to the current [[Concepts/Shared/05 Database State|Database State]]. If table contents change, MIN(c0) may change too.

An important clarification:

> CODDTest is not primarily testing whether the optimizer literally performs constant folding.

The authors use the optimization idea as a **testing transformation**.

## 4. Constant propagation

Once CODDTest knows:

    φ = 1

it substitutes that value into a query.

Original predicate:

    x IN (SELECT MIN(c0) FROM t0)

Folded predicate:

    x IN (1)

That substitution is [[Concepts/CODDTest/05 Constant Propagation|Constant Propagation]].

Remember the distinction:

    folding     = compute the value
    propagation = substitute the value

Together, these two operations explain the paper's name: Constant Optimization Driven Database System Testing.

## 5. A, O, and F

The paper becomes easier once three query roles are clear.

See [[Concepts/CODDTest/06 Original Auxiliary and Folded Queries|Original, Auxiliary, and Folded Queries]].

### A — auxiliary query

A evaluates the selected expression φ.

Example:

    SELECT MIN(c0) FROM t0;

Suppose the result is:

    Rφ = 1

### O — original query

O contains φ in its original form.

    SELECT ...
    WHERE x IN (SELECT MIN(c0) FROM t0);

### F — folded query

F contains Rφ instead.

    SELECT ...
    WHERE x IN (1);

The oracle compares O and F:

    result(O) ?= result(F)

A is not the query being compared. It exists to calculate the replacement value.

## 6. Independent expressions

Some expressions can be evaluated without knowing the current outer row.

Examples:

    LENGTH('abc') > 5

or:

    SELECT MIN(c0) FROM t0

These are [[Concepts/CODDTest/07A Independent Expressions|Independent Expressions]].

They may depend on database contents, but they do not depend on the outer row context.

That means CODDTest can usually evaluate them to one constant or constant list and substitute it directly.

## 7. Dependent expressions

Now consider:

    c0 + c1 > 0

Suppose the rows are:

| c0 | c1 | result |
|---:|---:|---:|
| -1 | 1 | 0 |
| 1 | 2 | 1 |

There is no one constant that represents the expression for every row.

This is a [[Concepts/CODDTest/07B Dependent Expressions|Dependent Expression]].

Correlated subqueries create the same kind of problem. See [[Concepts/CODDTest/09 Correlated and Non-correlated Subqueries|Correlated and Non-correlated Subqueries]].

CODDTest therefore computes a mapping:

    (-1, 1) → 0
    ( 1, 2) → 1

and represents it using [[Concepts/CODDTest/10 SQL CASE and Row Mapping|SQL CASE and Row Mapping]].

Conceptually:

    CASE
      WHEN c0=-1 AND c1=1 THEN 0
      WHEN c0= 1 AND c1=2 THEN 1
    END

This is the main complication after the basic idea.

## 8. Predicates and SQL NULL

CODDTest often places generated expressions inside [[Concepts/CODDTest/08A Predicates|Predicates]].

SQL conditions can produce three logical outcomes:

- TRUE;
- FALSE;
- UNKNOWN / NULL.

See [[Concepts/CODDTest/08B SQL Three-Valued Logic|SQL Three-Valued Logic]].

This matters because a transformation that mishandles NULL could change query semantics and create a false alarm.

The oracle is only useful when the transformation itself is valid.

## 9. Algorithm 1 in plain language

The paper's [[Concepts/Shared/10 Algorithmic Sketch|Algorithmic Sketch]] can be reduced to:

    1. Generate database state s
    2. Generate expression φ
    3. Determine whether φ is independent or dependent
    4. Build auxiliary query A
    5. Execute A to get Rφ
    6. Generate original query O containing φ
    7. Execute O
    8. Replace φ with Rφ to build F
    9. Execute F
   10. Compare O and F
   11. Report a mismatch

Or even more simply:

    choose φ
       ↓
    evaluate φ
       ↓
    build O and F
       ↓
    compare

The implementation uses [[Concepts/Shared/11 SQLancer|SQLancer]].

Query structure can be represented and transformed with an [[Concepts/CODDTest/15 Abstract Syntax Tree (AST)|Abstract Syntax Tree]].

## 10. How CODDTest differs from earlier test oracles

CODDTest is not the first DBMS technique to solve the oracle problem.

See [[Concepts/CODDTest/16 Existing Oracles - TLP NoREC PQS DQE|Existing Test Oracles]].

### TLP

[[Concepts/CODDTest/16A TLP - Ternary Logic Partitioning|TLP]] partitions data using:

    p
    NOT p
    p IS NULL

### NoREC

[[Concepts/CODDTest/16B NoREC - No Rewriting Required|NoREC]] compares a normal predicate computation with a logically equivalent alternate form.

### PQS

[[Concepts/CODDTest/16C PQS - Pivoted Query Synthesis|PQS]] chooses a known pivot row and generates a query that should contain it.

### DQE

[[Concepts/CODDTest/16D DQE - Differential Query Execution|DQE]] checks predicate behavior across SQL statement types.

CODDTest's distinctive transformation is:

> Evaluate an expression, then substitute the evaluated result.

The evaluation argues that this reaches bugs the compared techniques miss.

## 11. Our MySQL example

Our representative CODDTest reproduction is MySQL #111241.

The expression folds to:

    1

The constant-substituted form returns:

    1

The original scalar-subquery form returns:

    empty

So:

    result(constant form) ≠ result(subquery form)

Those forms should be semantically equivalent.

This is a direct [[Concepts/CODDTest/03 Metamorphic Relation|metamorphic-relation violation]].

Repository:

    repro/coddtest_111241.sh
    results/coddtest_111241.txt

## 12. What the evaluation shows

The authors evaluate CODDTest on:

- SQLite;
- MySQL;
- CockroachDB;
- DuckDB;
- TiDB.

The paper reports:

- 45 previously unknown bugs overall;
- 24 previously unknown logic bugs;
- 11 logic bugs not detected by the compared state-of-the-art test oracles.

The important point is not merely the bug count.

The authors are arguing that **constant optimization creates a meaningfully different oracle**.

## 13. Where the oracle can fail

Every equivalence relation has boundaries.

See [[Concepts/CODDTest/18 False Positives and Floating Point|False Positives and Floating Point]].

Potential difficulties include:

- floating-point representation;
- NULL semantics;
- dependent context;
- nondeterministic behavior;
- changing database state.

The general lesson is:

> A mismatch only indicates a DBMS bug if the transformation itself really preserves semantics.

## 14. Beyond predicates

The paper also extends the technique beyond simple WHERE predicates.

See [[Concepts/CODDTest/19 Beyond Predicates|Language Features Beyond Predicates]].

The general idea is broader:

> Evaluate a component under a fixed state, construct an equivalent constant representation, and compare behavior.

That is why the technique can reach multiple SQL language features.

# What to remember

If you remember five things, remember:

1. CODDTest solves the test-oracle problem with metamorphic testing.
2. Constant folding computes Rφ.
3. Constant propagation substitutes Rφ.
4. O and F should return the same result.
5. Independent expressions are easy; dependent expressions require per-row mappings.

For the compact concept synthesis:

[[Concepts/CODDTest/17 How CODDTest Fits Together]]

## Previous

[[Guides/00 The Three-Paper Story]]

## Next

[[Guides/02 Understanding DDLCheck|Part 2 — Understanding DDLCheck]]
