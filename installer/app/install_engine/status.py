from __future__ import annotations

import shutil
import subprocess


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def apt_installed(package: str) -> bool:
    return (
        subprocess.run(
            ["dpkg", "-s", package],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def flatpak_installed(app_id: str) -> bool:
    return (
        subprocess.run(
            ["flatpak", "info", app_id],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )
