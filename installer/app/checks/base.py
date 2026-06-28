from __future__ import annotations

from abc import ABC, abstractmethod

from app.checks.result import CheckResult


class BaseCheck(ABC):
    id: str
    title: str
    category: str
    weight: int = 1
    fixable: bool = False

    @abstractmethod
    def run(self) -> CheckResult:
        """Execute the check."""
