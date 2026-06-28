from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "profiles" / "buff"


def load(name: str) -> list[str]:
    file = ROOT / f"{name}.txt"

    if not file.exists():
        return []

    return [
        line.strip()
        for line in file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
