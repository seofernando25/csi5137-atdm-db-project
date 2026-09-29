# Constant Propagation

## In one sentence

**Constant propagation** means replacing an expression with a value that has already been computed for it.

## Tiny example

Suppose folding establishes:

    φ = SELECT MIN(c0) FROM t0
    Rφ = 1

Then this:

    x IN (SELECT MIN(c0) FROM t0)

can be transformed into:

    x IN (1)

## Why CODDTest cares

The propagation step creates the **folded query F** from the **original query O**.

The original query contains φ.

The folded query contains Rφ.

## Folding vs propagation

    folding     = compute the value
    propagation = substitute the value

This distinction is central to the paper's title: **Constant Optimization Driven Database System Testing**.

## Don't confuse it with

Folding answers:

> What is this expression's value?

Propagation answers:

> Where can I safely use that known value?

## Related

- [[04 Constant Folding]]
- [[06 Original Auxiliary and Folded Queries]]
