# WriteCheck Evaluation and Findings

## In one sentence

The evaluation tests whether WSS is a useful bug oracle and whether WriteCheck can expose real critical transaction bugs across production DBMSs.

## Systems

The paper evaluates:

- MySQL 8.0.32;
- PostgreSQL 15.2;
- SQLite 3.36.0;
- MariaDB 10.11.2;
- CockroachDB 22.2.5;
- TiDB 6.6.0.

## Empirical-study findings

From 35 studied critical transaction bugs:

- 32, or 91.4%, had test cases violating WSS;
- studied WSS violations generally had small initial databases;
- all used no more than five transactions;
- almost all transactions had no more than five statements;
- 90.6% of the studied WSS violations could be triggered deterministically by statement ordering.

These findings motivate WriteCheck's design.

## WriteCheck results

Across the six DBMSs, WriteCheck detected:

- 101 WSS violation instances;
- 22 unique WSS violations;
- 13 confirmed critical transaction bugs;
- 11 confirmed as new critical transaction bugs;
- 9 developer-classified false positives.

The paper reports that 6 unique violations were detectable only by stmt-WSS and 16 by both tx-WSS and stmt-WSS.

## Main takeaway

> A surprisingly simple final-state oracle can expose many serious transaction-engine bugs when the serial reference order is chosen carefully.

Paper evaluation: [[PDFs/WriteCheck_PVLDB2025.pdf#page=8]]
