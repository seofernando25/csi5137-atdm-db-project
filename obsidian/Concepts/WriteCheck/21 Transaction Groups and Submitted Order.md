# Transaction Groups and Submitted Order

## In one sentence

A **transaction group** is the set of transactions WriteCheck tests together, while the **submitted order** is the planned interleaving in which their statements are sent to the DBMS.

## Transaction group

Example:

    T1 = BEGIN → UPDATE → COMMIT
    T2 = BEGIN → DELETE → COMMIT

Together, T1 and T2 form one transaction group.

WriteCheck requires at least one explicit transaction and at least one transaction containing a write.

## Submitted order

WriteCheck chooses an order that preserves each transaction's internal statement order while interleaving statements across transactions.

Example:

    T1 BEGIN
    T2 BEGIN
    T1 UPDATE
    T2 DELETE
    T1 COMMIT
    T2 COMMIT

## Why randomize it?

Different interleavings exercise different conflicts and blocking behavior.

Enumerating every possible interleaving quickly becomes expensive, so WriteCheck randomly explores them.

## Important distinction

The submitted order is only what WriteCheck **asks the DBMS to execute**.

The real DBMS execution can differ.

See [[22 Submitted Order vs Actual Schedule]].
