from __future__ import annotations

from dataclasses import dataclass

from app.catalog.entry import CatalogEntry


@dataclass(frozen=True)
class Selection:
    entries: list[CatalogEntry]

    @property
    def ids(self) -> list[str]:
        return [entry.id for entry in self.entries]
