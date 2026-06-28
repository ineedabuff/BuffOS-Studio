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


class SubvolumesCheck(BaseCheck):
    id = "btrfs_subvolumes"
    title = "Btrfs subvolumes"
    category = "storage"
    required = ["@", "@home"]

    def __init__(self, provider: CommandProvider | None = None) -> None:
        self.provider = provider or SubprocessProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(
            ["btrfs", "subvolume", "list", "/"],
            check=False,
        )

        found = result.stdout
        passed = all(f"path {subvolume}" in found for subvolume in self.required)

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
            fixable=self.fixable,
        )
