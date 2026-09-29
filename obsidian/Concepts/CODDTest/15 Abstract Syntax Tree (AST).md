# Abstract Syntax Tree (AST)

An **Abstract Syntax Tree**, or AST, represents program or query structure as a tree instead of plain text.

For the expression a + b > 5, a simplified tree is:

        >
       / \
      +   5
     / \
    a   b

## Why an AST helps CODDTest

A query generator can manipulate syntax structurally:

1. find the node representing expression φ;
2. evaluate φ;
3. replace that node with an expression representing the folded value.

This is safer and more systematic than arbitrary string replacement.

## How important is this?

ASTs are implementation detail, not the main research idea.

For the presentation, mention ASTs only if explaining how SQLancer performs the transformation internally.

Related: [[14 SQLancer]]
