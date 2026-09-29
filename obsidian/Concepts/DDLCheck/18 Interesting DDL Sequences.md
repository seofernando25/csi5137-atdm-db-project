# Interesting DDL Sequences

## In one sentence

An **interesting DDL sequence** is one whose schema-transition history is sufficiently different from histories DDLCheck has already tested.

## The problem

Pure random generation can waste time:

    sequence A
    sequence B
    sequence C

may all exercise nearly the same structural transitions.

That leads to:

- duplicate bug reports;
- poor test-space exploration;
- fewer unique behaviors tested per hour.

## DDLCheck's optimization

1. translate seq_gen into a [[16 Database Schema Transition Graph (DSTG)|DSTG]];
2. compare it with previously tested DSTGs;
3. if an equivalent/similar history already exists, skip it;
4. otherwise, test it and record its graph.

## Why this matters

This is not part of the **correctness oracle** itself.

It is a **testing-efficiency optimization**.

The paper's evaluation shows it increases the number of unique DDL sequences tested and helps find unique bugs faster.

## Related

- [[17 Table Structure Equivalence]]
- [[23 Evaluation and Findings]]
