from unittest.mock import Mock, patch

from app.cli.setup.run import run


def test_setup_uses_app_selector():
    with (
        patch("builtins.input", return_value=""),
        patch("app.cli.setup.run.run_doctor"),
        patch("app.cli.setup.run.select_profile", return_value="buff"),
        patch("app.cli.setup.run.load_profile"),
        patch("app.cli.setup.run.edit_selection") as edit_selection,
        patch(
            "app.cli.setup.run.install_selection",
            return_value=Mock(installed=[], skipped=[], failed=[]),
        ),
        patch("app.cli.setup.run.render_report", return_value="Install Report"),
    ):
        run()

    edit_selection.assert_called_once()
