from __future__ import annotations

from pathlib import Path


def available_profiles() -> list[str]:
    root = Path("installer/catalog/profiles")

    return sorted(path.stem for path in root.glob("*.yaml"))
