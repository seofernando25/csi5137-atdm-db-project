# DDL, DML, and DQL

## In one sentence

These labels group SQL statements by whether they define structure, manipulate data, or query data.

## DDL — Data Definition Language

Changes schema:

    CREATE TABLE
    ALTER TABLE
    DROP TABLE
    CREATE INDEX
    CREATE VIEW

DDLCheck uses DDL to create different schema histories.

## DML — Data Manipulation Language

Changes stored data:

    INSERT
    UPDATE
    DELETE
    REPLACE

DDLCheck can run DML on both equivalent databases and compare their resulting states.

## DQL — Data Query Language

Reads data:

    SELECT

DDLCheck can run the same SELECT on both databases and compare query results.

## Why the distinction matters

DDL creates the test setup.

DML and DQL often **reveal** the hidden schema bug later.

## Related

- [[20 Bug-Revealing Statements]]
- [[15 Schema Bug Categories]]
