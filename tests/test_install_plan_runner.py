from unittest.mock import Mock, patch

from app.catalog.search import find_by_id
from app.install_engine.plan_runner import run_plan
from app.setup.selection import Selection


def test_run_plan():
    firefox = find_by_id("firefox")

    assert firefox is not None

    with patch(
        "app.install_engine.plan_runner.execute_plan",
        return_value=Mock(success=True),
    ) as execute_plan:
        report = run_plan(Selection([firefox]))

    execute_plan.assert_called_once()
    assert report.success
