# Read-Dependent Writes

## In one sentence

WriteCheck restricts generated transactions so a write operation does not depend on a value fetched by an earlier read statement in the same transaction.

## Avoided pattern

    SELECT balance FROM accounts ...
          ↓
    application receives value
          ↓
    UPDATE accounts SET balance = <computed from SELECT>

The later write depends on application-visible data read earlier.

## Why avoid it?

Such behavior can create concurrency problems because of **application transaction logic**, even if the DBMS transaction engine is implemented correctly.

WriteCheck wants to test DBMS transaction-processing bugs, not accidental application-level race conditions.

## What is still allowed?

A statement can read the value it updates internally:

    UPDATE t
    SET c = c + 1;

The read and write are part of one SQL operation.

## Why this matters for WSS

The restriction keeps final-state reasoning focused on DBMS handling of concurrent writes.

## Related

- [[03 Read and Write Operations]]
- [[11 Write-Specific Serializability (WSS)]]
