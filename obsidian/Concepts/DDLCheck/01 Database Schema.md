# Database Schema

## In one sentence

A **database schema** describes the logical structure of a database.

## Typical schema objects

A relational schema can contain:

- tables;
- columns;
- data types;
- indexes;
- primary keys;
- UNIQUE constraints;
- foreign keys;
- views.

## Tiny example

    users(
      id INT PRIMARY KEY,
      email TEXT UNIQUE
    )

The rows stored inside users are data.

The definition of users is schema.

## Why DDLCheck cares

DDLCheck creates the **same final visible schema in two different ways**.

If both databases expose equivalent schemas, later SQL operations should behave equivalently even if their construction histories were different.

## Don't confuse it with

[[Concepts/Shared/05 Database State|Database state]] includes stored data at a point in time.

A schema describes the database's structure.

## Related

- [[02 Schema Evolution]]
- [[04 Schema-Related Information]]
- [[06 Equivalent Databases]]
