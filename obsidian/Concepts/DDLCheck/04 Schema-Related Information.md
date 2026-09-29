# Schema-Related Information

## In one sentence

**Schema-related information** is internal DBMS metadata and physical information associated with a schema beyond the user's visible CREATE definitions.

## Visible schema

Users might see:

    TABLE t2
      c2 INT PRIMARY KEY

and a foreign key that points to t2.

## Hidden/internal information may include

- system-catalog entries;
- constraint metadata;
- table statistics;
- physical storage layout;
- hidden columns;
- schema-change history;
- optimizer metadata;
- file/tablespace information.

## Why DDLCheck cares

Two databases can have the same user-visible schema but reach it through different DDL histories.

If one history leaves stale internal metadata, later SQL can behave differently.

That is exactly what happened in [[24 MySQL 114904 Walkthrough|MySQL #114904]]: the visible foreign key referred to t2, while stale internal information still referred to the old table t0.

## Key distinction

    same visible schema
          does NOT guarantee
    same internal schema-related information

DDLCheck deliberately exploits that gap.
