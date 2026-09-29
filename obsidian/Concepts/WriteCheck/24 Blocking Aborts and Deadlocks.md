# Blocking, Aborts, and Deadlocks

## In one sentence

Concurrent transaction testing must account for statements that wait, transactions that abort, and cycles of waiting that form deadlocks.

## Blocking

A write may wait because another transaction currently holds a conflicting lock.

    T2 UPDATE → blocked
    T1 COMMIT
    T2 UPDATE → resumes

## Abort

A DBMS may abort a transaction because of:

- a detected deadlock;
- optimistic write-write conflict;
- an error that invalidates the transaction.

## Deadlock

A deadlock occurs when transactions wait on each other in a cycle.

Conceptually:

    T1 waits for T2
    T2 waits for T1

The DBMS usually resolves this by aborting one transaction.

## Why WriteCheck cares

These events change the actual schedule and therefore change the inferred serial oracle.

Aborted transactions are treated specially in tx-WSS and removed from the simplified stmt-WSS schedule.

## DBMS differences

Different systems report and recover from transaction errors differently, so WriteCheck includes DBMS-specific handling.

## Related

- [[12 Transaction-Level and Statement-Level WSS]]
- [[23 Transaction Execution Protocol]]
