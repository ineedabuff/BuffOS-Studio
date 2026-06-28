from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class FstrimCheck(BaseCheck):
    id = "fstrim"
    title = "Periodic TRIM"
    category = "storage"

    def __init__(self, provider: SystemProvider | None = None):
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(
            ["systemctl", "is-enabled", "fstrim.timer"],
        )

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=result.stdout.strip() == "enabled",
        )
