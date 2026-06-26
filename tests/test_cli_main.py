from unittest.mock import patch

from app.cli.main import main


def test_analyze_command():
    with (
        patch("sys.argv", ["buffos", "analyze"]),
        patch("app.cli.main.Runner") as runner,
    ):
        main()

        runner.assert_called_once_with(dry_run=True)
        runner.return_value.execute.assert_called_once()


def test_apply_command():
    with (
        patch("sys.argv", ["buffos", "apply"]),
        patch("app.cli.main.Runner") as runner,
    ):
        main()

        runner.assert_called_once_with()
        runner.return_value.execute.assert_called_once()
