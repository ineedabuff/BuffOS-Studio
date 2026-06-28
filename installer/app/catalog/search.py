from __future__ import annotations

from app.catalog.entry import CatalogEntry
from app.catalog.loader import load_entries


def find_by_id(entry_id: str) -> CatalogEntry | None:
    for entry in load_entries():
        if entry.id == entry_id:
            return entry

    return None


def find_by_category(category: str) -> list[CatalogEntry]:
    return [entry for entry in load_entries() if entry.category == category]


def all_categories() -> list[str]:
    return sorted({entry.category for entry in load_entries()})
