from unittest.mock import Mock, patch

from app.cli.setup.run import run


def test_default_setup(capsys):
    with (
        patch("builtins.input", return_value=""),
        patch("app.cli.setup.run.run_doctor"),
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

    out = capsys.readouterr().out

    assert "Loading Buff profile" in out
    assert "Install Report" in out
    assert "Setup completed" in out
