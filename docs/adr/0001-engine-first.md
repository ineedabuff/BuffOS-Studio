# ADR 0001

## Title

Engine First Architecture

## Status

Accepted

## Context

Buff Helper will eventually provide:

- CLI
- Rich TUI
- Qt GUI
- API

Duplicating business logic between these interfaces would
increase maintenance costs.

## Decision

All business logic belongs to the Engine.

Interfaces are only presentation layers.

## Consequences

Advantages

- Easy testing
- Easy maintenance
- Multiple frontends

Trade-offs

- Slightly more abstraction
- More files
