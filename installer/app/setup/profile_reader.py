from __future__ import annotations

from pathlib import Path


def read_profile(path: Path) -> list[str]:
    if not path.exists():
        return []

    ids: list[str] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("- "):
            ids.append(line.replace("- ", "", 1).strip())

    return ids
