"""
BuffOS Studio

Btrfs Layout Validator
"""

from __future__ import annotations

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult


class BtrfsLayoutValidator:
    """Validate the expected BuffOS Btrfs layout."""

    def validate(self, report: AnalysisReport) -> CheckResult:
        filesystem = report.get("Filesystem")
        root = report.get("Root Subvolume")
        home = report.get("Home Subvolume")

        valid = (
            filesystem is not None
            and filesystem.message == "btrfs"
            and root is not None
            and root.message == "/@"
            and home is not None
            and home.message == "/@home"
        )

        return CheckResult(
            success=valid,
            title="Btrfs Layout",
            message="Valid" if valid else "Invalid",
        )
