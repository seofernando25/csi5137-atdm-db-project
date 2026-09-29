---
type: guide
series: ATDM database testing papers
order: 2
paper: DDLCheck
tags: [guide, ddlcheck, schema-evolution, dbms-testing]
---

# Understanding DDLCheck

**Paper:** [[Papers/02 DDLCheck|Detecting Schema-Related Logic Bugs in Relational DBMSs via Equivalent Database Construction]]

**PDF:** [[PDFs/DDLCheck_PVLDB2025.pdf]]

## 1. The problem: schema history can matter when it should not

A relational DBMS stores more than rows. It also maintains a [[Concepts/DDLCheck/01 Database Schema|Database Schema]] containing tables, columns, data types, indexes, keys, foreign keys, constraints, and views.

Real applications change those structures over time.

For example:

    CREATE TABLE t0 (...)
          ↓
    ALTER TABLE t0 ADD COLUMN ...
          ↓
    ALTER TABLE t0 DROP COLUMN ...
          ↓
    ALTER TABLE t0 RENAME t2

That is [[Concepts/DDLCheck/02 Schema Evolution|Schema Evolution]].

The final schema may look simple, but the DBMS had to update many internal structures along the way.

DDLCheck asks:

> Can two databases expose the same final schema but behave differently because one reached that schema through a complicated history?

## 2. Visible schema vs schema-related information

The paper distinguishes what users can see from the additional metadata the DBMS maintains internally.

See [[Concepts/DDLCheck/04 Schema-Related Information|Schema-Related Information]].

Visible schema can include:

    TABLE t2
      c2 INT PRIMARY KEY

and:

    FOREIGN KEY (...) REFERENCES t2(...)

But internally the DBMS may also maintain:

- system catalog entries;
- foreign-key metadata;
- hidden columns;
- table statistics;
- physical storage information;
- optimizer metadata;
- schema-change history.

A bug may leave those internal structures stale while the visible schema appears correct.

That creates [[Concepts/DDLCheck/05 Schema-Related Logic Bugs|Schema-Related Logic Bugs]].

The defect may be created by one DDL statement and revealed much later by a different operation.

## 3. DDL, DML, and DQL play different roles

See [[Concepts/DDLCheck/03 DDL DML and DQL|DDL, DML, and DQL]].

### DDL

Changes structure:

    CREATE
    ALTER
    DROP
    CREATE INDEX
    CREATE VIEW

DDL creates the schema history under test.

### DML

Changes data:

    INSERT
    UPDATE
    DELETE
    REPLACE

DML can reveal that equivalent schemas evolve into different database states.

### DQL

Reads data:

    SELECT

DQL can reveal inconsistent query results.

The important idea is:

> DDL may create the hidden inconsistency, while DML or DQL reveals it later.

## 4. The two database constructions

DDLCheck creates two databases from different histories.

See [[Concepts/DDLCheck/08 Generated and Synthesized DDL Sequences|Generated and Synthesized DDL Sequences]].

### seq_gen

The generated sequence deliberately exercises schema evolution:

    CREATE
    ALTER
    DROP
    RENAME
    CREATE INDEX
    ...

Executing it creates:

    db_gen

### seq_syn

After seq_gen finishes, DDLCheck inspects the final schema and synthesizes a simpler path:

    CREATE TABLE final_structure ...
    CREATE VIEW ...
    necessary ALTER for dependencies

Executing it creates:

    db_syn

The intended relation is:

    schema(db_gen) = schema(db_syn)

while:

    history(db_gen) ≠ history(db_syn)

These are [[Concepts/DDLCheck/06 Equivalent Databases|Equivalent Databases]] for DDLCheck's purpose.

## 5. Why the synthesized database is useful

Suppose an ALTER or RENAME path leaves stale metadata.

The evolved database contains that hidden state:

    complex history
          ↓
       db_gen

The direct construction avoids that path:

    final schema
          ↓
       db_syn

Both should represent the same visible schema.

Therefore any later behavioral difference is suspicious.

This is the paper's version of [[Concepts/Shared/04 Equivalence-Based Testing|Equivalence-Based Testing]].

## 6. The DDLCheck oracle

See [[Concepts/DDLCheck/14 DDLCheck Oracle|DDLCheck Oracle]].

Once both databases exist, DDLCheck generates later SQL q.

