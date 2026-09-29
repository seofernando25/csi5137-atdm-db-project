# WriteCheck Concept Map

## Core chain

Initial database
↓
Generate transactions
↓
Choose submitted statement order
↓
Execute concurrently
↓
Observe actual concurrent schedule H_con
↓
Infer FCRFS serial schedule H_ser
↓
Replay H_ser on the same initial database
↓
Compare final database states
↓
Mismatch = WSS violation

## Foundations

- [[01 Transactions and ACID]]
- [[02 Explicit and Autocommit Transactions]]
- [[03 Read and Write Operations]]
- [[04 Transaction Schedules]]
- [[05 Concurrent and Serial Schedules]]
- [[06 Transaction Test Cases]]
- [[07 Critical Transaction Bugs]]
- [[08 Isolation Levels]]
- [[09 Concurrency Control Modes]]
- [[10 Write-Write Conflicts]]

## Main new property

- [[11 Write-Specific Serializability (WSS)]]
- [[12 Transaction-Level and Statement-Level WSS]]
- [[13 WSS vs Other Serializability Notions]]
- [[14 FCRFS Serial Pattern]]
- [[15 Happens-Before Relation]]
- [[16 WSS Correctness Assumption]]
- [[17 Read-Dependent Writes]]

## Why simple tests work

- [[18 Small-Scope Hypothesis]]
- [[19 Deterministic Triggering]]

## WriteCheck workflow

- [[20 WriteCheck Architecture]]
- [[21 Transaction Groups and Submitted Order]]
- [[22 Submitted Order vs Actual Schedule]]
- [[23 Transaction Execution Protocol]]
- [[24 Blocking Aborts and Deadlocks]]
- [[25 Inferring the Serial Oracle]]
- [[26 Final-State Comparison]]

## Oracle boundary / false positives

- [[27 Semi-Consistent Reads]]
- [[28 Gap Locks]]
- [[29 Permissible WSS Violations and False Positives]]

## Results and comparisons

- [[30 Evaluation and Findings]]
- [[31 Existing Transaction Verification and Testing Approaches]]
- [[32 Project Reproduction - MySQL 104833]]
- [[33 Limitations and Scope]]
- [[34 How WriteCheck Fits Together]]

## Shared concepts

- [[Concepts/Shared/01 Test Oracle|Test Oracle]]
- [[Concepts/Shared/02 Logic Bugs|Logic Bugs]]
- [[Concepts/Shared/04 Equivalence-Based Testing|Equivalence-Based Testing]]
- [[Concepts/Shared/05 Database State|Database State]]
- [[Concepts/Shared/09 Test Case Reduction|Test Case Reduction]]
- [[Concepts/Shared/11 SQLancer|SQLancer]]
