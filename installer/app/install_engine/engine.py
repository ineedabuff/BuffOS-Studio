from __future__ import annotations

import subprocess
from pathlib import Path

from app.catalog.search import find_by_id


def _read_yaml_value(text: str, key: str) -> str:
    lines = text.splitlines()

    for index, line in enumerate(lines):
        if line.strip() == "install:":
            for child in lines[index + 1 :]:
                if child and not child.startswith(" "):
                    break

                stripped = child.strip()
                prefix = f"{key}:"

                if stripped.startswith(prefix):
                    return stripped.replace(prefix, "", 1).strip()

    return ""


class InstallEngine:
    def install(self, app_id: str) -> bool:
        entry = find_by_id(app_id)

        if entry is None:
            print(f"✗ Unknown application: {app_id}")
            return False

        text = entry.path.read_text(encoding="utf-8")

        apt = _read_yaml_value(text, "apt")
        flatpak = _read_yaml_value(text, "flatpak")
        script = _read_yaml_value(text, "script")

        print(f"== Installing {entry.name} ==")

        if flatpak:
            subprocess.run(
                ["flatpak", "install", "-y", "flathub", flatpak],
                check=False,
            )
            return True

        if apt:
            subprocess.run(
                ["sudo", "apt", "install", "-y", apt],
                check=False,
            )
            return True

        if script:
            path = Path("installer/assets/scripts") / script
            subprocess.run(["bash", str(path)], check=False)
            return True

        print(f"✗ No install method for {entry.name}")
        return False
