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

        for result in self._results:
            if result.title not in self.EXCLUDED_FROM_READINESS:
                validation.add(result)

        return ReadinessScore().calculate(validation)

    @property
    def status(self) -> str:
        if self.readiness == 100:
            return "System Ready"

        return "Installation Required"

    def summary(self) -> None:
        print()
        print("System Analysis")
        print("----------------------------------------")

        passed = 0
        failed = 0

        for result in self._results:
            print(
                f"{'✓' if result.success else '✗'} {result.title:<20} {result.message}"
            )

            if result.success:
                passed += 1
            else:
                failed += 1

        print("----------------------------------------")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print()
        print(f"BuffOS Readiness: {self.readiness}%")
        print(f"Status: {self.status}")
