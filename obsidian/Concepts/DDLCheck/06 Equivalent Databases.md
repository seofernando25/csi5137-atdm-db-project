# Equivalent Databases

## In one sentence

DDLCheck calls two databases **equivalent** when they have the same user-visible database schema for the purpose of the oracle.

## Important point

Equivalent does **not** mean:

- same DDL history;
- same physical layout;
- identical hidden metadata.

Those differences are exactly what DDLCheck wants to stress.

## Mental model

    db_gen                     db_syn
    ------                     ------
    TABLE t2                   TABLE t2
      c2 INT PK                  c2 INT PK
    TABLE t1                   TABLE t1
      FK → t2                    FK → t2

       same visible schema
               ↓
          should behave
          equivalently

## Why DDLCheck cares

If the same later SQL statement behaves differently on equivalent databases, the DDL history has leaked into observable semantics.

That mismatch becomes a bug candidate.

## Related

- [[14 DDLCheck Oracle]]
- [[08 Generated and Synthesized DDL Sequences]]
- [[17 Table Structure Equivalence]]
