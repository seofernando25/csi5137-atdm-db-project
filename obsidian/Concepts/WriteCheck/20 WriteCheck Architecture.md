# WriteCheck Architecture

## In one sentence

WriteCheck generates a concurrent transaction execution, reconstructs what actually happened, infers a serial oracle, replays it, and compares the results.

## Workflow

### 1. Generate initial database

Create small tables, constraints, and data.

### 2. Generate transactions

Create a transaction group containing reads, writes, and transaction-control statements.

### 3. Generate submitted order

Choose an interleaving in which statements will be sent to the DBMS.

### 4. Execute and observe

Run the workload and record the **actual concurrent schedule**, including blocking and aborts.

### 5. Infer serial schedules

Use FCRFS for:

- tx-WSS;
- stmt-WSS.

### 6. Replay serially

Apply the inferred serial schedules to the same initial database.

### 7. Compare

Check write outcomes and final database state.

A mismatch indicates a WSS violation.

## Related

- [[22 Submitted Order vs Actual Schedule]]
- [[25 Inferring the Serial Oracle]]
- [[26 Final-State Comparison]]

Paper Figure 3: [[PDFs/WriteCheck_PVLDB2025.pdf#page=6]]
