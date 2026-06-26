"""
BuffOS Studio

Timeshift Analysis
"""

from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class TimeshiftAnalysis(Check):
    """Detect Timeshift installation."""

    name = "Timeshift"
    description = "Detect Timeshift."

    def run(self) -> CheckResult:
        installed = (
            Path("/usr/bin/timeshift").exists() or Path("/usr/sbin/timeshift").exists()
        )

        return CheckResult(
            success=installed,
            title=self.name,
            message="Installed" if installed else "Not installed",
        )
