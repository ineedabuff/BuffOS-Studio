from __future__ import annotations

from abc import ABC, abstractmethod


class Installer(ABC):
    name: str
    description: str

    @abstractmethod
    def install(self) -> bool:
        pass

    @abstractmethod
    def configure(self) -> bool:
        pass
