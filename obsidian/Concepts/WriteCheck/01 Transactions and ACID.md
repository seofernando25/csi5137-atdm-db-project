# Transactions and ACID

## In one sentence

A **transaction** is a unit of database work that should behave as one logical operation.

## Tiny example

    BEGIN
    UPDATE accounts ...
    INSERT INTO audit_log ...
    COMMIT

The statements belong together as one transaction.

## ACID

DBMS transactions are commonly described using four properties:

- **Atomicity** — all-or-nothing effects;
- **Consistency** — database rules remain satisfied;
- **Isolation** — concurrent transactions should not interfere in forbidden ways;
- **Durability** — committed changes survive failures.

## Why WriteCheck cares

WriteCheck targets bugs in **transaction processing mechanisms** that can leave an incorrect database state after concurrent transactions complete.

The paper calls the most serious of these **critical transaction bugs**.

## Important focus

WriteCheck is mainly about **isolation/concurrency behavior**, not durability testing.

## Related

- [[07 Critical Transaction Bugs]]
- [[08 Isolation Levels]]
- [[04 Transaction Schedules]]
