# Metamorphic Testing

**Metamorphic testing** is useful when the exact expected output is unknown, but a relationship between multiple executions is known.

Original input I → output O  
Follow-up input I' → output O'

The test checks a known relationship between O and O' instead of comparing against a precomputed correct answer.

## CODDTest

CODDTest constructs an original query O and a folded query F. Under the same database state, they should return identical results.

This directly addresses the [[01 Test Oracle|oracle problem]].

## Why the word metamorphic?

The original input is transformed into a related follow-up input while preserving some expected semantic property.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=4]]  
Next: [[03 Metamorphic Relation]]
