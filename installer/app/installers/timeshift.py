from __future__ import annotations

from app.installers.base import Installer
from app.providers.apt import AptProvider


class TimeshiftInstaller(Installer):
    name = "Timeshift"
    description = "Install and configure Timeshift."

    def __init__(self, apt: AptProvider) -> None:
        self.apt = apt

    def install(self) -> bool:
        return self.apt.install("timeshift")

    def configure(self) -> bool:
        return True

    def verify(self) -> bool:
        return True
