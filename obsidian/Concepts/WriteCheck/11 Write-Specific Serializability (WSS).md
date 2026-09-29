# Write-Specific Serializability (WSS)

## In one sentence

**Write-Specific Serializability (WSS)** requires a concurrent transaction schedule to produce the same final database state as its corresponding serial schedule, focusing on the effects of write operations.

## Core relation

    concurrent schedule H_con
             ↓
       final state A

    corresponding serial schedule H_ser
             ↓
       final state B

Expected:

    A = B

If the states differ, the schedule violates WSS.

## Why "write-specific"?

WSS focuses on what writes do to the final database state.

It deliberately does not require full equivalence of every read and write operation.

## Why WriteCheck cares

WSS becomes the paper's transaction test oracle.

The empirical study found that most studied critical transaction bugs had test cases violating this property.

## Important restriction

The paper assumes generated write operations do not depend on values returned by earlier reads in the same transaction.

See [[17 Read-Dependent Writes]].

## Related

- [[12 Transaction-Level and Statement-Level WSS]]
- [[13 WSS vs Other Serializability Notions]]
- [[25 Inferring the Serial Oracle]]
