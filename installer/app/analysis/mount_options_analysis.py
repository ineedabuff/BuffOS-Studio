"""
BuffOS Studio

Mount Options Analysis
"""

from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class MountOptionsAnalysis(Check):
    """Detect mount options for the root filesystem."""

    name = "Mount Options"
    description = "Detect root mount options."

    def run(self) -> CheckResult:
        mounts = Path("/proc/mounts")

        if not mounts.exists():
            return CheckResult(False, self.name, "Unknown")

        for line in mounts.read_text().splitlines():
            parts = line.split()

            if len(parts) < 4:
                continue

            if parts[1] != "/":
                continue

            return CheckResult(
                True,
                self.name,
                parts[3],
            )

        return CheckResult(False, self.name, "Unknown")
