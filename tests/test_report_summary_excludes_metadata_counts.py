from app.analysis.result import CheckResult
from app.core.report import Report


def test_report_summary_excludes_metadata_from_counts(capsys):
    report = Report()

    report.add(CheckResult(False, "Planned Fixes", "GrubBtrfsInstaller"))
    report.add(CheckResult(True, "Btrfs Layout", "Valid"))
    report.add(CheckResult(True, "Mount Options", "Valid"))
    report.add(CheckResult(True, "Timeshift", "Valid"))
    report.add(CheckResult(False, "grub-btrfs", "Missing"))

    report.summary()

    out = capsys.readouterr().out

    assert "Passed: 3" in out
    assert "Failed: 1" in out
    assert "BuffOS Readiness: 75%" in out
