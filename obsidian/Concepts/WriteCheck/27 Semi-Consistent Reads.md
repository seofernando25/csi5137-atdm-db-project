# Semi-Consistent Reads

## In one sentence

A **semi-consistent read** is a DBMS behavior in which a write statement may inspect a committed version of a locked row to decide whether the row matches its predicate.

## Why this matters

Suppose T1 has changed a row but not yet committed.

T2 runs an UPDATE with a WHERE condition.

Instead of simply waiting before evaluating the row, some MySQL/MariaDB behavior can inspect the latest committed version to decide whether T2 should care about that row.

This can reduce locking.

## Why WriteCheck notices it

The behavior can produce a final database state that differs from the FCRFS serial state.

Under WriteCheck's Assumption 1, that looks like a WSS violation.

DBMS developers may nevertheless consider the behavior intentional at that isolation level.

## Paper result

Semi-consistent reads are one major source of the paper's developer-classified false positives.

## General lesson

The oracle assumes a particular write-conflict semantics.

Real DBMS write semantics at weaker isolation levels can be more permissive.

## Related

- [[16 WSS Correctness Assumption]]
- [[29 Permissible WSS Violations and False Positives]]
