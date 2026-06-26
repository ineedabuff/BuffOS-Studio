from __future__ import annotations

from abc import ABC, abstractmethod

from app.core.logger import get_logger


class Module(ABC):
    """Base class for every BuffOS module."""

    name: str = "Unnamed Module"
    description: str = ""

    def __init__(self) -> None:
        self.logger = get_logger(self.name)

    @abstractmethod
    def run(self) -> bool:
        """Execute the module."""
        raise NotImplementedError
