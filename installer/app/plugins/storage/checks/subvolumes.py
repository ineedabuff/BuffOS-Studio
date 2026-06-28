from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class SubvolumesCheck(BaseCheck):
    id = "btrfs_subvolumes"
    title = "Btrfs subvolumes"
    category = "storage"
    required = ["@", "@home"]

    def __init__(self, provider: SystemProvider | None = None) -> None:
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(["btrfs", "subvolume", "list", "/"])
        passed = all(
            f"path {subvolume}" in result.stdout for subvolume in self.required
        )

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
            fixable=self.fixable,
        )
