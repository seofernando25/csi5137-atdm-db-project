# Project Reproduction — MySQL #104833

## In one sentence

Our project reproduces a transaction final-state inconsistency on MySQL 8.0.32 using the upstream **Troc** testcase and Troc's MVCC-based oracle.

## Important attribution

This is **not a rerun of WriteCheck itself**.

The case is relevant to the WriteCheck paper because it demonstrates the same broad problem:

> a concurrent transaction execution can produce a database state inconsistent with an expected oracle state.

But our executable reproduction is powered by Troc.

## Initial table

Three rows:

    (NULL, 1)
    (2,    2)
    (NULL, 3)

## Transactions

T1 at Read Committed:

    BEGIN
    UPDATE t SET a = 10
    COMMIT

T2 at Read Committed:

    BEGIN
    UPDATE t SET b = 20 WHERE a
    COMMIT

## Submitted order

    T1 BEGIN
    T1 UPDATE
    T2 BEGIN
    T2 UPDATE
    T1 COMMIT
    T2 COMMIT

T2's update blocks and later resumes.

## Observed final state

    [10, 1, 10, 20, 10, 20]

## Troc MVCC oracle state

    [10, 20, 10, 20, 10, 20]

The states differ.

## Repository

Case:

    repro/writecheck_104833.case.txt

Runner:

    repro/writecheck_104833.sh

Captured output:

    results/writecheck_104833.txt

## Presentation wording

> "For our class reproduction, we replay a transaction bug from the WriteCheck artifact lineage using Troc's published testcase and MVCC oracle on the same MySQL 8.0.32 baseline."

That is more precise than claiming WriteCheck generated our demonstration.
