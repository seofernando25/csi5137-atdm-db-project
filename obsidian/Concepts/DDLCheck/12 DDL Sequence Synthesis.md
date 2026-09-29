# DDL Sequence Synthesis

## In one sentence

**DDL sequence synthesis** reconstructs the final schema created by seq_gen using a simpler, more direct sequence seq_syn.

## Example

Complex history:

    CREATE TABLE t0 (...)
    ALTER TABLE t0 ADD ...
    ALTER TABLE t0 RENAME t2
    ALTER TABLE t2 DROP ...

Final structure:

    t2(final columns and constraints)

Synthesized history:

    CREATE TABLE t2(final columns and constraints)

## How DDLCheck does it

1. execute seq_gen;
2. inspect the final schema;
3. generate CREATE TABLE / CREATE VIEW statements;
4. order objects so dependencies are satisfiable;
5. handle foreign keys and circular dependencies specially.

## Why synthesis matters

seq_syn acts as a **clean construction path** for the same visible schema.

The contrast is:

    complex evolution history
          vs
    direct final construction

## Related

- [[13 Schema Introspection and System Catalogs]]
- [[19 Foreign-Key Dependencies and Circularity]]
- [[08 Generated and Synthesized DDL Sequences]]

Paper Section 3.3: [[PDFs/DDLCheck_PVLDB2025.pdf#page=5]]
