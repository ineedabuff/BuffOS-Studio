from __future__ import annotations

from app.analysis.result import CheckResult
from app.validators.readiness_score import ReadinessScore
from app.validators.validation_report import ValidationReport


class Report:
    EXCLUDED_FROM_READINESS = {
        "Planned Fixes",
        "Installation",
    }

    def __init__(self) -> None:
        self._results: list[CheckResult] = []

    def add(self, result: CheckResult) -> None:
        self._results.append(result)

    def extend(self, results: list[CheckResult]) -> None:
        self._results.extend(results)

    @property
    def readiness(self) -> int:
        validation = ValidationReport()

        for result in self.validation_results:
            validation.add(result)

        return ReadinessScore().calculate(validation)

    @property
    def validation_results(self) -> list[CheckResult]:
        return [
            result
            for result in self._results
            if result.title not in self.EXCLUDED_FROM_READINESS
        ]

    @property
    def passed(self) -> int:
        return sum(result.success for result in self.validation_results)

    @property
    def failed(self) -> int:
        return len(self.validation_results) - self.passed

    @property
    def status(self) -> str:
        if self.readiness == 100:
            return "System Ready"

        return "Installation Required"

    def summary(self) -> None:
        print()
        print("System Analysis")
        print("----------------------------------------")

        for result in self._results:
            print(
                f"{'✓' if result.success else '✗'} {result.title:<20} {result.message}"
            )

        print("----------------------------------------")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print()
        print(f"BuffOS Readiness: {self.readiness}%")
        print(f"Status: {self.status}")
