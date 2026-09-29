# WSS vs Other Serializability Notions

## In one sentence

WSS is intentionally weaker than full conflict serializability, but stricter than merely saying the concurrent final state matches any arbitrary serial order.

## Conflict serializability

Requires a concurrent schedule to be equivalent to a serial schedule with respect to conflicting reads and writes.

This is a strong property usually associated with Serializable behavior.

## Final-state serializability

Requires only that there exists **some** serial schedule producing the same final database state.

It does not constrain which serial schedule should be used.

## WSS

Also compares final database state, but requires a serial schedule that follows the paper's WSS ordering rule.

WriteCheck uses [[14 FCRFS Serial Pattern|FCRFS]] to infer that order.

## Mental hierarchy

    conflict serializability
        stronger / more detailed

    WSS
        write-focused final-state property
        with ordering constraint

    final-state serializability
        only needs some matching serial state

## Why this matters

WSS is broad enough to apply beyond Serializable isolation while still giving WriteCheck a concrete oracle.

## Related

- [[08 Isolation Levels]]
- [[14 FCRFS Serial Pattern]]
