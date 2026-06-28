from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    id: str
    title: str
    category: str
    options: list[str]
    multiple: bool = True
