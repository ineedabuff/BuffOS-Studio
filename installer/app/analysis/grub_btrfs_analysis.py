from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class GrubBtrfsAnalysis(Check):
    name = "grub-btrfs"
    description = "Detect grub-btrfs."

    def run(self) -> CheckResult:
        installed = (
            Path("/usr/bin/grub-btrfs").exists()
            or Path("/usr/bin/grub-btrfsd").exists()
        )

        return CheckResult(
            success=installed,
            title=self.name,
            message="Installed" if installed else "Not installed",
        )
