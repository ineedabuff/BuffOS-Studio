from app.checks.base import BaseCheck
from app.checks.result import CheckResult


class DemoCheck(BaseCheck):
    id = "demo"
    title = "Demo"
    category = "test"

    def run(self) -> CheckResult:
        return CheckResult(
            id=self.id,
            title=self.title,
            passed=True,
        )


def test_base_check():
    check = DemoCheck()

    assert check.id == "demo"
    assert check.title == "Demo"
    assert check.category == "test"
    assert check.weight == 1
    assert check.fixable is False
    assert check.run().passed
