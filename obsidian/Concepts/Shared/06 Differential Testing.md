# Differential Testing

## In one sentence

**Differential testing** runs the same input on multiple implementations or configurations and compares their outputs.

## Classic DBMS version

    same query
      ↓       ↓
    DBMS A  DBMS B
      ↓       ↓
    result A ?= result B

A disagreement reveals inconsistency, although it does not automatically tell us which implementation is wrong.

## Why DDLCheck discusses it

Traditional differential testing can compare multiple DBMSs, but different engines support different SQL features and semantics.

DDLCheck instead creates **two equivalent databases inside the same DBMS** and executes the same statements on both.

## Don't confuse it with

Metamorphic testing usually transforms the **input**.

Differential testing usually varies the **implementation/configuration** receiving the same input.

Both are ways to address the [[01 Test Oracle|oracle problem]].
