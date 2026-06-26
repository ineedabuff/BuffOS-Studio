from __future__ import annotations

from app.installers.base import Installer


class MountOptionsInstaller(Installer):
    def install(self) -> bool:
        return True

    def configure(self) -> bool:
        return True
