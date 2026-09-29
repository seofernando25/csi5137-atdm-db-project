# Gap Locks

## In one sentence

A **gap lock** protects a range between index records so another transaction cannot insert a new row into that protected range.

## Tiny example

Current table:

    {3}

T1 executes:

    DELETE FROM t
    WHERE c BETWEEN 1 AND 10;

T2 tries:

    INSERT INTO t VALUES (5);

The value 5 did not exist when T1 started, but it lies inside T1's predicate range.

## With a suitable gap/range lock

T2's insert can be blocked because 5 falls in the protected range.

## Without it

T2 may insert 5 concurrently.

That can lead to a final state that differs from the WSS serial oracle.

## Why WriteCheck cares

The paper identifies absence of gap locking as another major source of permissible WSS violations.

Different DBMSs and isolation levels use range/gap locking differently.

## Related

- [[10 Write-Write Conflicts]]
- [[16 WSS Correctness Assumption]]
- [[29 Permissible WSS Violations and False Positives]]
