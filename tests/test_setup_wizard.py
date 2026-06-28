from unittest.mock import patch

from app.setup.wizard import run


def test_setup_wizard(capsys, tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))

    with (
        patch("builtins.input", side_effect=["1", "", "", "", "", "", ""]),
        patch("app.setup.wizard.install_selection") as install_selection,
    ):
        run()

    out = capsys.readouterr().out
    profile = tmp_path / ".config" / "buff-helper" / "profile.yaml"

    assert "Linux Setup Assistant" in out
    assert "Selection Summary" in out
    assert "✓ Profile saved:" in out
    assert "✓ Installation completed" in out
    assert profile.exists()
    install_selection.assert_called_once()
