from __future__ import annotations

from pathlib import Path

from app.catalog.search import find_by_id
from app.setup.selection import Selection


def load_default_profile() -> Selection:
    path = Path("installer/app/profiles/buff/profile.yaml")

    entries = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("- "):
            app_id = line[2:].strip()
            entry = find_by_id(app_id)

            if entry is not None:
                entries.append(entry)

    return Selection(entries)
