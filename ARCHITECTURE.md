# BuffOS Studio Architecture

> Version 1.0
>
> This document defines the architecture of BuffOS Studio.
> Every new feature must follow these principles.

---

## Philosophy

BuffOS Studio is built around a reusable engine.

Applications should contain as little logic as possible.

Business logic belongs inside modules.

System interactions belong inside providers.

System inspection belongs inside analysis.

---

## Layers

UI
↓
Application
↓
Engine
↓
Modules
↓
Analysis + Providers

---

## Rules

- UI never talks directly to modules.
- Modules never call other modules.
- Providers never make decisions.
- Analysis never modifies the system.
- Engine orchestrates everything.

