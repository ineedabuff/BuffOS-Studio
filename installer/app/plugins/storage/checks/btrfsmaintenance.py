from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class BtrfsMaintenanceCheck(BaseCheck):
    id = "btrfsmaintenance"
    title = "btrfsmaintenance"
    category = "storage"

    def __init__(self, provider: SystemProvider | None = None):
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        return CheckResult(
            id=self.id,
            title=self.title,
            passed=self.provider.exists("/etc/default/btrfsmaintenance"),
        )
