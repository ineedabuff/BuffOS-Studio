from unittest.mock import Mock, patch

from app.catalog.search import find_by_id
from app.setup.installer import install_selection
from app.setup.selection import Selection


def test_install_selection():
    firefox = find_by_id("firefox")

    assert firefox is not None

    with patch(
        "app.setup.installer.run_plan",
        return_value=Mock(success=True),
    ) as run_plan:
        report = install_selection(Selection([firefox]))

    run_plan.assert_called_once()
    assert report.success
