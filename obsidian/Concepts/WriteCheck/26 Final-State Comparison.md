# Final-State Comparison

## In one sentence

WriteCheck detects a WSS violation by comparing the final database state of the actual concurrent execution with the final state produced by the inferred serial oracle.

## Process

Start from the same initial database.

Run:

    actual concurrent schedule H_con
             ↓
       final state A

Separately run:

    inferred serial schedule H_ser
             ↓
       final state B

Compare:

    A ?= B

## What else is observed?

WriteCheck also records whether corresponding write operations succeed or fail.

A success/error mismatch can imply that the resulting database states are inconsistent.

## Bug condition

    final state A ≠ final state B

indicates a WSS violation.

## Why final state is attractive

It is simple and DBMS-independent:

- read all table contents;
- compare the states.

The tester does not need to understand every internal locking decision.

## Limitation

Two different executions can sometimes end in the same final state even if another observable behavior is wrong.

See [[33 Limitations and Scope]].

## Related

- [[11 Write-Specific Serializability (WSS)]]
- [[25 Inferring the Serial Oracle]]
