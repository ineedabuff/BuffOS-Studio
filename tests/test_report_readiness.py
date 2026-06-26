from app.analysis.result import CheckResult
from app.core.report import Report


def test_report_readiness():
    report = Report()

    report.add(CheckResult(True, "A", "OK"))
    report.add(CheckResult(True, "B", "OK"))
    report.add(CheckResult(False, "C", "FAIL"))
    report.add(CheckResult(False, "D", "FAIL"))

    assert report.readiness == 50
