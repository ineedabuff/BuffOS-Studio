from unittest.mock import patch

from app.catalog.search import find_by_id
from app.install_engine.plan_runner import run_plan
from app.setup.selection import Selection


def test_run_plan():
    firefox = find_by_id("firefox")

    assert firefox is not None

    with patch("app.install_engine.plan_runner.execute_plan") as execute_plan:
        run_plan(Selection([firefox]))

    execute_plan.assert_called_once()
