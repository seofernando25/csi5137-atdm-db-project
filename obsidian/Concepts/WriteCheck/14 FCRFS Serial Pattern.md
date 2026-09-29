# FCRFS Serial Pattern

## In one sentence

**First Commit/Rollback First Scheduled (FCRFS)** orders transactions in the serial oracle according to which transaction finishes first in the actual concurrent execution.

## Rule

If T1 commits or rolls back before T2:

    T1 ends before T2
          ↓
    serial order: T1 → T2

## Tiny example

Actual concurrent completion order:

    T2 COMMIT
    T1 COMMIT

FCRFS serial schedule:

    T2 → T1

## Why this is the key oracle step

WriteCheck does not know the correct final database state in advance.

It needs a principled answer to:

> Which serial schedule should we replay?

The empirical study found that FCRFS inferred the useful serial schedule for all studied WSS violations.

The paper then gives a correctness argument under [[16 WSS Correctness Assumption|Assumption 1]].

## Don't confuse it with

FCRFS is not the original **start order**.

It is based on transaction **completion order**.

## Related

- [[15 Happens-Before Relation]]
- [[25 Inferring the Serial Oracle]]
