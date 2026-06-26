from __future__ import annotations

from app.installers.grub_btrfs import GrubBtrfsInstaller
from app.installers.timeshift import TimeshiftInstaller
from app.providers.base import PackageProvider
from app.providers.systemd import SystemdProvider


class InstallerFactory:
    def __init__(
        self,
        package_provider: PackageProvider,
        systemd_provider: SystemdProvider,
    ) -> None:
        self.package_provider = package_provider
        self.systemd_provider = systemd_provider

    def timeshift(self) -> TimeshiftInstaller:
        return TimeshiftInstaller(self.package_provider)

    def grub_btrfs(self) -> GrubBtrfsInstaller:
        return GrubBtrfsInstaller(
            self.package_provider,
            self.systemd_provider,
        )
