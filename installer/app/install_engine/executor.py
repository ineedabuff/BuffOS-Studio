from __future__ import annotations

import subprocess
from pathlib import Path

from app.install_engine.plan import InstallPlan
from app.install_engine.report import InstallReport
from app.install_engine.status import apt_installed, flatpak_installed


def execute_plan(plan: InstallPlan) -> InstallReport:
    installed: list[str] = []
    skipped: list[str] = []
    failed: list[str] = []

    missing_apt = [package for package in plan.apt if not apt_installed(package)]

    skipped.extend(package for package in plan.apt if apt_installed(package))

    if missing_apt:
        result = subprocess.run(
            ["sudo", "apt", "install", "-y", *missing_apt],
            check=False,
        )

        if result.returncode == 0:
            installed.extend(missing_apt)
        else:
            failed.extend(missing_apt)

    for app in plan.flatpak:
        if flatpak_installed(app):
            print(f"✓ {app}")
            skipped.append(app)
            continue

        result = subprocess.run(
            ["flatpak", "install", "-y", "flathub", app],
            check=False,
        )

        if result.returncode == 0:
            installed.append(app)
        else:
            failed.append(app)

    for script in plan.scripts:
        result = subprocess.run(
            ["bash", str(Path("installer/assets/scripts") / script)],
            check=False,
        )

        if result.returncode == 0:
            installed.append(script)
        else:
            failed.append(script)

    return InstallReport(
        installed=installed,
        skipped=skipped,
        failed=failed,
    )
