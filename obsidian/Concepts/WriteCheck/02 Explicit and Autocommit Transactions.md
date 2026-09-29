# Explicit and Autocommit Transactions

## In one sentence

WriteCheck distinguishes transactions that explicitly use BEGIN/COMMIT from individual SQL statements that run as their own transactions.

## Explicit transaction

    BEGIN
    UPDATE ...
    DELETE ...
    COMMIT

Several statements belong to one transaction.

## Autocommit transaction

With autocommit enabled, one standalone statement such as:

    UPDATE t SET c = 1;

forms a transaction by itself.

The paper calls this an **ACS transaction** for presentation convenience.

## Why WriteCheck cares

The distinction matters when constructing serial schedules.

Transaction-level WSS preserves explicit transaction boundaries.

Statement-level WSS can treat surviving DML/DQL statements as separate autocommit transactions.

## Related

- [[12 Transaction-Level and Statement-Level WSS]]
- [[21 Transaction Groups and Submitted Order]]
