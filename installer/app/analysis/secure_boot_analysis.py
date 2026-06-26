"""
BuffOS Studio

Secure Boot Analysis
"""

from __future__ import annotations

import subprocess

from app.analysis.base import Check
from app.analysis.result import CheckResult


class SecureBootAnalysis(Check):
    """Detect Secure Boot status."""

    name = "Secure Boot"
    description = "Detect Secure Boot state."

    def run(self) -> CheckResult:
        try:
            result = subprocess.run(
                ["mokutil", "--sb-state"],
                capture_output=True,
                text=True,
                check=False,
            )

            output = result.stdout.strip().lower()

            if "enabled" in output:
                return CheckResult(True, self.name, "Enabled")

            if "disabled" in output:
                return CheckResult(True, self.name, "Disabled")

            return CheckResult(False, self.name, "Unknown")

        except FileNotFoundError:
            return CheckResult(False, self.name, "mokutil not installed")
