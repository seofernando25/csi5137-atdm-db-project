# Concurrency Control Modes

## In one sentence

A **concurrency control mechanism** determines how a DBMS coordinates overlapping transactions.

## Two broad styles discussed in the paper

### Pessimistic

The DBMS prevents conflicting operations from proceeding simultaneously, often using locks.

A statement may block until another transaction commits or aborts.

### Optimistic

Transactions proceed more freely, and conflicts may be checked later, often at commit time.

A transaction may then be aborted if a conflict is detected.

## Why WriteCheck cares

The same transaction test framework needs to handle both styles.

WriteCheck therefore tracks:

- blocked statements;
- resumed statements;
- transaction aborts;
- commit/rollback outcomes.

## Important point

The WSS oracle is intended to be general across concurrency-control modes, but the actual execution protocol must adapt to DBMS behavior.

## Related

- [[10 Write-Write Conflicts]]
- [[23 Transaction Execution Protocol]]
- [[24 Blocking Aborts and Deadlocks]]
