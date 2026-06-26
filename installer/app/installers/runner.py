from __future__ import annotations

from app.installers.base import Installer


class InstallerRunner:
    def __init__(self) -> None:
        self._installers: list[Installer] = []

    def register(self, installer: Installer) -> None:
        self._installers.append(installer)

    def run(self) -> bool:
        for installer in self._installers:
            if not installer.install():
                return False

            if not installer.configure():
                return False

            if not installer.verify():
                return False

        return True
