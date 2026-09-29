# DDLCheck Oracle

## In one sentence

DDLCheck's oracle says that **equivalent databases created through different schema histories should behave the same when given the same later SQL**.

## Setup

    execute seq_gen → db_gen
    execute seq_syn → db_syn

Expected:

    schema(db_gen) = schema(db_syn)

## Test

Generate statement q and execute it on both databases:

    execute(db_gen, q)
           ?=
    execute(db_syn, q)

## What is compared?

Depending on q, DDLCheck compares:

- returned errors;
- SELECT results;
- resulting table contents / database state.

## Bug condition

If equivalent databases disagree:

    behavior(db_gen, q)
        ≠
    behavior(db_syn, q)

DDLCheck reports a schema-related bug candidate.

## Connection to the project theme

This is [[Concepts/Shared/04 Equivalence-Based Testing|equivalence-based testing]] at the **schema-history level**.

CODDTest changes an expression.

DDLCheck changes the path used to construct the database.

## Related

- [[06 Equivalent Databases]]
- [[15 Schema Bug Categories]]
- [[20 Bug-Revealing Statements]]
