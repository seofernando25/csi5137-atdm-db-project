---
type: guide
series: ATDM database testing papers
order: 3
paper: WriteCheck
tags: [guide, writecheck, transactions, serializability, dbms-testing]
---

# Understanding WriteCheck

**Paper:** [[Papers/03 WriteCheck|Simple Testing Can Expose Most Critical Transaction Bugs]]

**PDF:** [[PDFs/WriteCheck_PVLDB2025.pdf]]

## 1. The problem: what final state should concurrency produce?

Concurrency makes the test-oracle problem harder.

Suppose two transactions run at the same time.

They both complete successfully.

The database ends in some state.

How does the tester know whether that final state is correct?

A [[Concepts/WriteCheck/07 Critical Transaction Bugs|Critical Transaction Bug]] can silently leave incorrect data after every transaction has committed.

WriteCheck asks whether a serial reference execution can act as the oracle.

But that immediately raises another question:

> Which serial order should represent the concurrent execution?

Much of the paper exists to answer that question.

## 2. Transactions and schedules

A [[Concepts/WriteCheck/01 Transactions and ACID|Transaction]] is a logical unit of work.

An explicit transaction might be:

    BEGIN
    UPDATE ...
    DELETE ...
    COMMIT

The paper also distinguishes [[Concepts/WriteCheck/02 Explicit and Autocommit Transactions|Explicit and Autocommit Transactions]].

Now suppose there are two transactions.

T1:

    BEGIN
    UPDATE A
    COMMIT

T2:

    BEGIN
    UPDATE B
    COMMIT

A [[Concepts/WriteCheck/04 Transaction Schedules|Transaction Schedule]] is the order in which their statements actually execute.

A concurrent schedule can interleave them:

    T1 BEGIN
    T2 BEGIN
    T1 UPDATE A
    T2 UPDATE B
    T1 COMMIT
    T2 COMMIT

A [[Concepts/WriteCheck/05 Concurrent and Serial Schedules|Serial Schedule]] runs one transaction completely before the next.

WriteCheck compares concurrent behavior against a serial reference.

## 3. Why the paper focuses on writes

See [[Concepts/WriteCheck/03 Read and Write Operations|Read and Write Operations]].

Reads retrieve data:

    SELECT

Writes modify data:

    INSERT
    UPDATE
    DELETE
    REPLACE

The paper's key observation is that concurrent writes that conflict should normally require coordination.

For example:

T1:

    UPDATE t SET x = 10 WHERE id = 1;

T2:

    DELETE FROM t WHERE id = 1;

These are [[Concepts/WriteCheck/10 Write-Write Conflicts|Write-Write Conflicts]].

Depending on the DBMS, a conflicting operation may block or cause a transaction to abort.

That gives the authors a useful basis for reasoning about the final database state.

## 4. Write-Specific Serializability

The new property is [[Concepts/WriteCheck/11 Write-Specific Serializability (WSS)|Write-Specific Serializability]], or WSS.

At a high level:

    concurrent schedule H_con
             ↓
       final state A

should agree with:

    corresponding serial schedule H_ser
             ↓
       final state B

Expected:

    A = B

If the states differ, the schedule violates WSS.

The word write-specific is important.

WSS focuses on the effects of writes and the final database state rather than requiring full equivalence of every read and write event.

See [[Concepts/WriteCheck/13 WSS vs Other Serializability Notions|WSS vs Other Serializability Notions]].

That makes it weaker than full conflict serializability and lets the paper apply it beyond only Serializable isolation.

## 5. Isolation levels and concurrency control

WriteCheck operates across [[Concepts/WriteCheck/08 Isolation Levels|Isolation Levels]] such as:

- Read Uncommitted;
- Read Committed;
- Repeatable Read;
- Serializable.

DBMSs also use different [[Concepts/WriteCheck/09 Concurrency Control Modes|Concurrency Control Modes]].

A pessimistic system may block conflicting work immediately.

An optimistic system may allow more work and check for conflicts later.

WriteCheck therefore needs an oracle based on observable transaction behavior rather than one specific internal lock implementation.

## 6. tx-WSS and stmt-WSS

The paper defines two WSS variants.

See [[Concepts/WriteCheck/12 Transaction-Level and Statement-Level WSS|Transaction-Level and Statement-Level WSS]].

### tx-WSS

Transaction-level WSS keeps explicit transactions together.

If T1 contains several SQL statements, those statements remain one transaction in the serial reference.

### stmt-WSS

Statement-level WSS creates a simplified serial schedule.

For committed transactions:

- remove transaction-control statements;
- execute the remaining DQL/DML statements as individual autocommit transactions.

For aborted transactions:

- ignore their statements.

The paper needs both because some bugs are visible only at statement level.

## 7. Why a random serial order is not enough

Suppose T1 and T2 overlap.

Possible serial orders include:

    T1 → T2

and:

    T2 → T1

If the tester simply picks whichever order matches the observed concurrent state, the oracle becomes meaningless.

