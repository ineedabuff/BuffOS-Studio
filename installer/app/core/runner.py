from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from app.analysis.result import CheckResult
from app.core.logger import get_logger
from app.core.report import Report


logger = get_logger()


class Module(Protocol):
    name: str

    def run(self):
        ...


class Runner:
    """Executes registered modules."""

    def __init__(self) -> None:
        self.modules: list[Module] = []
        self.report = Report()

    def register(self, module: Module) -> None:
        self.modules.append(module)

    def execute(self) -> None:
        logger.info("Starting installation...")

        for module in self.modules:
            logger.info(f"Running module: {module.name}")

            try:
                result = module.run()

                if isinstance(result, CheckResult):
                    self.report.add(result)

                elif isinstance(result, Iterable):
                    for item in result:
                        if isinstance(item, CheckResult):
                            self.report.add(item)

                elif isinstance(result, bool):
                    if result:
                        logger.info(f"✓ {module.name} completed")
                    else:
                        logger.warning(f"⚠ {module.name} returned False")

            except Exception as exc:
                logger.exception(f"✗ {module.name} failed: {exc}")
                return

        self.report.summary()

        logger.info("Installation finished.")
