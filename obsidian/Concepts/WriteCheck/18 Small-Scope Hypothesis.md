# Small-Scope Hypothesis

## In one sentence

The **small-scope hypothesis** says that many important bugs can be exposed with small test cases rather than enormous inputs.

## What the empirical study found

The studied WSS violations generally needed small workloads:

- no more than 5 transactions;
- almost all involved transactions had no more than 5 statements;
- initial databases were also small.

## Why this matters

The space of all possible concurrent schedules is enormous.

Keeping tests small makes it practical to explore:

- different transaction groups;
- different statement orders;
- different isolation levels;
- different schema features.

## How WriteCheck uses it

The default generator bounds both the number of transactions and statements to small values.

This is not merely a convenience.

It is motivated by the empirical study of real transaction bugs.

## Related

- [[06 Transaction Test Cases]]
- [[19 Deterministic Triggering]]
- [[30 Evaluation and Findings]]
