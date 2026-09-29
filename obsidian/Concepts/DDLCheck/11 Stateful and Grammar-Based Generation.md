# Stateful and Grammar-Based Generation

## In one sentence

DDLCheck combines syntax rules with knowledge of the current schema so randomly generated SQL is both structurally valid and contextually meaningful.

## Grammar side

A grammar determines what forms are allowed:

    DDL :=
      CREATE
      ALTER
      DROP

DBMS-specific grammar rules cover options and syntax differences.

## State side

The current schema tells the generator what operations make sense.

For example:

    ALTER TABLE t1 ...

requires t1 to already exist.

## Why both are needed

Grammar alone can create syntactically valid but semantically impossible statements.

State alone does not tell us how to construct legal SQL syntax.

Together:

    grammar + current schema
              ↓
       useful random SQL

## Shared concepts

- [[Concepts/Shared/07 Stateful Test Generation|Stateful Test Generation]]
- [[Concepts/Shared/08 Grammar-Based Test Generation|Grammar-Based Test Generation]]

## DDLCheck detail

The paper supports many DDL statement types and DBMS-specific options, including MySQL ALTER algorithms.

Paper: [[PDFs/DDLCheck_PVLDB2025.pdf#page=5]]
