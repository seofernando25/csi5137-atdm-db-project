# Fact sheet: every number in the report and its source

Checked against the paper PDFs (`papers/` and the VLDB copy of Radar) on 2026-11-18.
"Fig." values are read off the published plots and are approximate. Everything else is copied
from the paper's text or tables.

## CODDTest (Zhang and Rigger, SIGMOD 2025)

| Fact | Value | Source |
|---|---|---|
| Campaign: unique new bugs | 45 (24 logic, 14 internal errors, 2 crashes, 5 hangs) | Sec. 4.1, Table 1 |
| Status, all 45 | 33 fixed, 12 verified | Sec. 4.1 |
| Status, the 24 logic bugs | 19 fixed, 5 verified | Sec. 4.1 |
| Manual analysis of the 24 logic bugs | NoREC 11, TLP 12, DQE 4, only CODDTest 11 | Table 2 |
| SQLite 3.30.0, 24 h, 10 threads: unique (exclusive) | NoREC 27 (3), TLP 27 (2), EET 6 (3), CODDTest 25 (4) | Sec. 4.2 |
| CODDTest misses in that run | 14 bugs, 4 of them index-related | Sec. 4.2 |
| Longest latent bug | 14 years, MySQL | Sec. 4.2 |
| Efficiency run | SQLite 3.42.0.0, 24 h, 10 threads, 64-core EPYC 7763, 512 GB | Sec. 4.3 |
| Tests in 24 h (thousands) | NoREC 2,086,646; TLP 976,216; DQE 441,350; CODDTest 497,092; expression only 1,423,068; subquery only 423,310 | Table 3 |
| Unique plans | 172,808; 137,743; 486; 2,577,603; 7,399; 2,755,619 | Table 3 |
| Branch coverage | 63.18; 63.63; 46.71; 63.06; 63.23; 62.19 % | Table 3 (all six configurations are reported) |
| Plans and coverage | collected in separate runs with the same configuration | Sec. 4.3 |
| Slowdown | 4.20 times slower than NoREC, 1.96 times slower than TLP | Sec. 4.3 |
| Depth sweep, MaxDepth 1 to 15 | time per query 9.91 times higher, throughput down 89.4% | Sec. 4.3, Figs. 2 and 3 |
| Campaign duration | intermittent, four months | Sec. 4.1 |

## DDLCheck (Song et al., PVLDB 18(7) 2025)

| Fact | Value | Source |
|---|---|---|
| Submitted / confirmed | 34 / 29 (21 schema bugs, 8 crashes) | Table 2 |
| Submitted per DBMS | MySQL 14, MariaDB 11, CockroachDB 2, TiDB 7, PostgreSQL 0, SQLite 0 | Table 2 |
| False positives | 0; duplicates 4; fixed 9 | Table 2 |
| Schema bugs without a query-result difference | 7 (4 stored state, 3 schema) | Sec. 4.2 |
| Bug-revealing statements (29) | SELECT 23, CREATE 2, INSERT 2, ALTER 1, REPLACE 1 | Fig. 6 |
| Conceptual comparison on the 21 schema bugs | NoREC 0, Radar 13, DQP 9 | Table 4 |
| Ablation, 24 h per DBMS, six DBMSs | unique sequences 20,468 / 14,994 / 17,967; unique bugs 8 / 5 / 4; bug occurrences 9 / 6 / 9 | Table 3 |
| Default max DDL length (`maxLength`) | 10 (5,000 statements per database pair) | Sec. 3.2, Sec. 4.1 |
| Hardware | 8 cores, 32 GB | Sec. 4.1 |

## Radar (Song et al., PVLDB 17(8) 2024)

