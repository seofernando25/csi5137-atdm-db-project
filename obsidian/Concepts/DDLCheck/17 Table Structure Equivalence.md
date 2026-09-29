# Table Structure Equivalence

## In one sentence

DDLCheck considers two table structures equivalent when their columns, constraints, indexes, and foreign keys can be matched consistently, even if names or column order differ.

## Core idea: a bijective mapping

Suppose:

    t1                t2
    --                --
    c1 INT       ↔    c3 INT
    c2 TEXT      ↔    c1 TEXT
    c3 INT       ↔    c2 INT

A one-to-one mapping can show that the structures are equivalent.

## What must match?

Under the mapping:

- column data types;
- column constraints;
- indexes and their columns;
- UNIQUE properties;
- foreign-key relationships.

## Why DDLCheck uses this

The optimization should avoid retesting histories that are structurally equivalent even if incidental names or column ordering differ.

This gives the DSTG comparison more flexibility than literal text comparison.

## Important nuance

This is an **approximation chosen for testing efficiency**.

It is not a universal mathematical definition of relational schema equivalence.

## Related

- [[16 Database Schema Transition Graph (DSTG)]]
- [[18 Interesting DDL Sequences]]

Paper: [[PDFs/DDLCheck_PVLDB2025.pdf#page=7]]
