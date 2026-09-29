# Generated and Synthesized DDL Sequences

## In one sentence

DDLCheck compares a **complex generated history** with a **simple synthesized history** that should produce the same final schema.

## seq_gen — generated sequence

Designed to exercise schema evolution:

    CREATE
    ALTER
    DROP
    RENAME
    CREATE INDEX
    ...

It produces db_gen.

## seq_syn — synthesized sequence

Reconstructs the final schema more directly, primarily using CREATE statements:

    CREATE TABLE final_structure ...
    CREATE VIEW ...
    ...

It produces db_syn.

## Expected relation

    schema(db_gen) = schema(db_syn)

but:

    history(db_gen) ≠ history(db_syn)

## Why this is clever

The final visible schema gives DDLCheck a way to manufacture an equivalent control database.

The direct construction acts like a clean reference against the database that experienced a complicated evolution history.

## Related

- [[12 DDL Sequence Synthesis]]
- [[14 DDLCheck Oracle]]
- [[06 Equivalent Databases]]
