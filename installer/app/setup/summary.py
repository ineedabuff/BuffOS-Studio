from __future__ import annotations

from app.setup.selection import Selection


def render_summary(selection: Selection) -> str:
    lines = [
        "Selection Summary",
        "-----------------",
    ]

    for entry in selection.entries:
        lines.append(f"- {entry.name} [{entry.category}]")

    return "\n".join(lines)
