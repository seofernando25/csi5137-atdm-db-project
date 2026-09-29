# DDLCheck Concept Map

## Core chain

Database schema
↓
Schema evolution
↓
Complex DDL history seq_gen
↓
Direct synthesized history seq_syn
↓
Equivalent visible schemas
↓
Run the same SQL on both databases
↓
Compare results / state / errors
↓
Mismatch = schema-related bug

## Foundations

- [[01 Database Schema]]
- [[02 Schema Evolution]]
- [[03 DDL DML and DQL]]
- [[04 Schema-Related Information]]
- [[05 Schema-Related Logic Bugs]]
- [[Concepts/Shared/01 Test Oracle|Test Oracle]]
- [[Concepts/Shared/04 Equivalence-Based Testing|Equivalence-Based Testing]]

## Core oracle

- [[06 Equivalent Databases]]
- [[07 DDL Sequences]]
- [[08 Generated and Synthesized DDL Sequences]]
- [[09 DDLCheck Architecture]]
- [[14 DDLCheck Oracle]]

## Constructing the two databases

- [[10 DDL Sequence Generation]]
- [[11 Stateful and Grammar-Based Generation]]
- [[12 DDL Sequence Synthesis]]
- [[13 Schema Introspection and System Catalogs]]
- [[19 Foreign-Key Dependencies and Circularity]]

## Testing more useful histories

- [[16 Database Schema Transition Graph (DSTG)]]
- [[17 Table Structure Equivalence]]
- [[18 Interesting DDL Sequences]]

## Understanding failures

- [[15 Schema Bug Categories]]
- [[20 Bug-Revealing Statements]]
- [[21 Root Causes of Schema Bugs]]
- [[22 Bug Report Reduction]]
- [[24 MySQL 114904 Walkthrough]]

## Evaluation and limitations

- [[23 Evaluation and Findings]]
- [[25 Limitations and Scope]]

## Synthesis

- [[26 How DDLCheck Fits Together]]
- [[Papers/02 DDLCheck]]
