# Algorithmic Sketch

An **algorithmic sketch** is a high-level pseudocode description of a method. It communicates the essential procedure without every implementation detail.

CODDTest's Algorithm 1 can be summarized as:

1. Generate expression φ.
2. Determine whether φ is independent or dependent.
3. Build auxiliary query A.
4. Execute A to obtain Rφ.
5. Generate original query O containing φ.
6. Execute O.
7. Replace φ with Rφ to create folded query F.
8. Execute F.
9. If O and F disagree, report a bug.

## Key branch

Independent expression:

- evaluate one constant or constant list.

Dependent expression:

- evaluate a row-to-result mapping.

## Class-ready explanation

> Algorithm 1 formalizes how CODDTest evaluates an expression, embeds it in an original query, substitutes the evaluated result into a folded query, and compares the two.

You do not need to memorize the individual line numbers.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=6]]
