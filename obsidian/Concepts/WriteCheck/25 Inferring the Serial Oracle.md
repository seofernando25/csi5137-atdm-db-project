# Inferring the Serial Oracle

## In one sentence

WriteCheck builds its reference execution by converting the observed concurrent schedule into an FCRFS serial schedule.

## tx-WSS oracle

Scan the actual schedule.

When a transaction reaches COMMIT or ROLLBACK, append that transaction to the serial list.

For autocommit transactions, append them directly.

This produces:

    H_FCRFS

## stmt-WSS oracle

Start from the transaction-level order.

Then:

- remove aborted transactions;
- remove BEGIN / COMMIT / ROLLBACK from committed transactions;
- keep the remaining DQL/DML statements;
- replay them as individual autocommit statements.

## Why this is the heart of WriteCheck

Without this step, WriteCheck would know:

    concurrent final state = X

but not what the correct reference state should be.

FCRFS manufactures the reference execution.

## Connection to other papers

CODDTest manufactures a folded query.

DDLCheck manufactures a directly constructed equivalent database.

WriteCheck manufactures an inferred serial execution.

## Related

- [[14 FCRFS Serial Pattern]]
- [[26 Final-State Comparison]]
