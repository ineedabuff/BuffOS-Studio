from app.analysis.result import CheckResult
from app.core.report import Report


def test_planned_fixes_do_not_affect_readiness():
    report = Report()

    report.add(CheckResult(False, "Planned Fixes", "GrubBtrfsInstaller"))
    report.add(CheckResult(True, "Btrfs Layout", "Valid"))
    report.add(CheckResult(True, "Mount Options", "Valid"))
    report.add(CheckResult(True, "Timeshift", "Valid"))
    report.add(CheckResult(False, "grub-btrfs", "Missing"))

    assert report.readiness == 75
