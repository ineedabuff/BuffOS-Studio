from __future__ import annotations

from typing import Protocol

from app.analysis.result import CheckResult
from app.core.logger import get_logger


logger = get_logger()


class Module(Protocol):
    name: str

    def run(self) -> bool | CheckResult:
        ...


class Runner:
    def __init__(self) -> None:
        self.modules: list[Module] = []

    def register(self, module: Module) -> None:
        self.modules.append(module)

    def execute(self) -> None:
        logger.info("Starting installation...")

        for module in self.modules:
            logger.info(f"Running module: {module.name}")

            try:
                result = module.run()

                if isinstance(result, CheckResult):
                    if result.success:
                        logger.info(f"✓ {result.title}: {result.message}")
                    else:
                        logger.warning(f"✗ {result.title}: {result.message}")
                    continue

                if result:
                    logger.info(f"✓ {module.name} completed")
                else:
                    logger.warning(f"⚠ {module.name} returned False")

            except Exception as exc:
                logger.exception(f"✗ {module.name} failed: {exc}")
                break

        logger.info("Installation finished.")
