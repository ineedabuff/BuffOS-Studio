from app.setup.wizard import run


def test_setup_wizard(capsys):
    run()

    out = capsys.readouterr().out

    assert "Linux Setup Assistant" in out
    assert "Choose your web browsers" in out
