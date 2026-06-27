from __future__ import annotations

from app.analysis.grub_btrfs_analysis import GrubBtrfsAnalysis
from app.analysis.mount_options_analysis import MountOptionsAnalysis
from app.analysis.timeshift_analysis import TimeshiftAnalysis
from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


class SystemPlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(
            manifest=PluginManifest(
                id="system",
                name="System",
                version="0.1.0",
                description="System configuration and maintenance plugin",
            ),
            analyses=[
                MountOptionsAnalysis(),
                TimeshiftAnalysis(),
                GrubBtrfsAnalysis(),
            ],
        )


PLUGIN = SystemPlugin
