# Contributing to BuffOS Studio

## Development Philosophy

BuffOS Studio follows a simple rule:

One step. One test. One commit.

---

## Git Workflow

- Work on a dedicated branch.
- Keep commits small.
- Use clear commit messages.
- Test before pushing.

---

## Commit Style

Use this format:

type(scope): message

Examples:

feat(engine): add report object
fix(analysis): detect btrfs correctly
docs: update roadmap
refactor(core): simplify runner

---

## Project Rules

- UI never talks directly to modules.
- Modules never call other modules.
- Providers never make decisions.
- Analysis never modifies the system.
- Engine orchestrates everything.

---

## Testing

Before every commit:

python3 installer/launcher.py