| Fact | Value | Source |
|---|---|---|
| Reports, then unique bugs | 1,663 reports, of which 1,621 were duplicates, leaving 42 submitted | Sec. 4.2 |
| Confirmed | 38 (30 metadata bugs, 8 other); 1 duplicate; 3 false positives | Table 2 |
| Discovery protocol | 10 rounds of 24 h per DBMS | Sec. 4.1 |
| Where the bugs are | TiDB: 31 of the 42 submitted, 24 of the 30 metadata bugs | Table 2 |
| Conceptual comparison on the 30 metadata bugs | NoREC 13, DQE 8, MutaSQL 5, TLP 3 | Table 5, Sec. 4.4.1 |
| End-to-end, 12 h | 21 metadata bugs by all tools; Radar 20, 15 found only by Radar; the alternatives 6 | Table 6, Sec. 4.4.2 |
| Ablation, 12 h, five DBMSs | 22 unique bugs with guidance, 14 without; TiDB 19 against 12 | Table 3 and Fig. 7 |
| Function coverage | MySQL 20.3% against 19.7%; MariaDB 19.7% against 19.3% | Table 4 |
| CockroachDB deployment | three-node cluster | Sec. 4.1 |

The old text cited Radar "Tables 4 and 5" for the comparisons. They are Tables 5 and 6.

## WriteCheck (Cui et al., PVLDB 18(8) 2025)

| Fact | Value | Source |
|---|---|---|
| Historical study | 140 transaction bugs, 35 critical; 32 (91.4%) violate WSS | Secs. 3.1 and 3.2 |
| Triggering conditions (Fig. 2, n = 32) | all need ≤2 tables and ≤5 transactions; 97.0% of tables ≤5 rows; 71.9% need schema properties | Sec. 3.4 |
| Critical bugs per DBMS (13) | MySQL 1, MariaDB 3, TiDB 9 | Table 3 |
| WSS breakdown (of 35 critical bugs) | 15 violate tx-WSS, 32 violate stmt-WSS (all 15 tx-WSS are a subset) | Sec. 3.2 |
| Serializable read-result check | Supported except PostgreSQL (SSI); 0 bugs found in evaluation | Secs. 5.4, 6.2 |
| Deterministic triggering | 29 of the 32 WSS violations (90.6%) | Sec. 3.4, Finding 5 |
| Discovery | 101 WSS violations, 22 unique; 13 confirmed critical (11 new, 2 known); 9 false positives | Table 2, Sec. 6.2 |
| Protocol | 5 rounds; 8 cores, 32 GB | Sec. 6.1 |
| Comparison set (29) | **13 found by WriteCheck plus 16 from DT², Troc and TxCheck.** This set is different from the 29 deterministic violations above | Sec. 6.5.1 |
| Capability on the 29 | WriteCheck 29, DT² 23, TxCheck 16, Troc 14; Elle, Cobra and Emme 0 | Table 3 (Sec. 6.5.1) |
| End-to-end, 12 h | critical / false positives: WriteCheck 4 / 5, DT² 2 / 24, Troc 2 / 4, TxCheck 1 / 4 | Table 4 (Sec. 6.5.2) |
| Causes of WriteCheck's false positives | 2 semi-consistent reads, 3 missing gap locks | Sec. 6.5.2; analysis in Sec. 6.4 |
| The other tools also report non-critical bugs | WriteCheck cannot detect non-critical bugs | Sec. 6.5.2 |

## Errors fixed in the second pass

5. WriteCheck's triggering-condition shares (its Fig. 2) are over the 32 WSS violations, with
   rows counted per initial table and statements per transaction. They are not over the 35
   critical bugs.

## Errors fixed in this pass

1. WriteCheck's comparison set was described as "the subset of the 32 that can be triggered
   by controlling statement order". It is 13 bugs found by WriteCheck plus 16 found by other
   tools (Sec. 6.5.1).
2. The caption of the CODDTest efficiency plot said branch coverage is not reported for the
   single-component variants. Table 3 reports it: 63.23% and 62.19%.
3. Two floats shared the label `fig:codd`, so "Figure 2" in Sec. 5.4 pointed to the explainer
   instead of the efficiency plot.
