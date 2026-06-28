from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InstallPlan:
    apt: list[str]
    flatpak: list[str]
    scripts: list[str]
