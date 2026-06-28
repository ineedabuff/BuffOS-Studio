from app.cli.doctor import command_exists, print_check


def test_command_exists():
    assert command_exists("python")


def test_print_check(capsys):
    print_check("Test", True)

    captured = capsys.readouterr()

    assert "✓ Test" in captured.out
