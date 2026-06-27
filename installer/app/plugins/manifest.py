from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PluginManifest:
    name: str
    version: str
    description: str
    enabled: bool = True
