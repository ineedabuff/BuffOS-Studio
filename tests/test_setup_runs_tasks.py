from unittest.mock import Mock, patch

from app.cli.setup.run import run


def test_setup_runs_profile_tasks():
    with (
        patch("builtins.input", return_value=""),
        patch("app.cli.setup.run.run_doctor"),
        patch("app.cli.setup.run.select_profile", return_value="buff"),
        patch("app.cli.setup.run.load_profile"),
        patch("app.cli.setup.run.edit_selection"),
        patch("app.cli.setup.run.run_profile_tasks") as run_profile_tasks,
        patch(
            "app.cli.setup.run.install_selection",
            return_value=Mock(installed=[], skipped=[], failed=[]),
        ),
        patch("app.cli.setup.run.render_report", return_value="Install Report"),
    ):
        run()

    run_profile_tasks.assert_called_once_with("buff")
