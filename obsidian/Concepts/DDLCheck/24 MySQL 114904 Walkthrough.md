# MySQL #114904 Walkthrough

## In one sentence

MySQL #114904 shows a table rename updating the **visible foreign-key definition** while stale internal schema-related information still remembers the old table name.

## Complex generated history — seq_gen

Start with parent table t0:

    CREATE TABLE t0 (
      c2 FLOAT8,
      PRIMARY KEY (c2)
    );

Create child table t1:

    CREATE TABLE t1 (
      c1 FLOAT8 UNIQUE,
      FOREIGN KEY (c1)
        REFERENCES t0(c2)
        ON UPDATE CASCADE
    );

Rename t0:

    ALTER TABLE t0 RENAME AS t2,
      ALGORITHM COPY;

## What should now be true?

The parent table is t2.

The foreign key in t1 should reference t2.

And, visibly, SHOW CREATE TABLE t1 does show a reference to t2.

## Reveal the bug

Insert a valid parent row:

    INSERT INTO t2 (c2) VALUES (1);

Then:

    INSERT INTO t1 (c1) VALUES (1);

The insert should satisfy the foreign key.

Instead, MySQL 8.0.32 rejects it.

The error internally refers to the stale old table name t0.

## Direct synthesized construction — seq_syn

Create the same final schema directly:

    CREATE TABLE t2 (...);

    CREATE TABLE t1 (
      ... REFERENCES t2(c2) ...
    );

The same insert succeeds.

## Oracle violation

    visible schema(db_gen)
           =
    visible schema(db_syn)

but:

    INSERT on db_gen
           ≠
    INSERT on db_syn

Therefore the construction history changed behavior when it should not have.

## What concept does it demonstrate?

This is a concrete example of:

- [[04 Schema-Related Information]];
- [[14 DDLCheck Oracle]];
- [[20 Bug-Revealing Statements]];
- [[21 Root Causes of Schema Bugs]].

## Our reproduction

We reproduced the published behavior on **MySQL 8.0.32**.

Repository script:

    repro/ddlcheck_114904.sh

Captured output:

    results/ddlcheck_114904.txt

Paper Listing 4: [[PDFs/DDLCheck_PVLDB2025.pdf#page=10]]
