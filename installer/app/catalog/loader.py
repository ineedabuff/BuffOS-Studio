from __future__ import annotations

from pathlib import Path

from app.catalog.entry import CatalogEntry

ROOT = Path(__file__).resolve().parents[2] / "catalog" / "applications"


def _read_value(text: str, key: str) -> str:
    prefix = f"{key}:"

    for line in text.splitlines():
        if line.startswith(prefix):
            return line.replace(prefix, "", 1).strip()

    return ""


def load_entries() -> list[CatalogEntry]:
    entries: list[CatalogEntry] = []

    for path in sorted(ROOT.glob("*/*.yaml")):
        text = path.read_text(encoding="utf-8")

        entries.append(
            CatalogEntry(
                id=_read_value(text, "id"),
                name=_read_value(text, "name"),
                category=_read_value(text, "category"),
                path=path,
            )
        )

    return entries
