# Submitted Order vs Actual Schedule

## In one sentence

The **submitted order** is the intended statement interleaving; the **actual schedule** is what really happens after the DBMS blocks, resumes, commits, or aborts transactions.

## Example submitted order

    T1 UPDATE
    T2 UPDATE
    T1 COMMIT
    T2 COMMIT

## Possible actual schedule

    T1 UPDATE
    T2 UPDATE → BLOCKED
    T1 COMMIT
    T2 UPDATE → RESUMES
    T2 COMMIT

The second update appears twice conceptually: first as a blocked attempt, later as the resumed execution.

## Why WriteCheck cares

The serial oracle must be inferred from the **actual concurrent execution**, not merely from the requested submission order.

Otherwise the tester could compare against the wrong completion order.

## What changes actual execution?

- lock waits;
- write-write conflicts;
- deadlocks;
- automatic aborts;
- DBMS-specific error handling.

## Related

- [[23 Transaction Execution Protocol]]
- [[24 Blocking Aborts and Deadlocks]]
- [[25 Inferring the Serial Oracle]]
