"""
BuffOS Studio

Root Subvolume Analysis
"""

from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class RootSubvolumeAnalysis(Check):
    """Detect the root Btrfs subvolume."""

    name = "Root Subvolume"
    description = "Detect the active root subvolume."

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

            options = parts[3].split(",")

            for option in options:
                if option.startswith("subvol="):
                    return CheckResult(
                        True,
                        self.name,
                        option.removeprefix("subvol="),
                    )

        return CheckResult(False, self.name, "Not detected")
