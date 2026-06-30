from __future__ import annotations

from pathlib import Path


def profile_tasks(profile: str) -> list[str]:
    path = Path("installer/catalog/tasks") / f"{profile}-postinstall.yaml"

    if not path.exists():
        return []

    tasks = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("- "):
            tasks.append(line[2:])

    return tasks
