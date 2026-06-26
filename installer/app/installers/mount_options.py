from __future__ import annotations

from app.installers.base import Installer
from app.providers.fstab import FstabProvider


class MountOptionsInstaller(Installer):
    def __init__(self, fstab: FstabProvider) -> None:
        self.fstab = fstab

    def install(self) -> bool:
        return True

    def configure(self) -> bool:
        content = self.fstab.read()
        self.fstab.write(content)
        return True
