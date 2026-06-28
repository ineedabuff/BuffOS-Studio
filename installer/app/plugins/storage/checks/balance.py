from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class BalanceCheck(BaseCheck):
    id = "balance"
    title = "Btrfs balance"
    category = "storage"

    def __init__(self, provider: SystemProvider | None = None):
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        text = self.provider.read_text("/etc/default/btrfsmaintenance")

        return CheckResult(
            id=self.id,
            title=self.title,
            passed='BTRFS_BALANCE_MOUNTPOINTS="/"' in text,
        )
