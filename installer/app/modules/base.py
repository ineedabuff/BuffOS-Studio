from __future__ import annotations

from abc import ABC, abstractmethod


class Module(ABC):
    """Base class for every BuffOS module."""

    name: str = "Unnamed Module"
    description: str = ""

    @abstractmethod
    def run(self) -> bool:
        """Execute the module."""
        raise NotImplementedError
