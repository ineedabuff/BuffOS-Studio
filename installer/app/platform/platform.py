from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Platform:
    name: str
    version: str
    family: str
    package_manager: str
    supported: bool

    @property
    def identifier(self) -> str:
        return f"{self.name} {self.version}"
