from __future__ import annotations

from app.installers.base import Installer
from app.providers.fstab import FstabProvider


class MountOptionsInstaller(Installer):
    OPTIONS = [
        "compress=zstd",
        "noatime",
        "ssd",
        "discard=async",
        "space_cache=v2",
    ]

    def __init__(self, fstab: FstabProvider) -> None:
        self.fstab = fstab

    def install(self) -> bool:
        return True

    def configure(self) -> bool:
        lines: list[str] = []

        for line in self.fstab.read().splitlines():
            if not line.strip() or line.startswith("#"):
                lines.append(line)
                continue

            parts = line.split()

            if len(parts) < 4 or parts[2] != "btrfs":
                lines.append(line)
                continue

            parts[3] = ",".join(self.OPTIONS)

            lines.append("\t".join(parts))

        self.fstab.write("\n".join(lines) + "\n")

        return True
