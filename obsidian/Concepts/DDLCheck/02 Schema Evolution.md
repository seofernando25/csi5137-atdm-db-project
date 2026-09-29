# Schema Evolution

## In one sentence

**Schema evolution** is the process of changing a database schema over time.

## Tiny example

    CREATE TABLE t0 (...)
          ↓
    ALTER TABLE t0 ADD COLUMN ...
          ↓
    ALTER TABLE t0 DROP COLUMN ...
          ↓
    RENAME t0 TO t2

The final visible schema might be simple, but the DBMS had to maintain internal information through every transition.

## Why DDLCheck cares

DDLCheck's central hypothesis is that **history can matter when it should not**.

A complex sequence of ALTER, DROP, RENAME, index changes, and constraints may leave stale or inconsistent internal state.

DDLCheck compares that evolved database against one built directly into the same final schema.

## Presentation sentence

> DDLCheck tests whether the path used to reach a schema incorrectly changes future behavior.

## Related

- [[04 Schema-Related Information]]
- [[08 Generated and Synthesized DDL Sequences]]
- [[16 Database Schema Transition Graph (DSTG)]]
