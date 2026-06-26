from __future__ import annotations

from app.installers.base import Installer


class TimeshiftInstaller(Installer):
    name = "Timeshift"
    description = "Install and configure Timeshift."

    def install(self) -> bool:
        print("[Install] Timeshift")
        return True

    def configure(self) -> bool:
        print("[Configure] Timeshift")
        return True

    def verify(self) -> bool:
        print("[Verify] Timeshift")
        return True
