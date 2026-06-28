from __future__ import annotations

import subprocess
from typing import Protocol

from app.checks.base import BaseCheck
from app.checks.result import CheckResult


class CommandResult(Protocol):
    stdout: str


class CommandProvider(Protocol):
    def run(self, command: list[str], *, check: bool = False) -> CommandResult: ...


class SubprocessProvider:
    def run(
        self,
        command: list[str],
        *,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            command,
            check=check,
            capture_output=True,
            text=True,
        )


class MountOptionsCheck(BaseCheck):
    id = "btrfs_mount_options"
    title = "Btrfs mount options"
    category = "storage"
    required = ["noatime", "compress=zstd", "ssd"]

    def __init__(self, provider: CommandProvider | None = None) -> None:
        self.provider = provider or SubprocessProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(
            ["findmnt", "-no", "OPTIONS", "/"],
            check=False,
        )

        options = result.stdout.strip()
        passed = all(option in options for option in self.required)

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
            fixable=self.fixable,
        )
