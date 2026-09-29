# Isolation Levels

## In one sentence

An **isolation level** controls which effects of concurrent transactions are allowed to become visible to one another.

## Common levels

DBMSs commonly expose levels such as:

- Read Uncommitted;
- Read Committed;
- Repeatable Read;
- Serializable.

Different DBMSs implement these levels differently.

## Why WriteCheck cares

WriteCheck is designed to operate across multiple isolation levels, not only Serializable.

That is one motivation for WSS.

The paper argues that WSS is weaker than full conflict serializability and can therefore be applied more broadly.

## Important caveat

Write behavior is not perfectly standardized across DBMSs at weaker isolation levels.

This is why some WSS violations are considered permissible by developers.

See:

- [[27 Semi-Consistent Reads]]
- [[28 Gap Locks]]
- [[29 Permissible WSS Violations and False Positives]]

## Related

- [[13 WSS vs Other Serializability Notions]]
- [[09 Concurrency Control Modes]]
