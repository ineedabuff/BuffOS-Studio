from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InstallReport:
    installed: list[str]
    skipped: list[str]
    failed: list[str]

    @property
    def success(self) -> bool:
        return not self.failed
