---
type: paper
title: Simple Testing Can Expose Most Critical Transaction Bugs
venue: PVLDB
year: 2025
tags: [paper, writecheck, transactions, serializability, dbms-testing]
---

# WriteCheck — Write-Specific Serializability Testing

**PDF:** [[PDFs/WriteCheck_PVLDB2025.pdf]]

## Core idea

A concurrent transaction execution should agree with an appropriate serial/oracle execution on the relevant final database state.

Concurrent execution → final state A  
Serial/oracle execution → final state B  
Expected relation: A = B.

## Our representative case

MySQL #104833 on MySQL 8.0.32.

Our replay uses the exact upstream testcase and Troc's MVCC oracle to expose the same final-state inconsistency.

Concurrent: [10, 1, 10, 20, 10, 20]  
Oracle: [10, 20, 10, 20, 10, 20]

## Next reading questions

- What exactly is write-specific serializability?
- Why does focusing on writes simplify testing?
- How does WriteCheck construct its oracle?
- What bugs are outside its scope?

![[PDFs/WriteCheck_PVLDB2025.pdf]]
