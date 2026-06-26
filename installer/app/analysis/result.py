from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResult:
    """Result returned by a BuffOS system check."""

    success: bool
    title: str
    message: str

    @property
    def failed(self) -> bool:
        return not self.success
