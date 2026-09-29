# Existing Transaction Verification and Testing Approaches

## In one sentence

WriteCheck compares against tools that either verify transaction histories against isolation models or construct different transaction-testing oracles.

## Verification approaches

Examples:

- Elle;
- Cobra;
- Emme.

These analyze histories and dependency relationships to determine whether claimed isolation guarantees were violated.

The paper argues they often assume key-value-like models and can miss bugs involving complex SQL features or histories without dependency cycles.

## Testing approaches

### DT2

Uses differential testing across DBMSs.

Limitation: DBMS-specific features and shared incorrect behavior can defeat the oracle.

### Troc

Tests pairs of transactions through an MVCC-based oracle.

Limitation in the paper's comparison: restricted feature/transaction patterns.

### TxCheck

Infers statement dependencies and constructs semantically related test cases.

Its effectiveness depends on correctly capturing those dependencies.

## Why WriteCheck argues for simplicity

WriteCheck needs only:

- a concurrent schedule;
- its inferred serial order;
- final-state comparison.

This makes it easier to support complex SQL and multiple DBMSs.

## Project note

Our project reproduction for MySQL #104833 uses **Troc**, not a rerun of WriteCheck.

See [[32 Project Reproduction - MySQL 104833]].
