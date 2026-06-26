from __future__ import annotations

from app.providers.base import PackageProvider


class FakeAptProvider(PackageProvider):
    def __init__(self) -> None:
        self.installed: list[str] = []

    def install(self, package: str) -> bool:
        self.installed.append(package)
        return True