Then:

    execute(db_gen, q)
          ?=
    execute(db_syn, q)

Depending on q, DDLCheck compares:

- errors;
- SELECT results;
- resulting table contents;
- database state.

Expected:

    behavior(db_gen, q)
          =
    behavior(db_syn, q)

A mismatch is a schema-related bug candidate.

Notice the connection to CODDTest:

    CODDTest:
    result(O) = result(F)

    DDLCheck:
    behavior(db_gen, q) = behavior(db_syn, q)

The shared structure is the same, but the object being transformed is larger.

## 7. How DDLCheck generates valid histories

Random DDL generation has to be stateful.

This is invalid if t1 does not exist:

    ALTER TABLE t1 ...

So DDLCheck maintains an internal schema model.

Conceptually:

    empty schema
        ↓
    CREATE t1
        ↓
    schema contains t1
        ↓
    generate operation valid for t1
        ↓
    update schema model
        ↓
    repeat

See [[Concepts/DDLCheck/10 DDL Sequence Generation|DDL Sequence Generation]] and [[Concepts/Shared/07 Stateful Test Generation|Stateful Test Generation]].

DDLCheck also uses [[Concepts/Shared/08 Grammar-Based Test Generation|Grammar-Based Test Generation]] to handle DBMS-specific syntax and options.

Grammar plus current schema state gives the generator useful random DDL rather than arbitrary invalid statements.

## 8. How DDLCheck reconstructs the final schema

After seq_gen executes, DDLCheck needs to learn what schema actually exists.

See [[Concepts/DDLCheck/13 Schema Introspection and System Catalogs|Schema Introspection and System Catalogs]].

Different DBMSs expose metadata through facilities such as:

- INFORMATION_SCHEMA;
- sqlite_schema;
- PostgreSQL system catalogs.

DDLCheck reads those definitions and constructs a simpler direct schema.

That process is [[Concepts/DDLCheck/12 DDL Sequence Synthesis|DDL Sequence Synthesis]].

## 9. Foreign-key dependencies make synthesis harder

Suppose:

    orders.customer_id
      REFERENCES customers.id

Then customers normally needs to exist before the foreign-key relationship can be established.

Synthesis therefore needs dependency ordering.

Circular dependencies are harder:

    A → B
    ↑   ↓
    └───┘

DDLCheck can create the tables first and add some foreign keys afterward.

See [[Concepts/DDLCheck/19 Foreign-Key Dependencies and Circularity|Foreign-Key Dependencies and Circularity]].

This concept matters directly to our MySQL reproduction because #114904 involves a foreign key and table rename.

## 10. Too many possible histories

Schema-evolution testing has a huge input space.

Random generation may repeatedly produce histories that look different as SQL text but exercise similar structural transitions.

That wastes time and creates duplicates.

DDLCheck therefore introduces a testing-efficiency representation called the [[Concepts/DDLCheck/16 Database Schema Transition Graph (DSTG)|Database Schema Transition Graph]], or DSTG.

Conceptually:

    structure S0
       │ CREATE
       ▼
    structure S1
       │ ALTER
       ▼
    structure S2

Nodes represent table structures.

Edges represent DDL transformations.

The graph captures **how the schema evolved**, not merely its final form.

## 11. Table structure equivalence

To compare DSTGs, literal SQL text is too strict.

Two tables can be structurally equivalent even when names or column order differ.

See [[Concepts/DDLCheck/17 Table Structure Equivalence|Table Structure Equivalence]].

DDLCheck uses a one-to-one mapping between corresponding columns and checks properties such as:

- data types;
- constraints;
- indexes;
- UNIQUE properties;
- foreign-key relationships.

This lets it identify histories that are structurally similar.

## 12. Interesting DDL sequences

The DSTG is used to choose [[Concepts/DDLCheck/18 Interesting DDL Sequences|Interesting DDL Sequences]].

The optimization is:

    generate seq_gen
          ↓
    translate to DSTG
          ↓
    similar DSTG already tested?
       /                  \
     yes                  no
      ↓                    ↓
    skip                 test

This is not the correctness oracle.

It is a way to spend the test budget on more diverse histories.

## 13. How schema bugs appear

See [[Concepts/DDLCheck/15 Schema Bug Categories|Schema Bug Categories]].

DDLCheck describes several observable failure forms.

### Incorrect database schema

The DDL process creates or reports the wrong schema.

