from __future__ import annotations

from app.installers.base import Installer
from app.providers.base import PackageProvider


class GrubBtrfsInstaller(Installer):
    name = "grub-btrfs"
    description = "Install and configure grub-btrfs."

    def __init__(self, provider: PackageProvider) -> None:
        self.provider = provider

    def install(self) -> bool:
        return self.provider.install("grub-btrfs")

    def configure(self) -> bool:
        return True

    def verify(self) -> bool:
        return True
