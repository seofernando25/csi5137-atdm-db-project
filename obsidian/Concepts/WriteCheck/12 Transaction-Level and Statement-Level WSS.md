# Transaction-Level and Statement-Level WSS

## In one sentence

WriteCheck checks WSS at two granularities: **whole transactions** and **individual surviving SQL statements**.

## tx-WSS

Transaction-level WSS keeps an explicit transaction together as one unit.

Example:

    T1 = BEGIN → UPDATE → DELETE → COMMIT
    T2 = BEGIN → INSERT → COMMIT

The oracle serializes complete transactions.

## stmt-WSS

Statement-level WSS builds a simplified serial schedule.

For committed transactions:

- remove BEGIN / COMMIT;
- execute remaining DQL/DML statements as autocommit transactions.

For aborted transactions:

- ignore their statements.

## Why both exist

Some bugs only appear when transaction boundaries are preserved.

Others can be exposed by comparing statement-level effects.

The paper found cases detected only by stmt-WSS.

## Don't confuse them

stmt-WSS is **not** simply "tx-WSS with fewer statements."

It deliberately changes transaction boundaries for the simplified oracle.

## Related

- [[02 Explicit and Autocommit Transactions]]
- [[11 Write-Specific Serializability (WSS)]]
