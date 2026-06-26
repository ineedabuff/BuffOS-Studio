from __future__ import annotations

from app.installers.base import Installer
from app.providers.fstab import FstabProvider


class MountOptionsInstaller(Installer):
    OPTIONS = (
        "compress=zstd,"
        "noatime,"
        "ssd,"
        "discard=async,"
        "space_cache=v2"
    )

    def __init__(self, fstab: FstabProvider) -> None:
        self.fstab = fstab

    def install(self) -> bool:
        return True

    def configure(self) -> bool:
        content = self.fstab.read()

        updated = content.replace(
            "defaults",
            self.OPTIONS,
        )

        self.fstab.write(updated)

        return True
