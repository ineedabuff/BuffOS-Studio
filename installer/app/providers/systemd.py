from __future__ import annotations

import subprocess


class SystemdProvider:
    def is_enabled(self, service: str) -> bool:
        result = subprocess.run(
            ["systemctl", "is-enabled", service],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0

    def is_active(self, service: str) -> bool:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0

    def enable(self, service: str) -> bool:
        result = subprocess.run(
            ["sudo", "systemctl", "enable", service],
            check=False,
        )
        return result.returncode == 0

    def start(self, service: str) -> bool:
        result = subprocess.run(
            ["sudo", "systemctl", "start", service],
            check=False,
        )
        return result.returncode == 0
