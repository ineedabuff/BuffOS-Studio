from __future__ import annotations

from app.installers.base import Installer
from app.providers.base import PackageProvider
from app.providers.systemd import SystemdProvider


class GrubBtrfsInstaller(Installer):
    name = "grub-btrfs"
    description = "Install and configure grub-btrfs."

    def __init__(self, provider: PackageProvider, systemd: SystemdProvider) -> None:
        self.provider = provider
        self.systemd = systemd
        self.installed = False
        self.skipped = False

    def install(self) -> bool:
        self.installed = self.provider.install("grub-btrfs")

        if not self.installed:
            self.skipped = True

        return True

    def configure(self) -> bool:
        if self.skipped:
            return True

        service = "grub-btrfsd.service"

        if not self.systemd.enable(service):
            return False

        return self.systemd.start(service)
