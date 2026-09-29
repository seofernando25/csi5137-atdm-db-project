# Schema-Related Logic Bugs

## In one sentence

A **schema-related logic bug** is incorrect DBMS behavior caused by faulty maintenance or use of schema information.

## Examples

A DBMS might:

- fail to update a foreign key after a table rename;
- retain metadata for a dropped column;
- use stale table statistics;
- produce different SELECT results depending on schema history;
- reject a valid INSERT because hidden metadata is wrong.

## Why these bugs are difficult

The visible schema may look correct.

The bug may appear only later when another SQL statement uses stale or inconsistent internal information.

## DDLCheck's strategy

Create two databases with equivalent visible schemas but different construction histories.

Then compare their behavior.

## Related

- [[Concepts/Shared/02 Logic Bugs|Logic Bugs]]
- [[04 Schema-Related Information]]
- [[21 Root Causes of Schema Bugs]]
