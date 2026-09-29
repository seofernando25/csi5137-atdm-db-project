# Bug-Revealing Statements

## In one sentence

A **bug-revealing statement** is the later SQL statement that finally makes a hidden schema inconsistency observable.

## Important distinction

The DDL history can **create** the bug:

    CREATE
      ↓
    ALTER
      ↓
    RENAME
      ↓
    stale internal metadata

but nothing visible may fail yet.

A later statement reveals it:

    INSERT / SELECT / ALTER / ...
             ↓
        observable mismatch

## DDLCheck terminology

DDLCheck first builds db_gen and db_syn.

It then generates SQL statements and executes the same statement on both.

The first statement that causes inconsistent behavior is the bug-revealing statement.

## Our example

In MySQL #114904:

1. renaming the referenced table creates stale foreign-key information;
2. the schema can still appear reasonable;
3. a later INSERT into the referencing table exposes the inconsistency.

See [[24 MySQL 114904 Walkthrough]].

## Why this is useful

It separates:

- **bug-inducing history** from
- **bug-revealing operation**.

That distinction is common in stateful systems.
