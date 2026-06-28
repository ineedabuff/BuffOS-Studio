from __future__ import annotations

import subprocess
from typing import Protocol

from app.checks.result import CheckResult


class CommandResult(Protocol):
    stdout: str


class CommandProvider(Protocol):
    def run(self, command: list[str], *, check: bool = False) -> CommandResult: ...


class SubprocessProvider:
    def run(
        self, command: list[str], *, check: bool = False
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            command,
            check=check,
            capture_output=True,
            text=True,
        )


class BtrfsCheck:
    def __init__(self, provider: CommandProvider | None = None) -> None:
        self.provider = provider or SubprocessProvider()

    def run(self) -> CheckResult:
        result = self.provider.run(
            ["findmnt", "-no", "FSTYPE", "/"],
            check=False,
        )

        return CheckResult(
            id="btrfs",
            title="Btrfs",
            passed=result.stdout.strip() == "btrfs",
            fixable=False,
        )
