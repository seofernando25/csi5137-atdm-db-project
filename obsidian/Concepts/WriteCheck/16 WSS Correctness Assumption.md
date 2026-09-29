# WSS Correctness Assumption

## In one sentence

WriteCheck's correctness argument assumes the DBMS correctly identifies relevant write conflicts and correctly blocks or aborts transactions because of those conflicts.

## Assumption 1

Conceptually:

    conflicting concurrent writes
            ↓
    DBMS recognizes conflict
            ↓
    block or abort appropriately

## Why the theorem needs this

Suppose T1 finishes while another transaction has an unresolved conflicting write that should have prevented T1 from completing.

Then "first transaction to finish should come first in the serial schedule" would no longer be safe reasoning.

FCRFS depends on the DBMS enforcing those write conflicts correctly.

## Why this assumption is extremely important

It explains both:

- why the oracle works when the assumption holds;
- why WriteCheck can report developer-accepted behavior as a false positive when the assumption does not hold.

Examples:

- [[27 Semi-Consistent Reads]]
- [[28 Gap Locks]]

## Related

- [[10 Write-Write Conflicts]]
- [[14 FCRFS Serial Pattern]]
- [[29 Permissible WSS Violations and False Positives]]
