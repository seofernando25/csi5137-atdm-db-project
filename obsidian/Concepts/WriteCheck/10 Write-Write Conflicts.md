# Write-Write Conflicts

## In one sentence

A **write-write conflict** occurs when concurrent write operations affect overlapping data in a way that requires coordination.

## Tiny example

T1:

    UPDATE t SET x = 10 WHERE id = 1;

T2:

    DELETE FROM t WHERE id = 1;

Both target the same row.

## Expected DBMS behavior

Depending on the DBMS and concurrency-control mode, the second operation may:

- block;
- cause a transaction to abort;
- be rejected at commit.

The important idea is that conflicting writes should not silently pass through in a way that creates an invalid final state.

## Why WriteCheck cares

The paper's WSS correctness argument assumes that the DBMS can identify relevant write conflicts and process them appropriately.

That assumption is formalized in [[16 WSS Correctness Assumption]].

## Predicate-based conflicts

Conflicts are not always just "same primary key."

A range predicate can conflict with rows that do not yet exist, which is why [[28 Gap Locks|gap locking]] becomes relevant.
