from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.validators.timeshift_validator import TimeshiftValidator


def test_timeshift_validator_not_installed():
    report = AnalysisReport()
    report.add(CheckResult(False, "Timeshift", "Not installed"))

    result = TimeshiftValidator().validate(report)

    assert result.success is False
    assert result.message == "Not installed"
