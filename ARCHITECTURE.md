# Buff Helper Architecture

> Analyze. Repair. Optimize.

Buff Helper is an intelligent Linux assistant designed to analyze,
repair, optimize and explain Linux systems.

It is **not** a Linux distribution.

It is **not** an installation script.

It is a reusable engine that powers multiple interfaces.

---

# Philosophy

The user should always understand:

- What is happening
- Why it is recommended
- What are the benefits
- What are the trade-offs
- How to undo the change

Nothing should happen silently.

---

# Design Principles

1. Engine first.
2. UI contains no business logic.
3. Everything is testable.
4. Plugins extend the engine.
5. Providers isolate distributions.
6. Profiles describe systems.
7. Every change should be reversible.
8. Explain before applying.
9. Beautiful code matters.
10. Simplicity wins.

---

# Architecture

GUI
TUI
CLI
API
 │
 ▼
 Engine
 │
 ├── Analysis
 ├── Doctor
 ├── Planner
 ├── Installers
 ├── Validators
 ├── Optimizer
 ├── Plugins
 └── Providers

---

# Development Rule

One feature

↓

One test

↓

One commit

---

# Goal

Help Linux users understand their system,
not only modify it.
