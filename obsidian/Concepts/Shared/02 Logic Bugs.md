# Logic Bugs

## In one sentence

A **logic bug** occurs when software completes normally but produces semantically incorrect behavior.

## DBMS example

A database might:

- return the wrong rows;
- reject a valid INSERT;
- accept an invalid state;
- maintain stale metadata;
- commit a transaction to an incorrect state.

None of these necessarily crashes the DBMS.

## Why this matters

Wrong-result bugs are harder to test than crashes because the tester needs a [[01 Test Oracle|test oracle]].

## Across the four papers

- CODDTest: query/expression logic.
- DDLCheck: schema-related logic and downstream behavior.
- WriteCheck: transaction/concurrency logic.
- Radar: metadata (index) logic.

The bug domains differ, but all four need a way to recognize incorrect behavior without knowing every correct result in advance.