### Incorrect database state

The same DML operation causes db_gen and db_syn to contain different data.

### Incorrect query result

The same query returns different answers.

This demonstrates an important idea:

> A schema-evolution defect can later look like a data bug or query bug.

## 14. Bug-inducing history vs bug-revealing statement

The history may silently create the defect:

    CREATE
      ↓
    ALTER
      ↓
    RENAME
      ↓
    stale internal metadata

Nothing visible may fail yet.

A later statement finally exposes it:

    INSERT / SELECT / ALTER / ...
              ↓
         visible mismatch

That later statement is the [[Concepts/DDLCheck/20 Bug-Revealing Statements|Bug-Revealing Statement]].

This distinction is useful when reading generated bug reports.

## 15. MySQL #114904

Our project reproduces MySQL #114904 on MySQL 8.0.32.

See [[Concepts/DDLCheck/24 MySQL 114904 Walkthrough|MySQL #114904 Walkthrough]].

The simplified story is:

1. Create parent table t0.
2. Create child t1 with a foreign key referencing t0.
3. Rename t0 to t2.
4. Inspect t1: the visible foreign key now refers to t2.
5. Insert a parent row into t2.
6. Insert the matching child row into t1.

That last insert should succeed.

Instead, MySQL rejects it.

The failure text exposes stale internal information still referencing t0.

Now create the same final schema directly:

    parent = t2
    child FK → t2

The same insert succeeds.

So:

    visible schema(db_gen)
          =
    visible schema(db_syn)

but:

    INSERT behavior(db_gen)
          ≠
    INSERT behavior(db_syn)

That is DDLCheck's core idea in one real bug.

## 16. Root causes

See [[Concepts/DDLCheck/21 Root Causes of Schema Bugs|Root Causes of Schema Bugs]].

The paper discusses root causes including:

- incorrect maintenance of database schemas;
- incorrect maintenance of schema-related information;
- incorrect query optimization.

This is why DDLCheck is not merely testing DDL parsing.

Schema evolution interacts with catalogs, constraints, statistics, storage, and optimization.

## 17. Test-case reduction

Generated cases can be large.

DDLCheck uses [[Concepts/DDLCheck/22 Bug Report Reduction|Bug Report Reduction]] to remove unnecessary DDL and test statements while preserving the failure.

The basic strategy is:

    remove statement
          ↓
    bug still occurs?
       /        \
     yes        no
      ↓          ↓
    keep      restore
    removed

This is the shared [[Concepts/Shared/09 Test Case Reduction|Test Case Reduction]] idea.

Reduction turns random-testing output into a developer-friendly reproduction.

## 18. What the evaluation shows

See [[Concepts/DDLCheck/23 Evaluation and Findings|Evaluation and Findings]].

The paper evaluates:

- MySQL;
- PostgreSQL;
- SQLite;
- MariaDB;
- CockroachDB;
- TiDB.

The authors report:

- 34 submitted bugs;
- 29 confirmed as previously unknown;
- 9 fixed at the time described in the paper.

The evaluation also supports two design claims.

First, complex schema histories matter: many confirmed bugs require the evolved path.

Second, the DSTG-based optimization increases the number of unique histories tested and helps discover unique bugs faster.

## 19. Limits of the oracle

See [[Concepts/DDLCheck/25 Limitations and Scope|Limitations and Scope]].

DDLCheck cannot enumerate every possible schema or history.

It samples the space with randomized generation.

It also avoids nondeterministic SQL that would make comparison unreliable.

Finally, its structural-equivalence rules are a practical testing abstraction, not a universal proof that two arbitrary schemas are mathematically identical.

That is the tradeoff:

> strong enough to expose real schema-history bugs, practical enough to test production DBMSs.

# What to remember

Remember these five ideas:

1. A visible schema is not all the DBMS maintains.
2. seq_gen creates a complicated history.
3. seq_syn creates the same final schema directly.
4. Later SQL should behave the same on db_gen and db_syn.
5. DSTGs improve test-space diversity rather than defining the correctness oracle.

For the compact synthesis:

[[Concepts/DDLCheck/26 How DDLCheck Fits Together]]

## Previous

[[Guides/01 Understanding CODDTest|Part 1 — Understanding CODDTest]]

## Next

[[Guides/03 Understanding WriteCheck|Part 3 — Understanding WriteCheck]]
