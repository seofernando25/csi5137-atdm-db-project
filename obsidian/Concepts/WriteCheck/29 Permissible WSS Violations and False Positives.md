# Permissible WSS Violations and False Positives

## In one sentence

A WriteCheck **false positive** is a WSS violation that DBMS developers consider intentional or permissible under that system's transaction semantics rather than an implementation bug.

## Why they happen

The WSS proof depends on [[16 WSS Correctness Assumption|Assumption 1]].

Some DBMSs intentionally use write behavior that does not satisfy that assumption.

The paper's main examples are:

- [[27 Semi-Consistent Reads]];
- [[28 Gap Locks|lack of gap locks]].

## Important nuance

"False positive" here does not necessarily mean the behavior is intuitive.

The authors argue some permissible violations create:

- inconsistent write semantics;
- confusing partial updates;
- different behavior across DBMSs;
- different behavior across isolation levels.

But if the DBMS specification allows the behavior, WriteCheck cannot label it a critical implementation bug automatically.

## General testing lesson

An oracle is only valid inside its assumptions.

When the semantics are underspecified, bug classification may require developer feedback.

## Related

- [[33 Limitations and Scope]]
- [[30 Evaluation and Findings]]
