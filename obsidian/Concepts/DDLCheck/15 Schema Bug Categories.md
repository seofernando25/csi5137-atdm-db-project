# Schema Bug Categories

## In one sentence

DDLCheck classifies observable schema-related failures according to **what becomes inconsistent**.

## 1. Incorrect database schema

The DDL history itself creates an incorrect schema or produces an unexpected error.

Example idea:

    seq_gen says final schema should be S
    DBMS stores / reports something inconsistent with S

## 2. Incorrect database state

A DML statement causes equivalent databases to contain different data.

Example:

    same INSERT
      ↓
    db_gen state ≠ db_syn state

## 3. Incorrect query result

A query returns different results even though the visible schemas and test data should be equivalent.

Example:

    same SELECT
      ↓
    result_gen ≠ result_syn

## Why this matters

The original defect may be in schema handling, but its **manifestation** can appear later as:

- a DDL error;
- corrupted/divergent data;
- a wrong query answer.

## Related

- [[05 Schema-Related Logic Bugs]]
- [[20 Bug-Revealing Statements]]
- [[21 Root Causes of Schema Bugs]]
