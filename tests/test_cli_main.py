from unittest.mock import patch

from app.cli.main import main


def test_analyze_command():
    with (
        patch("sys.argv", ["buffos", "analyze"]),
        patch("app.cli.main.create_runner") as create_runner,
    ):
        main()

        create_runner.assert_called_once_with(dry_run=True)
        create_runner.return_value.execute.assert_called_once()


def test_apply_command():
    with (
        patch("sys.argv", ["buffos", "apply"]),
        patch("app.cli.main.create_runner") as create_runner,
    ):
        main()

        create_runner.assert_called_once_with()
        create_runner.return_value.execute.assert_called_once()
