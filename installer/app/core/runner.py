from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.core.logger import get_logger
from app.core.report import Report
from app.core.validator_runner import ValidatorRunner
from app.install.installer_factory import InstallerFactory
from app.install.planner import InstallationPlanner
from app.installers.base import Installer
from app.installers.runner import InstallerRunner
from app.providers.apt import AptProvider
from app.providers.systemd import SystemdProvider
from app.validators.btrfs_layout import BtrfsLayoutValidator
from app.validators.grub_btrfs_validator import GrubBtrfsValidator
from app.validators.mount_options_validator import MountOptionsValidator
from app.validators.timeshift_validator import TimeshiftValidator

logger = get_logger()


class Module(Protocol):
    name: str

    def run(self): ...


class Runner:
    def __init__(
        self,
        factory: InstallerFactory | None = None,
        installer_runner: InstallerRunner | None = None,
        validator_runner: ValidatorRunner | None = None,
    ) -> None:
        self.modules: list[Module] = []
        self.report = Report()
        self.analysis_report = AnalysisReport()
        self.installer_runner = installer_runner or InstallerRunner()
        self.factory = factory or InstallerFactory(
            AptProvider(),
            SystemdProvider(),
        )
        self.validator_runner = validator_runner or self._create_validator_runner()

    def register(self, module: Module) -> None:
        self.modules.append(module)

    def execute(self) -> None:
        logger.info("Starting installation...")

        self._run_modules()

        validation_report = self.validator_runner.run(self.analysis_report)

        planner = InstallationPlanner(self.factory)
        plan = planner.create(validation_report)
        installers = plan.all()

        self._report_planned_fixes(installers)

        for installer in installers:
            self.installer_runner.register(installer)

        installed = self.installer_runner.run()

        self.report.add(
            CheckResult(
                success=installed,
                title="Installation",
                message="Completed" if installed else "Failed",
            )
        )

        final_validation = self.validator_runner.run(self.analysis_report)

        for result in final_validation.all():
            self.report.add(result)

        self.report.summary()

        logger.info("Installation finished.")

    def _run_modules(self) -> None:
        for module in self.modules:
            logger.info(f"Running module: {module.name}")

            try:
                result = module.run()
                self._collect_result(result)
            except Exception as exc:
                logger.exception(f"✗ {module.name} failed: {exc}")
                self.report.add(CheckResult(False, module.name, str(exc)))
                return

    def _collect_result(self, result) -> None:
        if isinstance(result, CheckResult):
            self.analysis_report.add(result)
            return

        if isinstance(result, Iterable):
            for item in result:
                if isinstance(item, CheckResult):
                    self.analysis_report.add(item)
            return

        if isinstance(result, bool) and not result:
            logger.warning("Module returned False")

    def _report_planned_fixes(self, installers: list[Installer]) -> None:
        if not installers:
            self.report.add(CheckResult(True, "Planned Fixes", "None"))
            return

        names = ", ".join(installer.__class__.__name__ for installer in installers)

        self.report.add(CheckResult(True, "Planned Fixes", names))

    def _create_validator_runner(self) -> ValidatorRunner:
        runner = ValidatorRunner()
        runner.register(BtrfsLayoutValidator())
        runner.register(MountOptionsValidator())
        runner.register(TimeshiftValidator())
        runner.register(GrubBtrfsValidator())
        return runner
