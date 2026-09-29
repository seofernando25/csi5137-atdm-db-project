# Read and Write Operations

## In one sentence

WriteCheck separates operations that **observe data** from operations that **modify data**, because WSS deliberately focuses on the effects of writes.

## Reads

Typical read operation:

    SELECT ...

Reads retrieve values without directly changing the database state.

## Writes

Typical write operations:

    INSERT
    UPDATE
    DELETE
    REPLACE

Writes change stored data.

## Why WriteCheck focuses on writes

The paper's key observation is that concurrent write operations that conflict should normally be blocked or cause an abort.

This gives the authors a simple property for reasoning about final database state.

## Important nuance

WSS does not say reads are unimportant to transaction semantics.

It says the **oracle property being checked focuses on write effects**.

## Related

- [[10 Write-Write Conflicts]]
- [[11 Write-Specific Serializability (WSS)]]
- [[17 Read-Dependent Writes]]
