from app.analysis.result import CheckResult
from app.core.report import Report


def test_report_summary(capsys):
    report = Report()

    report.add(CheckResult(True, "Timeshift", "Valid"))
    report.add(CheckResult(False, "grub-btrfs", "Missing"))

    report.summary()

    out = capsys.readouterr().out

    assert "BuffOS Readiness:" in out
    assert "Passed: 1" in out
    assert "Failed: 1" in out
