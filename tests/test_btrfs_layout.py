from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.validators.btrfs_layout import BtrfsLayoutValidator


def test_btrfs_layout_valid():
    report = AnalysisReport()

    report.add(CheckResult(True, "Filesystem", "btrfs"))
    report.add(CheckResult(True, "Root Subvolume", "/@"))
    report.add(CheckResult(True, "Home Subvolume", "/@home"))

    result = BtrfsLayoutValidator().validate(report)

    assert result.success is True
    assert result.message == "Valid"
