from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


FILES = {
    "README.md": """# Buff Helper

> Understand before you automate.

Buff Helper is a plugin-driven Linux assistant.

It helps users analyze, repair, optimize and learn from their systems.

## Quick Start

Run bootstrap, then analyze your system.

## Documentation

- English: docs/en/README.md
- Français: docs/fr/README.md
""",
    "VISION.md": """# Vision

Linux is powerful.

Power should be understandable.

Buff Helper exists to help users understand, repair, optimize and learn from Linux systems.
""",
    "PRINCIPLES.md": """# Principles

- Understand before you automate.
- Explain before you apply.
- Engine first.
- Plugin first.
- One feature, one test, one commit.
- Everything user-facing must be translatable.
- Documentation is part of the API.
- Build for five years, not five days.
""",
    "docs/en/README.md": """# Buff Helper Documentation

Buff Helper documentation in English.

## Sections

- Architecture
- Plugins
- Philosophy
""",
    "docs/fr/README.md": """# Documentation Buff Helper

Documentation de Buff Helper en français.

## Sections

- Architecture
- Plugins
- Philosophie
""",
}


def main() -> None:
    for relative, content in FILES.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"generated {relative}")


if __name__ == "__main__":
    main()
