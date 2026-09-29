# Grammar-Based Test Generation

## In one sentence

**Grammar-based generation** uses rules describing valid syntax to construct test inputs.

## Tiny example

A simplified DDL grammar might say:

    ddlStatement :=
        CREATE TABLE
      | ALTER TABLE
      | DROP TABLE

Each production expands into more detailed rules.

## Why this helps

Random characters rarely form useful SQL. A grammar keeps generated statements syntactically meaningful while still exploring many combinations.

## DDLCheck

DDLCheck uses DBMS-specific grammar information for DDL and SQL generation, combined with [[07 Stateful Test Generation|stateful generation]] so the statements are also contextually valid.

## Don't confuse it with

A grammar guarantees structure/syntax.

It does not by itself guarantee semantic validity; the generator still needs knowledge of the current database schema.
