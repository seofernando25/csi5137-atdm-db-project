# How CODDTest Fits Together

If you understand this page, you understand the core paper.

## Step 1 — Oracle problem

A DBMS can return a wrong answer without crashing.

See [[01 Test Oracle]] and [[12 Logic Bugs]].

## Step 2 — Metamorphic solution

We do not know the correct answer, but we can construct two queries that should agree.

See [[02 Metamorphic Testing]] and [[03 Metamorphic Relation]].

## Step 3 — Choose expression φ

Generate an expression under a fixed [[11 Database State|database state]].

## Step 4 — Fold φ

Use auxiliary query A to compute Rφ.

See [[04 Constant Folding]].

## Step 5 — Build original O

Generate a query containing φ.

## Step 6 — Propagate Rφ

Replace φ with Rφ to create folded query F.

See [[05 Constant Propagation]] and [[06 Original Auxiliary and Folded Queries]].

## Step 7 — Handle dependency

If φ is independent, one constant is enough.

If φ depends on outer-row values, compute a row-to-result mapping.

See [[07 Independent and Dependent Expressions]], [[07A Independent Expressions]], [[07B Dependent Expressions]], and [[10 SQL CASE and Row Mapping]].

## Step 8 — Compare

E_s(O) = E_s(F) → test passes.

E_s(O) ≠ E_s(F) → bug candidate.

## Full mental model

Test oracle problem  
↓  
Metamorphic testing  
↓  
Generate φ  
↓  
Auxiliary query A  
↓  
Constant folding → Rφ  
↓  
Original O versus Folded F  
↓  
Compare results  
↓  
Mismatch = potential DBMS bug

## Implementation layer

[[14 SQLancer]] provides the framework.

[[15 Abstract Syntax Tree (AST)|ASTs]] help represent and transform generated queries.

## Comparison layer

See [[16 Existing Oracles - TLP NoREC PQS DQE]] and its TLP, NoREC, PQS, and DQE child notes.

Return to [[Papers/01 CODDTest]].
