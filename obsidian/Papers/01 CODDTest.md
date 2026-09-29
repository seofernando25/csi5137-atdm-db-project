---
type: paper
title: Constant Optimization Driven Database System Testing
authors: [Chi Zhang, Manuel Rigger]
venue: PACMMOD / SIGMOD
year: 2025
tags: [paper, coddtest, metamorphic-testing, dbms-testing]
---

# CODDTest — Constant Optimization Driven Database System Testing

[[Guides/01 Understanding CODDTest|Narrative guide]]

**PDF:** [[PDFs/CODDTest_SIGMOD2025.pdf]]  
**Preprint:** https://arxiv.org/abs/2501.11252  
**DOI:** https://doi.org/10.1145/3709674

## Thesis

CODDTest turns [[Concepts/CODDTest/04 Constant Folding|constant folding]] and [[Concepts/CODDTest/05 Constant Propagation|constant propagation]] into a [[Concepts/Shared/01 Test Oracle|test oracle]]. It evaluates an SQL expression under a fixed database state, replaces that expression with its computed value, and verifies that the original and transformed queries agree.

## Core notation

- s: [[Concepts/Shared/05 Database State|database state]]
- φ: expression selected for folding
- A: [[Concepts/CODDTest/06 Original Auxiliary and Folded Queries|auxiliary query]]
- O: original query
- Rφ: evaluated result of φ
- F: folded query

The metamorphic invariant is E_s(O) = E_s(F).

## Six-step method

1. Initialize a non-empty database state.
2. Generate expression φ.
3. Evaluate φ using A — folding.
4. Generate original query O containing φ.
5. Replace φ with Rφ — propagation — producing F.
6. Execute O and F; a mismatch is a bug candidate.

## Concept map

[[Concepts/CODDTest/00 Concept Map]]

## Evaluation

The paper evaluates SQLite, MySQL, CockroachDB, DuckDB, and TiDB. The authors report 45 previously unknown bugs, including 24 logic bugs, and state that 11 logic bugs were not detected by the compared state-of-the-art oracles.

## Our reproduction

MySQL #111241 on MySQL 8.0.32:

- folded value = 1
- constant-substituted form returns 1
- original scalar-subquery form returns no row

Repository result: ../results/coddtest_111241.txt

## Reading pointers

- Background: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]
- Approach: [[PDFs/CODDTest_SIGMOD2025.pdf#page=5]]
- Algorithm 1: [[PDFs/CODDTest_SIGMOD2025.pdf#page=6]]
- Independent expressions: [[PDFs/CODDTest_SIGMOD2025.pdf#page=7]]
- Dependent expressions: [[PDFs/CODDTest_SIGMOD2025.pdf#page=8]]
- Evaluation: [[PDFs/CODDTest_SIGMOD2025.pdf#page=12]]
