# DDL Sequences

## In one sentence

A **DDL sequence** is an ordered history of schema-changing SQL statements.

## Example

    CREATE TABLE t0 (...)
    CREATE INDEX i0 ON t0(...)
    ALTER TABLE t0 ADD COLUMN ...
    ALTER TABLE t0 RENAME t2
    DROP INDEX i0

Order matters because each statement operates on the schema created by the previous statements.

## Why DDLCheck cares

DDLCheck does not merely test isolated ALTER TABLE statements.

It tests **histories**.

A bug may require several earlier schema changes before stale internal information becomes observable.

## Two special sequences

DDLCheck uses:

- seq_gen — a generated, potentially complex history;
- seq_syn — a simpler synthesized construction of the final schema.

See [[08 Generated and Synthesized DDL Sequences]].

## Related

- [[02 Schema Evolution]]
- [[10 DDL Sequence Generation]]
- [[16 Database Schema Transition Graph (DSTG)]]
