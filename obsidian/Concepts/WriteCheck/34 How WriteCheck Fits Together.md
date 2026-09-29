# How WriteCheck Fits Together

If you understand this page, you understand the core paper.

## Step 1 — Start with the oracle problem

A concurrent execution leaves some final database state.

But how do we know that state is correct?

See [[Concepts/Shared/01 Test Oracle|Test Oracle]].

## Step 2 — Focus on write effects

WriteCheck proposes [[11 Write-Specific Serializability (WSS)|WSS]].

A concurrent schedule should produce the same final database state as a corresponding serial schedule of the same transactions.

## Step 3 — Generate a small transaction test case

Create:

- a small initial database;
- a transaction group;
- an isolation level / concurrency mode;
- a submitted statement order.

The empirical study motivates small tests.

See:

- [[06 Transaction Test Cases]];
- [[18 Small-Scope Hypothesis]].

## Step 4 — Execute concurrently

Submit statements according to the generated order.

But the DBMS can:

- block;
- resume;
- abort;
- deadlock.

So:

    submitted order
          ≠
    actual schedule

See [[22 Submitted Order vs Actual Schedule]].

## Step 5 — Record the actual schedule

WriteCheck's [[23 Transaction Execution Protocol|execution protocol]] reconstructs what really happened.

Call this:

    H_con

## Step 6 — Infer the serial oracle

Use [[14 FCRFS Serial Pattern|FCRFS]].

Transactions that finish first are scheduled first in the serial execution.

Build both:

- tx-WSS serial schedule;
- stmt-WSS simplified serial schedule.

See [[25 Inferring the Serial Oracle]].

## Step 7 — Replay from the same initial state

Run the serial schedule on a fresh copy of the initial database.

Now we have:

    state(H_con)

and:

    state(H_ser)

## Step 8 — Compare final states

Expected:

    state(H_con) = state(H_ser)

If not:

    WSS violation

See [[26 Final-State Comparison]].

## Step 9 — Interpret the mismatch

If [[16 WSS Correctness Assumption|Assumption 1]] holds, the mismatch is strong evidence of a transaction-processing bug.

If the DBMS intentionally uses more permissive semantics, the violation may become a developer-classified false positive.

Examples:

- [[27 Semi-Consistent Reads]];
- [[28 Gap Locks]].

## One-line mental model

    concurrent schedule
            ↓ observe
    actual schedule H_con
            ↓ FCRFS
    serial oracle H_ser
            ↓ replay
    compare final states
            ↓
    mismatch = WSS violation

## Connection to the other papers

### CODDTest

Manufactures an equivalent **query**.

    O ≡ F

### DDLCheck

Manufactures an equivalent **database construction**.

    db_gen ≡ db_syn

### WriteCheck

Manufactures an equivalent **serial execution**.

    H_con ≡ H_ser
    with respect to WSS final state

All three fit [[Concepts/Shared/04 Equivalence-Based Testing|equivalence-based testing]].

## Our project demonstration

[[32 Project Reproduction - MySQL 104833]]

Remember: our executable replay uses Troc's MVCC oracle, not WriteCheck itself.

Return to [[Papers/03 WriteCheck]].
