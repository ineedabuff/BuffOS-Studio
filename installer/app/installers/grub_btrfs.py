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

    def install(self) -> bool:
        return self.provider.install("grub-btrfs")

    def configure(self) -> bool:
        service = "grub-btrfsd.service"

        if not self.systemd.enable(service):
            return False

        return self.systemd.start(service)
