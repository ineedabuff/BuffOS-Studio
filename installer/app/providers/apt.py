from __future__ import annotations

import subprocess

from app.providers.base import PackageProvider


class AptProvider(PackageProvider):
    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run

    def install(self, package: str) -> bool:
        if self.dry_run:
            return True

        result = subprocess.run(
            ["sudo", "apt", "install", "-y", package],
            check=False,
        )

        return result.returncode == 0
