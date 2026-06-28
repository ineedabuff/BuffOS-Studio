from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CatalogEntry:
    id: str
    name: str
    category: str
    path: Path
