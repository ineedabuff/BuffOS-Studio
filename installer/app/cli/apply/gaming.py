from __future__ import annotations

import shutil
import subprocess

APT = [
    "gamemode",
    "mangohud",
    "vkbasalt",
    "goverlay",
]

FLATPAK = [
    "ru.linux_gaming.PortProton",
]


def apt_installed(pkg: str) -> bool:
    return (
        subprocess.run(
            ["dpkg", "-s", pkg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def flatpak_installed(app: str) -> bool:
    return (
        subprocess.run(
            ["flatpak", "info", app],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def run() -> None:
    print("== Buff Helper Gaming ==")

    for pkg in APT:
        if apt_installed(pkg):
            print(f"✓ {pkg}")
            continue

        print(f"Installing {pkg}...")
        subprocess.run(
            ["sudo", "apt", "install", "-y", pkg],
            check=False,
        )

    if shutil.which("flatpak"):
        for app in FLATPAK:
            if flatpak_installed(app):
                print(f"✓ {app}")
                continue

            print(f"Installing {app}...")
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

    print("Gaming profile completed.")