Almost any final state might match some serial ordering.

WriteCheck therefore needs a justified way to infer the reference order without knowing the correct state in advance.

That leads to FCRFS.

## 8. FCRFS

See [[Concepts/WriteCheck/14 FCRFS Serial Pattern|FCRFS Serial Pattern]].

FCRFS means:

> **First Commit/Rollback First Scheduled.**

If T1 finishes before T2 in the actual concurrent execution, FCRFS puts T1 before T2 in the serial schedule.

Example completion order:

    T2 COMMIT
    T1 COMMIT

Inferred serial order:

    T2 → T1

This is the key step that turns WSS into an automated oracle.

## 9. Happens-before and the correctness intuition

The paper describes ordering using the [[Concepts/WriteCheck/15 Happens-Before Relation|Happens-Before Relation]].

If:

    T1.end happens before T2.end

then FCRFS puts:

    T1 before T2

The proof's intuition is more important than memorizing its notation.

If the DBMS correctly handles conflicting writes, a transaction that already finished should not still have unresolved conflicting work that would invalidate that order.

This depends on a central assumption.

## 10. Assumption 1

See [[Concepts/WriteCheck/16 WSS Correctness Assumption|WSS Correctness Assumption]].

Conceptually:

    conflicting writes
          ↓
    DBMS identifies conflict
          ↓
    block or abort appropriately

Under that assumption, the paper argues that the concurrent execution should produce the same final state as the FCRFS serial execution.

This assumption explains both the strength and the boundary of WriteCheck's oracle.

## 11. Read-dependent writes are restricted

See [[Concepts/WriteCheck/17 Read-Dependent Writes|Read-Dependent Writes]].

WriteCheck avoids application-style patterns such as:

    SELECT x
      ↓
    application computes using x
      ↓
    later UPDATE uses the computed value

Such behavior could produce concurrency problems caused by application logic even if the DBMS transaction mechanism is correct.

The paper wants to test DBMS transaction-processing bugs, so generated writes are restricted accordingly.

A statement such as:

    UPDATE t SET x = x + 1;

is still allowed because the read/modify behavior is contained in one SQL statement.

## 12. Why small tests can work

The authors begin with an empirical study of real critical transaction bugs.

See [[Concepts/WriteCheck/18 Small-Scope Hypothesis|Small-Scope Hypothesis]].

They find that studied WSS violations generally use small test cases:

- no more than five transactions;
- almost all transactions have no more than five statements;
- initial databases are small.

That is good news for automated testing.

The transaction space is enormous, but many serious bugs do not require enormous workloads.

## 13. Deterministic triggering

Concurrency bugs are often associated with nondeterministic timing.

The paper reports that most studied WSS violations can be triggered by submitting statements in a particular order.

See [[Concepts/WriteCheck/19 Deterministic Triggering|Deterministic Triggering]].

This means WriteCheck can often expose the bug without deeply instrumenting the DBMS scheduler.

But the order submitted by the tester is not necessarily the real execution order.

## 14. Submitted order vs actual schedule

This distinction is essential.

Suppose WriteCheck submits:

    T1 UPDATE
    T2 UPDATE
    T1 COMMIT
    T2 COMMIT

The DBMS might actually behave like:

    T1 UPDATE
    T2 UPDATE → BLOCKED
    T1 COMMIT
    T2 UPDATE → RESUMES
    T2 COMMIT

Therefore:

    submitted order ≠ actual schedule

See [[Concepts/WriteCheck/22 Submitted Order vs Actual Schedule|Submitted Order vs Actual Schedule]].

The serial oracle must be derived from what actually happened.

## 15. The transaction execution protocol

WriteCheck implements a [[Concepts/WriteCheck/23 Transaction Execution Protocol|Transaction Execution Protocol]].

It:

1. submits statements according to the chosen order;
2. detects successful execution or blocking;
3. continues other eligible work;
4. detects when blocked statements resume;
5. records commits, rollbacks, and errors;
6. reconstructs the actual concurrent schedule.

The protocol must also handle [[Concepts/WriteCheck/24 Blocking Aborts and Deadlocks|Blocking, Aborts, and Deadlocks]].

A transaction can:

- wait on a lock;
- abort because of a deadlock;
- fail an optimistic conflict check;
- enter an error state requiring rollback.

All of these affect the schedule used by the oracle.

## 16. Inferring the serial oracle

Once the actual schedule is known, WriteCheck constructs the reference execution.

See [[Concepts/WriteCheck/25 Inferring the Serial Oracle|Inferring the Serial Oracle]].

For tx-WSS:

- scan completion events;
- order transactions using FCRFS.

For stmt-WSS:

- start from that transaction order;
- remove aborted transactions;
- remove transaction-control statements;
- replay remaining DQL/DML statements individually.

This is WriteCheck's version of manufacturing the reference execution.

CODDTest manufactures F.

DDLCheck manufactures db_syn.

WriteCheck manufactures H_ser.

## 17. Final-state comparison

Now both executions start from the same initial database.

