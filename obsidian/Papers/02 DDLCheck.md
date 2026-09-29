---
type: paper
title: Detecting Schema-Related Logic Bugs in Relational DBMSs via Equivalent Database Construction
venue: PVLDB
year: 2025
tags: [paper, ddlcheck, schema, dbms-testing]
---

# DDLCheck — Equivalent Database Construction

**PDF:** [[PDFs/DDLCheck_PVLDB2025.pdf]]

## Core idea

Two databases can reach an equivalent final schema through different DDL histories. If the final schemas are semantically equivalent, later operations should behave equivalently.

CREATE → ALTER → RENAME

should behave like:

direct CREATE of the final schema.

A mismatch can reveal stale internal schema state.

## Our representative case

MySQL #114904 on MySQL 8.0.32:

- visible foreign-key metadata references renamed table t2;
- an insert fails;
- the error still references stale table t0;
- the directly created equivalent schema succeeds.

## Next reading questions

- How does DDLCheck define schema equivalence?
- Which DDL operations are generated?
- What bug categories are targeted?
- How are failures reduced?
- What is outside DDLCheck's oracle?

![[PDFs/DDLCheck_PVLDB2025.pdf]]
