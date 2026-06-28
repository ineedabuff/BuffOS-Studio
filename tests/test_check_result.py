from app.checks.result import CheckResult


def test_check_result():
    result = CheckResult(
        id="steam",
        title="Steam",
        passed=True,
    )

    assert result.id == "steam"
    assert result.title == "Steam"
    assert result.passed is True
    assert result.fixable is False
