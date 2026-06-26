from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.core.logger import get_logger
from app.core.report import Report
from app.core.validator_runner import ValidatorRunner
from app.validators.btrfs_layout import BtrfsLayoutValidator
from app.validators.grub_btrfs_validator import GrubBtrfsValidator
from app.validators.mount_options_validator import MountOptionsValidator
from app.validators.timeshift_validator import TimeshiftValidator

logger = get_logger()


class Module(Protocol):
    name: str

    def run(self): ...


class Runner:
    def __init__(self) -> None:
        self.modules: list[Module] = []
        self.report = Report()
        self.analysis_report = AnalysisReport()
        self.validator_runner = ValidatorRunner()
        self.validator_runner.register(BtrfsLayoutValidator())
        self.validator_runner.register(MountOptionsValidator())
        self.validator_runner.register(TimeshiftValidator())
        self.validator_runner.register(GrubBtrfsValidator())

    def register(self, module: Module) -> None:
        self.modules.append(module)

    def execute(self) -> None:
        logger.info("Starting installation...")

        for module in self.modules:
            logger.info(f"Running module: {module.name}")

            try:
                result = module.run()

                if isinstance(result, CheckResult):
                    self.analysis_report.add(result)

                elif isinstance(result, Iterable):
                    for item in result:
                        if isinstance(item, CheckResult):
                            self.analysis_report.add(item)

                elif isinstance(result, bool):
                    if result:
                        logger.info(f"✓ {module.name} completed")
                    else:
                        logger.warning(f"⚠ {module.name} returned False")

            except Exception as exc:
                logger.exception(f"✗ {module.name} failed: {exc}")
                return

        for result in self.analysis_report.all():
            self.report.add(result)

        validation_report = self.validator_runner.run(self.analysis_report)

        for result in validation_report.all():
            self.report.add(result)

        self.report.summary()

        logger.info("Installation finished.")
