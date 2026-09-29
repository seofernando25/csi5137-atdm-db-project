---
type: index
course: CSI 5137
course_name: Advanced Topics in Databases and Data Management
tags: [atdm, database-testing, papers]
---

# CSI 5137 — ATDM Paper Notebook

## The three papers

1. [[Papers/01 CODDTest|CODDTest — Constant Optimization Driven Database System Testing]]
   - PDF: [[PDFs/CODDTest_SIGMOD2025.pdf]]
2. [[Papers/02 DDLCheck|DDLCheck — Equivalent Database Construction]]
   - PDF: [[PDFs/DDLCheck_PVLDB2025.pdf]]
3. [[Papers/03 WriteCheck|WriteCheck — Write-Specific Serializability Testing]]
   - PDF: [[PDFs/WriteCheck_PVLDB2025.pdf]]

## Current focus: CODDTest

Start with [[Concepts/CODDTest/00 Concept Map]].

Recommended order:

1. [[Concepts/CODDTest/01 Test Oracle]]
2. [[Concepts/CODDTest/02 Metamorphic Testing]]
3. [[Concepts/CODDTest/03 Metamorphic Relation]]
4. [[Concepts/CODDTest/04 Constant Folding]]
5. [[Concepts/CODDTest/05 Constant Propagation]]
6. [[Concepts/CODDTest/06 Original Auxiliary and Folded Queries]]
7. [[Concepts/CODDTest/07 Independent and Dependent Expressions]]
8. [[Concepts/CODDTest/07A Independent Expressions]]
9. [[Concepts/CODDTest/07B Dependent Expressions]]
10. [[Concepts/CODDTest/08A Predicates]]
11. [[Concepts/CODDTest/08B SQL Three-Valued Logic]]
12. [[Concepts/CODDTest/13 Algorithmic Sketch]]
13. [[Concepts/CODDTest/17 How CODDTest Fits Together]]

## Shared project question

How can we test a DBMS for wrong answers when we do not know the correct answer in advance?

| Paper | Layer | Equivalence used as oracle |
|---|---|---|
| CODDTest | Query / expression | Original query ≡ folded query |
| DDLCheck | Schema / DDL | Evolved schema ≡ directly created schema |
| WriteCheck | Transactions | Concurrent execution ≡ serial/oracle execution |
