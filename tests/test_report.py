from app.analysis.result import CheckResult
from app.core.report import Report


def test_report_accepts_results():
    report = Report()

    report.add(CheckResult(True, "A", "OK"))
    report.add(CheckResult(False, "B", "FAIL"))

    assert len(report._results) == 2
