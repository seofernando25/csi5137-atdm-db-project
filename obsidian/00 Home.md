---
type: index
course: CSI 5137
course_name: Advanced Topics in Databases and Data Management
tags: [atdm, database-testing, papers]
---

# CSI 5137 — ATDM Paper Notebook

This vault decomposes the four class-project papers (Radar is covered in the cross-paper map) into small, linked study notes.

## Start here

1. [[Concepts/00 Cross-Paper Map]]
2. [[Concepts/Shared/00 Shared Concepts]]
3. Choose a paper concept map.

## Read as a narrative series

If you want to learn the papers front-to-back rather than browse individual concepts:

1. [[Guides/00 The Three-Paper Story]]
2. [[Guides/01 Understanding CODDTest]]
3. [[Guides/02 Understanding DDLCheck]]
4. [[Guides/03 Understanding WriteCheck]]
5. [[Guides/04 Three Papers, One Testing Idea]]

The guides are continuous explanations. Important terminology links out to the smaller concept notes when you want more detail.

## Papers

### 1. CODDTest

[[Papers/01 CODDTest|Paper note]] · [[PDFs/CODDTest_SIGMOD2025.pdf|PDF]] · [[Concepts/CODDTest/00 Concept Map|Concept map]]

Focus:

> Evaluate an expression, substitute the result, and compare equivalent queries.

### 2. DDLCheck

[[Papers/02 DDLCheck|Paper note]] · [[PDFs/DDLCheck_PVLDB2025.pdf|PDF]] · [[Concepts/DDLCheck/00 Concept Map|Concept map]]

Focus:

> Construct the same visible schema through different histories and compare later behavior.

### 3. WriteCheck

[[Papers/03 WriteCheck|Paper note]] · [[PDFs/WriteCheck_PVLDB2025.pdf|PDF]] · [[Concepts/WriteCheck/00 Concept Map|Concept map]]

Focus:

> Observe the real concurrent schedule, infer an FCRFS serial execution, and compare final database states.

## Shared project question

> How can we test a DBMS for wrong answers when we do not know the correct answer in advance?

| Paper | DBMS layer | Equivalence idea |
|---|---|---|
| CODDTest | Query / expression | Original query ≡ folded query |
| DDLCheck | Schema / DDL | Evolved schema ≡ directly constructed schema |
| WriteCheck | Transactions | Concurrent execution ≡ oracle execution/state |

## Recommended CODDTest path

1. [[Concepts/Shared/01 Test Oracle]]
2. [[Concepts/Shared/03 Metamorphic Testing]]
3. [[Concepts/CODDTest/03 Metamorphic Relation]]
4. [[Concepts/CODDTest/04 Constant Folding]]
5. [[Concepts/CODDTest/05 Constant Propagation]]
6. [[Concepts/CODDTest/06 Original Auxiliary and Folded Queries]]
7. [[Concepts/CODDTest/07 Independent and Dependent Expressions]]
8. [[Concepts/CODDTest/17 How CODDTest Fits Together]]

## Recommended DDLCheck path

1. [[Concepts/DDLCheck/01 Database Schema]]
2. [[Concepts/DDLCheck/02 Schema Evolution]]
3. [[Concepts/DDLCheck/04 Schema-Related Information]]
4. [[Concepts/DDLCheck/06 Equivalent Databases]]
5. [[Concepts/DDLCheck/08 Generated and Synthesized DDL Sequences]]
6. [[Concepts/DDLCheck/14 DDLCheck Oracle]]
7. [[Concepts/DDLCheck/10 DDL Sequence Generation]]
8. [[Concepts/DDLCheck/12 DDL Sequence Synthesis]]
9. [[Concepts/DDLCheck/16 Database Schema Transition Graph (DSTG)]]
10. [[Concepts/DDLCheck/24 MySQL 114904 Walkthrough]]
11. [[Concepts/DDLCheck/26 How DDLCheck Fits Together]]


## Recommended WriteCheck path

1. [[Concepts/WriteCheck/01 Transactions and ACID]]
2. [[Concepts/WriteCheck/04 Transaction Schedules]]
3. [[Concepts/WriteCheck/05 Concurrent and Serial Schedules]]
4. [[Concepts/WriteCheck/08 Isolation Levels]]
5. [[Concepts/WriteCheck/10 Write-Write Conflicts]]
6. [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)]]
7. [[Concepts/WriteCheck/12 Transaction-Level and Statement-Level WSS]]
8. [[Concepts/WriteCheck/14 FCRFS Serial Pattern]]
9. [[Concepts/WriteCheck/16 WSS Correctness Assumption]]
10. [[Concepts/WriteCheck/22 Submitted Order vs Actual Schedule]]
11. [[Concepts/WriteCheck/25 Inferring the Serial Oracle]]
12. [[Concepts/WriteCheck/26 Final-State Comparison]]
13. [[Concepts/WriteCheck/32 Project Reproduction - MySQL 104833]]
14. [[Concepts/WriteCheck/34 How WriteCheck Fits Together]]

## Repository resources

Outside the vault:

- reproduction scripts: ../repro/
- captured outputs: ../results/
- presentation materials: ../presentation/
