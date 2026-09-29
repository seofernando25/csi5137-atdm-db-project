# Existing Oracles — TLP, NoREC, PQS, DQE

CODDTest compares itself with several existing DBMS-testing approaches.

The important thing is to understand the **oracle idea** behind each technique, not memorize every implementation detail.

## TLP — Ternary Logic Partitioning

Partition the data using:

- predicate p;
- NOT p;
- p IS NULL.

The partitions should reconstruct the result of the original unpartitioned query.

TLP exploits SQL's [[08 Predicates and Three-Valued Logic|three-valued logic]].

## NoREC — No Rewriting Required

NoREC reformulates predicate evaluation so two logically equivalent computations can be compared, often using aggregate counts.

Its goal is to reveal wrong-result bugs associated with query optimization.

## PQS — Pivoted Query Synthesis

PQS selects a known **pivot row** and generates a query that should contain that row according to an internal expression evaluator.

Unlike a pure equality comparison between complete query results, PQS manufactures a known expected property.

## DQE — Differential Query Execution

DQE checks whether a predicate behaves consistently across different statement contexts, such as SELECT, UPDATE, and DELETE.

## CODDTest's difference

CODDTest evaluates an expression and substitutes its result to construct the follow-up query.

The authors argue this allows CODDTest to reach language features and bug patterns that the compared oracles cannot easily expose.

## Presentation sentence

> All of these techniques solve the test-oracle problem differently; CODDTest's novelty is using constant optimization as the metamorphic transformation.

Paper comparison section: [[PDFs/CODDTest_SIGMOD2025.pdf#page=15]]
