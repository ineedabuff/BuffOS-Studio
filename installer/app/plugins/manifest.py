from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PluginManifest:
    id: str
    name: str
    version: str
    description: str
    author: str = "Buff Helper Project"
    license: str = "MIT"
    homepage: str = "https://github.com/ineedabuff/BuffOS-Studio"
    enabled: bool = True
