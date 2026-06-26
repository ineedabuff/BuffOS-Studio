from __future__ import annotations

from app.install.installation_plan import InstallationPlan
from app.install.installer_factory import InstallerFactory
from app.validators.validation_report import ValidationReport


class InstallationPlanner:
    def __init__(self, factory: InstallerFactory) -> None:
        self.factory = factory

    def create(self, report: ValidationReport) -> InstallationPlan:
        plan = InstallationPlan()

        timeshift = report.get("Timeshift")
        if timeshift is None or timeshift.failed:
            plan.add(self.factory.timeshift())

        grub_btrfs = report.get("grub-btrfs")
        if grub_btrfs is None or grub_btrfs.failed:
            plan.add(self.factory.grub_btrfs())

        return plan
