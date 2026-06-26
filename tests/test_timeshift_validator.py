from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.validators.timeshift_validator import TimeshiftValidator


def test_timeshift_validator():
    report = AnalysisReport()
    report.add(CheckResult(True, "Timeshift", "Installed"))

    result = TimeshiftValidator().validate(report)

    assert result.success is True
    assert result.message == "Valid"
