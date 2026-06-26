from __future__ import annotations

from app.analysis.result import CheckResult


class ValidationReport:
    def __init__(self) -> None:
        self._results: dict[str, CheckResult] = {}

    def add(self, result: CheckResult) -> None:
        self._results[result.title] = result

    def get(self, title: str) -> CheckResult | None:
        return self._results.get(title)

    def all(self) -> list[CheckResult]:
        return list(self._results.values())

    @property
    def passed(self) -> int:
        return sum(result.success for result in self._results.values())

    @property
    def failed(self) -> int:
        return len(self._results) - self.passed
