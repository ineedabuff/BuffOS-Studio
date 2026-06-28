from __future__ import annotations

import subprocess
from pathlib import Path

from app.install_engine.plan import InstallPlan
from app.install_engine.status import apt_installed, flatpak_installed


def execute_plan(plan: InstallPlan) -> None:
    missing_apt = [package for package in plan.apt if not apt_installed(package)]

    if missing_apt:
        subprocess.run(
            ["sudo", "apt", "install", "-y", *missing_apt],
            check=False,
        )

    for app in plan.flatpak:
        if flatpak_installed(app):
            print(f"✓ {app}")
            continue

        subprocess.run(
            ["flatpak", "install", "-y", "flathub", app],
            check=False,
        )

    for script in plan.scripts:
        subprocess.run(
            ["bash", str(Path("installer/assets/scripts") / script)],
            check=False,
        )
