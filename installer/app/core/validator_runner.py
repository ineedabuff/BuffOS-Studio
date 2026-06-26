from __future__ import annotations

from app.analysis.analysis_report import AnalysisReport
from app.validators.validation_report import ValidationReport


class ValidatorRunner:
    def __init__(self) -> None:
        self._validators = []

    def register(self, validator) -> None:
        self._validators.append(validator)

    def run(self, report: AnalysisReport) -> ValidationReport:
        validation = ValidationReport()

        for validator in self._validators:
            validation.add(validator.validate(report))

        return validation
