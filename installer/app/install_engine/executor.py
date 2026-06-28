from __future__ import annotations

import subprocess
from pathlib import Path

from app.install_engine.plan import InstallPlan


def execute_plan(plan: InstallPlan) -> None:
    if plan.apt:
        subprocess.run(
            ["sudo", "apt", "install", "-y", *plan.apt],
            check=False,
        )

    for app in plan.flatpak:
        subprocess.run(
            ["flatpak", "install", "-y", "flathub", app],
            check=False,
        )

    for script in plan.scripts:
        subprocess.run(
            ["bash", str(Path("installer/assets/scripts") / script)],
            check=False,
        )
