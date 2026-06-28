from app.checks.renderer import render_check, render_report
from app.checks.result import CheckResult


def test_render_check_passed():
    result = CheckResult(id="steam", title="Steam", passed=True)

    assert render_check(result) == "✓ Steam"


def test_render_check_failed():
    result = CheckResult(id="steam", title="Steam", passed=False)

    assert render_check(result) == "✗ Steam"


def test_render_report_score():
    results = [
        CheckResult(id="steam", title="Steam", passed=True),
        CheckResult(id="portproton", title="PortProton", passed=False),
    ]

    report = render_report(results)

    assert "Buff Ready" in report
    assert "✓ Steam" in report
    assert "✗ PortProton" in report
    assert "Score: 50%" in report
