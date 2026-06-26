from __future__ import annotations

from app.installers.base import Installer
from app.providers.base import PackageProvider


class TimeshiftInstaller(Installer):
    name = "Timeshift"
    description = "Install and configure Timeshift."

    def __init__(self, provider: PackageProvider) -> None:
        self.provider = provider

    def install(self) -> bool:
        return self.provider.install("timeshift")

    def configure(self) -> bool:
        return True
