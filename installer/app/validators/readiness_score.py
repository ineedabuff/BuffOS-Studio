from __future__ import annotations

from app.validators.validation_report import ValidationReport


class ReadinessScore:
    def calculate(self, report: ValidationReport) -> int:
        total = len(report.all())

        if total == 0:
            return 0

        return round((report.passed / total) * 100)
