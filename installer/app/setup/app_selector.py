from __future__ import annotations

from app.setup.selection import Selection


def edit_selection(selection: Selection) -> Selection:
    selected = []

    print()
    print("Choose applications")
    print("-------------------")

    for entry in selection.entries:
        answer = input(f"[Y/n] {entry.name}: ").strip().lower()

        if answer in ("", "y", "yes", "o", "oui"):
            selected.append(entry)

    return Selection(selected)
