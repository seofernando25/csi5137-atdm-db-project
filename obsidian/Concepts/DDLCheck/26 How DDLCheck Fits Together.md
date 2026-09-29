# How DDLCheck Fits Together

If you understand this page, you understand the core paper.

## Step 1 — Start with the oracle problem

We cannot know the correct behavior of every randomly generated database workload in advance.

See [[Concepts/Shared/01 Test Oracle|Test Oracle]].

## Step 2 — Focus on schema history

A DBMS maintains much more than the visible CREATE definition.

See:

- [[02 Schema Evolution]];
- [[04 Schema-Related Information]].

## Step 3 — Generate a complex history

DDLCheck creates seq_gen through stateful random DDL generation.

    empty schema
       ↓
    CREATE
       ↓
    ALTER / DROP / INDEX / RENAME ...
       ↓
    db_gen

See [[10 DDL Sequence Generation]].

## Step 4 — Inspect the final schema

DDLCheck reads the resulting schema from DBMS system catalogs.

See [[13 Schema Introspection and System Catalogs]].

## Step 5 — Synthesize the control database

Construct seq_syn that creates the same visible schema more directly.

    final schema
       ↓
    CREATE statements
       ↓
    db_syn

See [[12 DDL Sequence Synthesis]].

## Step 6 — Establish equivalence

    schema(db_gen) = schema(db_syn)

The histories differ, but the visible schemas should be equivalent.

See [[06 Equivalent Databases]].

## Step 7 — Execute the same SQL

Generate later SQL statement q.

    db_gen ── q ──→ behavior A
    db_syn ── q ──→ behavior B

Compare:

- errors;
- query results;
- resulting data state.

See [[14 DDLCheck Oracle]].

## Step 8 — Report a mismatch

    behavior A ≠ behavior B

means the schema history has affected observable semantics.

That is a schema-related bug candidate.

## Step 9 — Avoid wasting the test budget

Represent each history as a [[16 Database Schema Transition Graph (DSTG)|DSTG]].

Skip histories that are structurally too similar to ones already tested.

See [[18 Interesting DDL Sequences]].

## Step 10 — Reduce the case

When a mismatch is found, simplify it into a developer-friendly report.

See [[22 Bug Report Reduction]].

## One-line mental model

    evolve schema one way
            ≡
    construct same schema directly
            ↓
       run same SQL
            ↓
        compare behavior

## Connection to CODDTest

CODDTest:

    same query meaning
    different expression representation

DDLCheck:

    same final schema
    different construction history

Both are examples of [[Concepts/Shared/04 Equivalence-Based Testing|equivalence-based testing]].

## Concrete example

[[24 MySQL 114904 Walkthrough]]

Return to [[Papers/02 DDLCheck]].
