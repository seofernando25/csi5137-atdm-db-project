# Deterministic Triggering

## In one sentence

A transaction bug is **deterministically triggerable** when a chosen statement submission order can reproduce it reliably without controlling hidden internal scheduling state.

## Why concurrency is usually hard

Concurrent systems can behave differently from run to run because:

- thread timing changes;
- lock acquisition changes;
- internal scheduling changes.

## What the paper found

Most studied WSS violations could be triggered by submitting statements in a particular order.

The paper reports that 90.6% of the studied WSS violations were deterministically triggerable this way.

## Why WriteCheck cares

This observation makes practical testing much simpler.

Instead of instrumenting the DBMS scheduler deeply, WriteCheck can:

1. generate a transaction group;
2. choose a submitted order;
3. observe what actually happened;
4. infer the oracle afterward.

## Important caveat

Submitted order still does not equal actual schedule.

See [[22 Submitted Order vs Actual Schedule]].

## Related

- [[18 Small-Scope Hypothesis]]
- [[23 Transaction Execution Protocol]]
