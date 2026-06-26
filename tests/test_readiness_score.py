from app.analysis.result import CheckResult
from app.validators.readiness_score import ReadinessScore
from app.validators.validation_report import ValidationReport


def test_readiness_score():
    report = ValidationReport()

    report.add(CheckResult(True, "A", "OK"))
    report.add(CheckResult(True, "B", "OK"))
    report.add(CheckResult(False, "C", "KO"))
    report.add(CheckResult(True, "D", "OK"))

    score = ReadinessScore().calculate(report)

    assert score == 75
