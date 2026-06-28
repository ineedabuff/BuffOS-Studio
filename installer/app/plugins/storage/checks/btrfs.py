from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class BtrfsCheck(BaseCheck):
    id = "btrfs"
    title = "Btrfs"
    category = "storage"

    def __init__(self, provider: SystemProvider | None = None) -> None:
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(["findmnt", "-no", "FSTYPE", "/"])

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=result.stdout.strip() == "btrfs",
            fixable=self.fixable,
        )
