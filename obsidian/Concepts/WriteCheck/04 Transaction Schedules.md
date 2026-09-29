# Transaction Schedules

## In one sentence

A **transaction schedule** is the order in which statements from one or more transactions actually execute.

## Example transactions

T1:

    BEGIN
    UPDATE A
    COMMIT

T2:

    BEGIN
    UPDATE B
    COMMIT

## One possible schedule

    T1 BEGIN
    T2 BEGIN
    T1 UPDATE A
    T2 UPDATE B
    T1 COMMIT
    T2 COMMIT

The operations are interleaved.

## Why schedules matter

Two transactions can contain exactly the same SQL but produce different behavior depending on the interleaving.

WriteCheck therefore tests **transaction schedules**, not merely sets of transactions.

## Paper notation

The concurrent schedule is written as:

    H_con

A corresponding serial schedule is written as:

    H_ser

## Related

- [[05 Concurrent and Serial Schedules]]
- [[22 Submitted Order vs Actual Schedule]]
- [[14 FCRFS Serial Pattern]]
