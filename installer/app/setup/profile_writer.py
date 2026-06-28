from __future__ import annotations

from pathlib import Path

from app.setup.selection import Selection


def write_profile(selection: Selection, path: Path) -> Path:
    lines = [
        "applications:",
    ]

    for entry in selection.entries:
        lines.append(f"  - {entry.id}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return path
