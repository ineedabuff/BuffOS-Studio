from __future__ import annotations

from app.checks.result import CheckResult


class Report:
    """Collects the results of every executed check."""

    def __init__(self) -> None:
        self.results: list[CheckResult] = []

    def add(self, result: CheckResult) -> None:
        self.results.append(result)

    @property
    def passed(self) -> int:
        return sum(result.success for result in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed
