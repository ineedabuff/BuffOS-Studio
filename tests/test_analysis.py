from app.analysis.operating_system_analysis import OperatingSystemAnalysis
from app.analysis.filesystem import FilesystemAnalysis
from app.analysis.firmware_analysis import FirmwareAnalysis
from app.analysis.secure_boot_analysis import SecureBootAnalysis
from app.analysis.timeshift_analysis import TimeshiftAnalysis
from app.analysis.grub_btrfs_analysis import GrubBtrfsAnalysis


def test_operating_system():
    result = OperatingSystemAnalysis().run()
    assert result.title == "Operating System"


def test_filesystem():
    result = FilesystemAnalysis().run()
    assert result.title == "Filesystem"


def test_firmware():
    result = FirmwareAnalysis().run()
    assert result.title == "Firmware"


def test_secure_boot():
    result = SecureBootAnalysis().run()
    assert result.title == "Secure Boot"


def test_timeshift():
    result = TimeshiftAnalysis().run()
    assert result.title == "Timeshift"


def test_grub_btrfs():
    result = GrubBtrfsAnalysis().run()
    assert result.title == "grub-btrfs"
