"""
BuffOS Studio

Firmware Analysis
"""

from __future__ import annotations

from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class FirmwareAnalysis(Check):
    """Detect the current firmware mode."""

    name = "Firmware"
    description = "Detect firmware mode."

    def run(self) -> CheckResult:
        mode = "UEFI" if Path("/sys/firmware/efi").exists() else "BIOS"

        return CheckResult(
            success=True,
            title=self.name,
            message=mode,
        )
