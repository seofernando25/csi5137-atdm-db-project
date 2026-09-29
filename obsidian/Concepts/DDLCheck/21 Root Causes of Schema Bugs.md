# Root Causes of Schema Bugs

## In one sentence

DDLCheck's confirmed failures can originate from different internal subsystems even though schema evolution is what exposes them.

## Root causes identified by the authors

For the confirmed bugs whose cause could be determined, the paper groups them into three categories.

### 1. Incorrect maintenance of database schemas

The DBMS's stored schema definition becomes wrong.

Example idea:

    rename table
        ↓
    INFORMATION_SCHEMA still exposes stale reference

### 2. Incorrect maintenance of schema-related information

The visible schema may look right, but other metadata remains stale or inconsistent.

Examples include:

- stale table statistics;
- stale foreign-key metadata;
- inconsistent index information.

[[24 MySQL 114904 Walkthrough|MySQL #114904]] belongs here.

### 3. Incorrect query optimization

Equivalent schema histories can lead the optimizer to produce behaviorally inconsistent query plans.

## Why this is important

DDLCheck is not merely a "DDL parser tester."

Schema evolution touches:

- catalogs;
- storage;
- constraints;
- statistics;
- optimizers.

A schema-history bug can therefore surface far away from the DDL statement that caused it.

Paper Section 4.3: [[PDFs/DDLCheck_PVLDB2025.pdf#page=10]]
