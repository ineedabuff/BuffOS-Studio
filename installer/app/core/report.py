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

    def summary(self) -> None:
        print("\nSystem Analysis")
        print("-" * 40)

        for result in self.results:
            status = "✓" if result.success else "✗"
            print(f"{status} {result.title:<20} {result.message}")

        print("-" * 40)
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
