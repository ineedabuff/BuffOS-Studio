from __future__ import annotations

from app.install_engine.engine import _read_yaml_value
from app.install_engine.plan import InstallPlan
from app.setup.selection import Selection


def create_plan(selection: Selection) -> InstallPlan:
    apt: list[str] = []
    flatpak: list[str] = []
    scripts: list[str] = []

    for entry in selection.entries:
        text = entry.path.read_text(encoding="utf-8")

        apt_package = _read_yaml_value(text, "apt")
        flatpak_app = _read_yaml_value(text, "flatpak")
        script = _read_yaml_value(text, "script")

        if apt_package:
            apt.append(apt_package)

        if flatpak_app:
            flatpak.append(flatpak_app)

        if script:
            scripts.append(script)

    return InstallPlan(
        apt=apt,
        flatpak=flatpak,
        scripts=scripts,
    )
