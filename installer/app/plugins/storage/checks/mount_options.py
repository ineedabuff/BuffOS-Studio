from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class MountOptionsCheck(BaseCheck):
    id = "btrfs_mount_options"
    title = "Btrfs mount options"
    category = "storage"
    required = ["noatime", "compress=zstd", "ssd"]

    def __init__(self, provider: SystemProvider | None = None) -> None:
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(["findmnt", "-no", "OPTIONS", "/"])
        options = result.stdout.strip()
        passed = all(option in options for option in self.required)

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
            fixable=self.fixable,
        )
