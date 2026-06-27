from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.plugins.manifest import PluginManifest


@dataclass(slots=True)
class Plugin:
    manifest: PluginManifest
    analyses: list[Any] = field(default_factory=list)
    validators: list[Any] = field(default_factory=list)
    installers: list[Any] = field(default_factory=list)
    commands: list[Any] = field(default_factory=list)
    learn_topics: list[Any] = field(default_factory=list)

    @property
    def id(self) -> str:
        return self.manifest.id

    @property
    def name(self) -> str:
        return self.manifest.name

    @property
    def description(self) -> str:
        return self.manifest.description

    @property
    def version(self) -> str:
        return self.manifest.version

    @property
    def author(self) -> str:
        return self.manifest.author

    @property
    def license(self) -> str:
        return self.manifest.license

    @property
    def homepage(self) -> str:
        return self.manifest.homepage

    @property
    def enabled(self) -> bool:
        return self.manifest.enabled
