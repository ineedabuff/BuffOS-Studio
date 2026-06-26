from __future__ import annotations

import subprocess

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult


class GrubBtrfsValidator:
    def validate(self, report: AnalysisReport) -> CheckResult:
        analysis = report.get("grub-btrfs")

        if analysis is None or not analysis.success:
            return CheckResult(False, "grub-btrfs", "Not installed")

        enabled = subprocess.run(
            ["systemctl", "is-enabled", "grub-btrfsd.service"],
            capture_output=True,
            text=True,
        )

        if enabled.returncode != 0:
            return CheckResult(False, "grub-btrfs", "Service disabled")

        active = subprocess.run(
            ["systemctl", "is-active", "grub-btrfsd.service"],
            capture_output=True,
            text=True,
        )

        if active.returncode != 0:
            return CheckResult(False, "grub-btrfs", "Service stopped")

        return CheckResult(True, "grub-btrfs", "Valid")
