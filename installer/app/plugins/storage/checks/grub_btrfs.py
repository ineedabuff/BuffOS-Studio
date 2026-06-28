from __future__ import annotations

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class GrubBtrfsCheck(BaseCheck):
    id = "grub_btrfs"
    title = "grub-btrfs"
    category = "storage"

    def __init__(self, provider: SystemProvider | None = None):
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        passed = (
            self.provider.which("grub-btrfs") is not None
            and self.provider.exists("/etc/default/grub-btrfs/config")
            and self.provider.exists("/usr/lib/systemd/system/grub-btrfsd.service")
        )

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
        )
