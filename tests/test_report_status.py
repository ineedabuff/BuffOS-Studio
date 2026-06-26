from app.analysis.result import CheckResult
from app.core.report import Report


def test_report_status_ready():
    report = Report()

    report.add(CheckResult(True, "A", "OK"))
    report.add(CheckResult(True, "B", "OK"))

    assert report.status == "System Ready"


def test_report_status_installation_required():
    report = Report()

    report.add(CheckResult(True, "A", "OK"))
    report.add(CheckResult(False, "B", "FAIL"))

    assert report.status == "Installation Required"
