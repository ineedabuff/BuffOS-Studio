from __future__ import annotations

from pathlib import Path

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult


class TimeshiftValidator:
    def validate(self, report: AnalysisReport) -> CheckResult:
        analysis = report.get("Timeshift")

        if analysis is None or not analysis.success:
            return CheckResult(False, "Timeshift", "Not installed")

        config = Path("/etc/timeshift/timeshift.json")

        if not config.exists():
            return CheckResult(False, "Timeshift", "Configuration missing")

        return CheckResult(True, "Timeshift", "Valid")
