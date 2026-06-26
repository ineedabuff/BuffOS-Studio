from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.validators.grub_btrfs_validator import GrubBtrfsValidator


def test_grub_btrfs_validator_not_installed():
    report = AnalysisReport()
    report.add(CheckResult(False, "grub-btrfs", "Not installed"))

    result = GrubBtrfsValidator().validate(report)

    assert result.success is False
    assert result.message == "Not installed"
