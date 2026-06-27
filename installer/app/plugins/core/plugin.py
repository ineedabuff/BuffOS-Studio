from __future__ import annotations

from app.analysis.filesystem import FilesystemAnalysis
from app.analysis.firmware_analysis import FirmwareAnalysis
from app.analysis.home_subvolume_analysis import HomeSubvolumeAnalysis
from app.analysis.operating_system_analysis import OperatingSystemAnalysis
from app.analysis.root_subvolume_analysis import RootSubvolumeAnalysis
from app.analysis.secure_boot_analysis import SecureBootAnalysis
from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin
from app.validators.btrfs_layout import BtrfsLayoutValidator


class CorePlugin(Plugin):
    def __init__(self) -> None:
        super().__init__(
            manifest=PluginManifest(
                id="core",
                name="Core",
                version="1.0.0",
                description="Core Buff Helper plugin",
            ),
            analyses=[
                OperatingSystemAnalysis(),
                FirmwareAnalysis(),
                SecureBootAnalysis(),
                FilesystemAnalysis(),
                RootSubvolumeAnalysis(),
                HomeSubvolumeAnalysis(),
            ],
            validators=[
                BtrfsLayoutValidator(),
            ],
        )


PLUGIN = CorePlugin
