# Transaction Test Cases

## In one sentence

A WriteCheck **transaction test case** contains the initial database, a group of transactions, and an order in which their statements are submitted.

## Main pieces

### Initial database

Tables, constraints, and starting rows.

### Transaction group

Transactions T1, T2, ..., Tn.

### Submitted order

An intended interleaving of statements from those transactions.

## Why this matters

A transaction bug may depend on all three:

- a specific schema;
- specific initial values;
- a specific concurrency pattern.

## Important distinction

The submitted order is not necessarily the order the DBMS actually completes.

Blocking, aborts, deadlocks, and resumption can change the real execution.

See [[22 Submitted Order vs Actual Schedule]].

## Related

- [[18 Small-Scope Hypothesis]]
- [[21 Transaction Groups and Submitted Order]]
- [[23 Transaction Execution Protocol]]
