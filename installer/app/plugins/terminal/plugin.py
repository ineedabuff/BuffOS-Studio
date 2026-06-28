from __future__ import annotations

from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


class TerminalPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(
            manifest=PluginManifest(
                id="terminal",
                name="Terminal",
                version="0.1.0",
                description="Buff terminal and shell customization plugin",
            ),
        )


PLUGIN = TerminalPlugin
