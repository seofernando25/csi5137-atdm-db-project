# Critical Transaction Bugs

## In one sentence

A **critical transaction bug** is a DBMS implementation bug that causes concurrent transactions to leave an incorrect database state.

## Why the paper uses "critical"

Many transaction bugs can cause:

- incorrect results;
- unexpected errors;
- performance degradation.

WriteCheck focuses on bugs that corrupt the resulting database state after the involved transactions complete.

## Example shape

Expected final state:

    {1, 2, 3}

Actual final state:

    {1, 3}

No crash is required.

## Why these bugs are hard to detect

The DBMS may accept every SQL statement normally.

The error only becomes visible when the final state is compared against a valid oracle.

## Empirical motivation

The authors studied 35 real-world critical transaction bugs and found that 32 of them had test cases violating WSS.

## Related

- [[Concepts/Shared/02 Logic Bugs|Logic Bugs]]
- [[11 Write-Specific Serializability (WSS)]]
- [[30 Evaluation and Findings]]
