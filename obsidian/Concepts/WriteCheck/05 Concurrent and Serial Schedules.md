# Concurrent and Serial Schedules

## In one sentence

A **concurrent schedule** interleaves transactions, while a **serial schedule** runs one transaction completely before the next.

## Concurrent

    T1: BEGIN
    T2: BEGIN
    T1: UPDATE
    T2: UPDATE
    T1: COMMIT
    T2: COMMIT

## Serial

    T1: BEGIN
    T1: UPDATE
    T1: COMMIT
    T2: BEGIN
    T2: UPDATE
    T2: COMMIT

No overlap occurs.

## Why WriteCheck compares them

WriteCheck's core oracle expects the concurrent write effects to match a particular serial ordering inferred from the actual concurrent schedule.

The hard part is not generating a serial order.

The hard part is deciding **which serial order is the correct oracle**.

That leads to [[14 FCRFS Serial Pattern|FCRFS]].

## Related

- [[11 Write-Specific Serializability (WSS)]]
- [[25 Inferring the Serial Oracle]]
