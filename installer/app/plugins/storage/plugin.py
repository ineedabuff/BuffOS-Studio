from __future__ import annotations

from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


class StoragePlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(
            manifest=PluginManifest(
                id="storage",
                name="Storage",
                version="0.1.0",
                description="Storage health checks",
            ),
        )


PLUGIN = StoragePlugin
