# Stateful Test Generation

## In one sentence

**Stateful test generation** generates each new operation using the state created by previous operations.

## Why SQL needs this

This sequence is meaningful:

    CREATE TABLE t1 (...)
    ALTER TABLE t1 ...
    INSERT INTO t1 ...

But generating the ALTER before t1 exists would usually be invalid.

## DDLCheck

DDLCheck dynamically maintains the current schema while producing DDL statements so later operations reference objects that actually exist.

## More general lesson

Database tests often cannot be generated as isolated statements. Earlier statements create:

- tables;
- columns;
- constraints;
- data;
- transactional context;

that later statements depend on.

## Related

- [[08 Grammar-Based Test Generation]]
- [[Concepts/DDLCheck/10 DDL Sequence Generation|DDL Sequence Generation]]
