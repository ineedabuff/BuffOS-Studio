from unittest.mock import Mock, patch

from app.cli.setup.run import run


def test_setup_uses_profile_selector():
    with (
        patch("builtins.input", return_value=""),
        patch("app.cli.setup.run.run_doctor"),
        patch("app.cli.setup.run.select_profile", return_value="buff"),
        patch("app.cli.setup.run.load_profile"),
        patch(
            "app.cli.setup.run.install_selection",
            return_value=Mock(
                installed=[],
                skipped=[],
                failed=[],
            ),
        ),
        patch(
            "app.cli.setup.run.render_report",
            return_value="Install Report",
        ),
    ):
        run()
