# Happens-Before Relation

## In one sentence

A **happens-before relation** records that one event occurred before another within a schedule.

## Notation

The paper writes:

    A ≺_H B

to mean A happens before B in schedule H.

A and B can be:

- statements;
- transaction-ending events;
- transactions.

## Why WriteCheck needs it

FCRFS is defined using completion order.

If:

    T1.end ≺_Hcon T2.end

then FCRFS schedules:

    T1 before T2

in the serial oracle.

## Role in the proof

The paper uses happens-before reasoning to show that, if conflicting writes are correctly blocked or aborted, statements from other transactions can be rearranged around the first completed transaction without changing the final state.

Repeating this transformation leads to the FCRFS serial schedule.

## Presentation advice

Understand the intuition.

You do not need to reproduce the formal proof line by line.

## Related

- [[14 FCRFS Serial Pattern]]
- [[16 WSS Correctness Assumption]]
