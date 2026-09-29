# Transaction Execution Protocol

## In one sentence

WriteCheck's **transaction execution protocol** drives statements according to the submitted order while recording blocking, resumption, errors, and transaction outcomes to reconstruct the actual schedule.

## Why a protocol is needed

Normal sequential execution is not enough for concurrency testing.

A submitted statement can block while another transaction must continue.

WriteCheck therefore executes statements independently and observes their execution state.

## Simplified behavior

For each next statement:

1. submit it;
2. determine whether it succeeds, blocks, or causes an abort;
3. if blocked, continue with other eligible statements;
4. when a blocking transaction completes, detect resumed statements;
5. record the final actual order.

## Why this is general

The protocol is designed around observable DBMS behavior rather than a single engine's internal lock implementation.

DBMS-specific handling is still required for abort/error semantics.

## Related

- [[22 Submitted Order vs Actual Schedule]]
- [[24 Blocking Aborts and Deadlocks]]
- [[20 WriteCheck Architecture]]

Paper Algorithm 1: [[PDFs/WriteCheck_PVLDB2025.pdf#page=8]]
