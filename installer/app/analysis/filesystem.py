"""
BuffOS Studio

Filesystem Analysis
"""

from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class FilesystemAnalysis(Check):
    """Detect the root filesystem."""

    name = "Filesystem"
    description = "Detect root filesystem."

    def run(self) -> CheckResult:
        filesystem = self.detect_root_filesystem()

        return CheckResult(
            success=True,
            title=self.name,
            message=filesystem,
        )

    @staticmethod
    def detect_root_filesystem() -> str:
        mounts = Path("/proc/mounts")

        if not mounts.exists():
            return "Unknown"

        for line in mounts.read_text().splitlines():
            parts = line.split()

            if len(parts) >= 3 and parts[1] == "/":
                return parts[2]

        return "Unknown"