Actual concurrent execution:

    H_con
      ↓
    state A

Inferred serial execution:

    H_ser
      ↓
    state B

WriteCheck compares:

    state A ?= state B

See [[Concepts/WriteCheck/26 Final-State Comparison|Final-State Comparison]].

A mismatch is a WSS violation.

The method can also observe whether corresponding write operations succeed or fail.

## 18. Why false positives are interesting

Some WSS violations were shown to DBMS developers and considered permissible rather than implementation bugs.

See [[Concepts/WriteCheck/29 Permissible WSS Violations and False Positives|Permissible WSS Violations and False Positives]].

These cases are important because they show that WriteCheck's oracle depends on the assumed write semantics.

Two mechanisms appear prominently.

## 19. Semi-consistent reads

See [[Concepts/WriteCheck/27 Semi-Consistent Reads|Semi-Consistent Reads]].

At some isolation levels, MySQL/MariaDB write processing can inspect a committed version of a locked row to decide whether a WHERE predicate matches.

This can reduce locking.

It can also produce a final state that differs from the FCRFS serial state.

WriteCheck reports the mismatch.

Developers may consider the behavior intentional.

That is a direct example of an oracle assumption meeting DBMS-specific semantics.

## 20. Gap locks

See [[Concepts/WriteCheck/28 Gap Locks|Gap Locks]].

Suppose current data is:

    {3}

T1 executes:

    DELETE FROM t
    WHERE c BETWEEN 1 AND 10;

T2 concurrently inserts:

    5

Value 5 did not exist when T1 began, but it lies inside T1's predicate range.

A gap/range lock can prevent that insert.

Without it, the concurrent final state can differ from the serial oracle.

Different DBMSs and isolation levels make different choices here.

## 21. What the empirical study and evaluation show

See [[Concepts/WriteCheck/30 Evaluation and Findings|Evaluation and Findings]].

From 35 studied critical transaction bugs, the authors found that 32, or 91.4%, had test cases violating WSS.

WriteCheck is evaluated on:

- MySQL 8.0.32;
- PostgreSQL 15.2;
- SQLite 3.36.0;
- MariaDB 10.11.2;
- CockroachDB 22.2.5;
- TiDB 6.6.0.

The paper reports:

- 101 WSS violation instances;
- 22 unique WSS violations;
- 13 confirmed critical transaction bugs;
- 11 confirmed as new critical transaction bugs;
- 9 developer-classified false positives.

The important design conclusion is:

> A simple final-state oracle can expose serious transaction bugs if the serial reference is inferred carefully.

## 22. Comparison with earlier approaches

See [[Concepts/WriteCheck/31 Existing Transaction Verification and Testing Approaches|Existing Transaction Verification and Testing Approaches]].

The paper discusses tools including:

- Elle;
- Cobra;
- Emme;
- DT2;
- Troc;
- TxCheck.

Some verify histories against isolation models.

Some use differential testing.

Some use MVCC or dependency-based oracles.

WriteCheck argues for a simpler reference construction based on actual schedule plus FCRFS.

## 23. Our MySQL #104833 project reproduction

See [[Concepts/WriteCheck/32 Project Reproduction - MySQL 104833|Project Reproduction — MySQL #104833]].

Our observed final state is:

    [10, 1, 10, 20, 10, 20]

The oracle state is:

    [10, 20, 10, 20, 10, 20]

They differ.

Important attribution:

> Our runnable reproduction uses the upstream Troc testcase and Troc's MVCC-based oracle. It is not a direct run of WriteCheck.

The example is still useful because it concretely demonstrates the same broad transaction-testing problem: a concurrent execution can leave a final state inconsistent with a constructed oracle.

## 24. Limits of WriteCheck

See [[Concepts/WriteCheck/33 Limitations and Scope|Limitations and Scope]].

Important limitations include:

- unsupported SQL features;
- random exploration cannot cover every schedule;
- not every critical transaction bug violates WSS;
- an unusual actual schedule can lead to an unhelpful inferred serial oracle;
- final-state comparison does not detect every read anomaly;
- WSS can flag behavior permitted by DBMS-specific write semantics.

That last point is especially important.

The paper does not prove that every WSS mismatch is automatically a product defect under every isolation-level specification.

# What to remember

Remember these six ideas:

1. A schedule is the actual ordering of transaction operations.
2. WSS compares concurrent write effects with a corresponding serial schedule.
3. FCRFS infers the serial order from transaction completion order.
4. Submitted order and actual schedule can differ because of blocking and aborts.
5. WriteCheck replays the inferred serial schedule and compares final states.
6. The oracle depends on assumptions about conflict handling, which explains some false positives.

For the compact synthesis:

[[Concepts/WriteCheck/34 How WriteCheck Fits Together]]

## Previous

[[Guides/02 Understanding DDLCheck|Part 2 — Understanding DDLCheck]]

## Next

[[Guides/04 Three Papers, One Testing Idea|Finale — Three Papers, One Testing Idea]]
