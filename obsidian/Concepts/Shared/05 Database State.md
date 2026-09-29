# Database State

## In one sentence

A **database state** is the database's data and relevant structure at a particular point in an execution.

## Why the term changes meaning across papers

### CODDTest

The state must stay fixed while an expression is evaluated and the original/folded queries are compared.

### DDLCheck

DDLCheck distinguishes the visible schema from the data state produced after DML statements. Two equivalent databases should remain behaviorally consistent.

### WriteCheck

The **final state** after a transaction schedule is an important observable used by the oracle.

## Important distinction

A database **schema** describes structure.

A database **state** usually includes actual stored data as well.

DDLCheck additionally introduces **schema-related internal information**, which may differ even when the visible schemas are equivalent.
