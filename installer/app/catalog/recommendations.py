from __future__ import annotations

from app.catalog.loader import load_entries


def recommended():
    apps = []

    for entry in load_entries():
        text = entry.path.read_text(encoding="utf-8")

        if "recommended: true" in text:
            apps.append(entry)

    return sorted(apps, key=lambda app: app.name)
