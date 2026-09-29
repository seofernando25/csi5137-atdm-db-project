# Schema Introspection and System Catalogs

## In one sentence

**Schema introspection** means asking the DBMS what schema objects currently exist so DDLCheck can reconstruct the final database definition.

## Why DDLCheck needs it

After executing seq_gen, DDLCheck must know the resulting schema before it can synthesize seq_syn.

It cannot simply infer everything from the SQL text because the DBMS is the system under test and may normalize or represent definitions differently.

## Examples of metadata sources

The paper uses DBMS-specific catalog facilities such as:

- MySQL / MariaDB / TiDB / CockroachDB: INFORMATION_SCHEMA;
- SQLite: sqlite_schema;
- PostgreSQL: system catalogs such as pg_index and pg_constraint.

## Important distinction

A system catalog is itself **schema-related information**.

That means bugs can affect both:

1. the metadata DDLCheck reads;
2. later DBMS behavior that consumes related metadata.

## Related

- [[04 Schema-Related Information]]
- [[12 DDL Sequence Synthesis]]
- [[24 MySQL 114904 Walkthrough]]
