from __future__ import annotations

from pathlib import Path

from app.catalog.search import find_by_id
from app.setup.selection import Selection


def load_profile(profile: str) -> Selection:
    path = Path("installer/catalog/profiles") / f"{profile}.yaml"

    entries = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("- "):
            entry = find_by_id(line[2:].strip())

            if entry is not None:
                entries.append(entry)

    return Selection(entries)
