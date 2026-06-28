from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "profiles"


def load(name: str, profile: str = "buff") -> list[str]:
    file = ROOT / profile / f"{name}.txt"

    if not file.exists():
        return []

    return [
        line.strip()
        for line in file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
