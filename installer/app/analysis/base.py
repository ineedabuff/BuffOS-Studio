from __future__ import annotations

from abc import ABC, abstractmethod

from app.analysis.result import CheckResult
from app.core.logger import get_logger


class Check(ABC):
    """Base class for every BuffOS system check."""

    name: str = "Unnamed Check"
    description: str = ""

    def __init__(self) -> None:
        self.logger = get_logger(self.name)

    @abstractmethod
    def run(self) -> CheckResult:
        """Execute the check."""
        raise NotImplementedError
