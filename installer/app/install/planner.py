from __future__ import annotations

from app.install.installation_plan import InstallationPlan
from app.installers.grub_btrfs import GrubBtrfsInstaller
from app.installers.timeshift import TimeshiftInstaller
from app.providers.base import PackageProvider
from app.validators.validation_report import ValidationReport


class InstallationPlanner:
    def __init__(self, provider: PackageProvider) -> None:
        self.provider = provider

    def create(self, report: ValidationReport) -> InstallationPlan:
        plan = InstallationPlan()

        timeshift = report.get("Timeshift")
        if timeshift is None or timeshift.failed:
            plan.add(TimeshiftInstaller(self.provider))

        grub_btrfs = report.get("grub-btrfs")
        if grub_btrfs is None or grub_btrfs.failed:
            plan.add(GrubBtrfsInstaller(self.provider))

        return plan
