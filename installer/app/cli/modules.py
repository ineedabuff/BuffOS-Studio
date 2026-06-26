from __future__ import annotations

from app.analysis.filesystem import FilesystemAnalysis
from app.analysis.firmware_analysis import FirmwareAnalysis
from app.analysis.grub_btrfs_analysis import GrubBtrfsAnalysis
from app.analysis.home_subvolume_analysis import HomeSubvolumeAnalysis
from app.analysis.mount_options_analysis import MountOptionsAnalysis
from app.analysis.operating_system_analysis import OperatingSystemAnalysis
from app.analysis.root_subvolume_analysis import RootSubvolumeAnalysis
from app.analysis.secure_boot_analysis import SecureBootAnalysis
from app.analysis.timeshift_analysis import TimeshiftAnalysis
from app.core.runner import Runner


def create_runner(dry_run: bool = False) -> Runner:
    runner = Runner(dry_run=dry_run)

    runner.register(OperatingSystemAnalysis())
    runner.register(FirmwareAnalysis())
    runner.register(SecureBootAnalysis())
    runner.register(FilesystemAnalysis())
    runner.register(RootSubvolumeAnalysis())
    runner.register(HomeSubvolumeAnalysis())
    runner.register(MountOptionsAnalysis())
    runner.register(TimeshiftAnalysis())
    runner.register(GrubBtrfsAnalysis())

    return runner
