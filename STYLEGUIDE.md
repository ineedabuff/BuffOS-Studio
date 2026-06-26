# BuffOS Studio Style Guide

## General

- Readability over cleverness.
- Explicit is better than implicit.
- Small functions.
- Small classes.
- One responsibility per object.

---

## Naming

Classes:
- PascalCase

Functions:
- snake_case

Variables:
- snake_case

Constants:
- UPPER_CASE

---

## Modules

A module should orchestrate work.

A module should not contain business logic.

---

## Providers

Providers perform actions.

Providers never make decisions.

---

## Analysis

Analysis never changes the system.

Analysis only collects information.

---

## Engine

Engine coordinates everything.

Engine never contains Linux-specific logic.

---

## Logging

Never use print().

Always use the project logger.

---

## Commits

One feature.

One test.

One commit.

