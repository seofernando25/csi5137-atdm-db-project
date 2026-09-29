# WriteCheck Limitations and Scope

## In one sentence

WriteCheck is deliberately simple, but that simplicity depends on workload restrictions, random exploration, and an assumption about how DBMSs handle write conflicts.

## 1. Unsupported SQL features

The generator may miss bugs requiring features it does not generate, such as nondeterministic functions.

## 2. Random exploration

The transaction and schedule space is enormous.

WriteCheck samples it rather than exhaustively enumerating every case.

Therefore it can miss bugs.

## 3. Oracle-order sensitivity

A buggy DBMS may itself produce an unusual actual schedule.

If the inferred FCRFS serial schedule happens to produce the same incorrect final state, WriteCheck can miss the bug.

## 4. Not every critical transaction bug violates WSS

The empirical study found some critical transaction bugs whose test cases did not violate WSS.

WriteCheck cannot detect such bugs using this oracle.

## 5. False positives when Assumption 1 does not hold

Permissible behaviors such as semi-consistent reads or missing gap locks can violate WSS without being classified as implementation bugs.

## 6. Final-state focus

WriteCheck is strongest at detecting incorrect write effects.

It is not a complete verifier for every read anomaly or every transaction semantic.

## Related

- [[16 WSS Correctness Assumption]]
- [[29 Permissible WSS Violations and False Positives]]
