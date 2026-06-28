from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnswerSet:
    selected: dict[str, list[str]]

    def ids(self) -> list[str]:
        values: list[str] = []

        for entries in self.selected.values():
            values.extend(entries)

        return values
