# DDLCheck Architecture

## In one sentence

DDLCheck is a pipeline that builds two equivalent databases, exercises both with the same SQL, and compares their observable behavior.

## Five main pieces

### 1. DDL sequence generation

Create a complex seq_gen.

### 2. Sequence-oriented testing optimization

Avoid spending time on schema histories that are too similar to ones already tested.

### 3. DDL sequence synthesis

Inspect the final schema and create a simpler seq_syn.

### 4. SQL statement generation

Generate DDL/DML/DQL statements to execute against both databases.

### 5. Bug detection

Compare:

- errors;
- query results;
- resulting database states.

## Flow

    seq_gen → db_gen ─┐
                      ├─ same SQL → compare
    seq_syn → db_syn ─┘

## Related

- [[10 DDL Sequence Generation]]
- [[12 DDL Sequence Synthesis]]
- [[18 Interesting DDL Sequences]]
- [[14 DDLCheck Oracle]]

Paper Figure 1: [[PDFs/DDLCheck_PVLDB2025.pdf#page=4]]
