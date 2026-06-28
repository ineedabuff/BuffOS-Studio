from __future__ import annotations

import subprocess

from app.profile.loader import load


def install_apt() -> None:
    packages = load("apt")

    if packages:
        subprocess.run(
            [
                "sudo",
                "apt",
                "install",
                "-y",
                *packages,
            ],
            check=False,
        )


def install_flatpak() -> None:
    for app in load("flatpak"):
        subprocess.run(
            [
                "flatpak",
                "install",
                "-y",
                "flathub",
                app,
            ],
            check=False,
        )


def enable_systemd() -> None:
    for service in load("systemd"):
        subprocess.run(
            [
                "sudo",
                "systemctl",
                "enable",
                "--now",
                service,
            ],
            check=False,
        )


def run() -> None:
    install_apt()
    install_flatpak()
    enable_systemd()
