# Database Schema Transition Graph (DSTG)

## In one sentence

A **Database Schema Transition Graph**, or DSTG, represents how table structures change throughout a DDL sequence.

## Mental model

Instead of remembering only:

    CREATE → ALTER → ALTER

record the states:

    table structure S0
            │ CREATE
            ▼
    table structure S1
            │ ALTER
            ▼
    table structure S2

## Graph pieces

The paper models a DSTG using:

- nodes: table structures at points in the history;
- relationships/edges: DDL statements that transform one structure into another;
- mappings connecting each edge to its incoming and outgoing nodes.

## Why DDLCheck needs it

Random generation can repeatedly produce histories that are syntactically different but structurally very similar.

The DSTG gives DDLCheck a representation of **schema-evolution history**, so it can decide whether a new sequence is interesting enough to test.

## Don't confuse it with

The DSTG is **not** the user-visible database schema.

It is a testing representation of the *history of structural changes*.

## Related

- [[18 Interesting DDL Sequences]]
- [[17 Table Structure Equivalence]]
- [[02 Schema Evolution]]

Paper Section 3.5: [[PDFs/DDLCheck_PVLDB2025.pdf#page=6]]
