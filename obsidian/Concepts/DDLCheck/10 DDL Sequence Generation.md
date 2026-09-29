# DDL Sequence Generation

## In one sentence

DDLCheck randomly generates a **valid evolving schema history** rather than isolated DDL statements.

## Basic flow

Start with an empty schema:

    schema = ∅

Generate an initial CREATE TABLE:

    schema = {t1}

Then repeatedly:

1. choose a DDL operation valid for the current schema;
2. generate the concrete statement;
3. update the in-memory schema model;
4. continue until the chosen sequence length is reached.

## Why DDLCheck does this

The goal is to exercise combinations such as:

    CREATE
      ↓
    ALTER
      ↓
    CREATE INDEX
      ↓
    DROP
      ↓
    RENAME

These histories stress metadata-maintenance paths that a direct CREATE statement never exercises.

## Key idea

The generator is random, but **not stateless**.

See [[11 Stateful and Grammar-Based Generation]].

Paper Algorithm 1: [[PDFs/DDLCheck_PVLDB2025.pdf#page=5]]
