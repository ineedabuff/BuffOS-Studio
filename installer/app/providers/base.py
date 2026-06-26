from __future__ import annotations

from typing import Protocol


class PackageProvider(Protocol):
    def install(self, package: str) -> bool: ...
