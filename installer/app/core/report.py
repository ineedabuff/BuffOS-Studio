from __future__ import annotations

from app.analysis.result import CheckResult
from app.validators.readiness_score import ReadinessScore
from app.validators.validation_report import ValidationReport


class Report:
    def __init__(self) -> None:
        self._results: list[CheckResult] = []

    def add(self, result: CheckResult) -> None:
        self._results.append(result)

    def summary(self) -> None:
        print()
        print("System Analysis")
        print("----------------------------------------")

        passed = 0
        failed = 0

        readiness = ValidationReport()

        for result in self._results:
            status = "✓" if result.success else "✗"

            if result.success:
                passed += 1
            else:
                failed += 1

            readiness.add(result)
            print(f"{status} {result.title:<20} {result.message}")

        print("----------------------------------------")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

        score = ReadinessScore().calculate(readiness)

        print()
        print(f"BuffOS Readiness: {score}%")
