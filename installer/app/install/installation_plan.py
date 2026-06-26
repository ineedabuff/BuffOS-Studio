from __future__ import annotations

from app.installers.base import Installer


class InstallationPlan:
    def __init__(self) -> None:
        self._installers: list[Installer] = []

    def add(self, installer: Installer) -> None:
        self._installers.append(installer)

    def all(self) -> list[Installer]:
        return self._installers
