# CODDTest Concept Map

## Core chain

Test oracle  
↓  
Metamorphic testing  
↓  
Metamorphic relation  
↓  
Constant folding + constant propagation  
↓  
A / O / F queries  
↓  
Independent vs dependent expressions  
↓  
Algorithm 1  
↓  
Compare O and F  
↓  
Mismatch = logic-bug candidate

## Foundation

- [[Concepts/Shared/01 Test Oracle|Test Oracle]]
- [[Concepts/Shared/03 Metamorphic Testing|Metamorphic Testing]]
- [[03 Metamorphic Relation]]
- [[Concepts/Shared/02 Logic Bugs|Logic Bugs]]

## Constant-optimization vocabulary

- [[04 Constant Folding]]
- [[05 Constant Propagation]]
- [[06 Original Auxiliary and Folded Queries]]
- [[Concepts/Shared/05 Database State|Database State]]

## SQL concepts

- [[08 Predicates and Three-Valued Logic]]
  - [[08A Predicates]]
  - [[08B SQL Three-Valued Logic]]
- [[09 Correlated and Non-correlated Subqueries]]
- [[10 SQL CASE and Row Mapping]]
- [[07 Independent and Dependent Expressions]]
  - [[07A Independent Expressions]]
  - [[07B Dependent Expressions]]

## Implementation and comparisons

- [[Concepts/Shared/10 Algorithmic Sketch|Algorithmic Sketch]]
- [[Concepts/Shared/11 SQLancer|SQLancer]]
- [[15 Abstract Syntax Tree (AST)]]
- [[16 Existing Oracles - TLP NoREC PQS DQE]]
  - [[16A TLP - Ternary Logic Partitioning]]
  - [[16B NoREC - No Rewriting Required]]
  - [[16C PQS - Pivoted Query Synthesis]]
  - [[16D DQE - Differential Query Execution]]
- [[18 False Positives and Floating Point]]
- [[19 Beyond Predicates]]

## Synthesis

- [[17 How CODDTest Fits Together]]
- [[Papers/01 CODDTest]]
