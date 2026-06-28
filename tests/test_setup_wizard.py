from unittest.mock import patch

from app.setup.wizard import run


def test_setup_wizard(capsys, tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))

    with patch("builtins.input", side_effect=["", "", "", "", "", "", ""]):
        run()

    out = capsys.readouterr().out
    profile = tmp_path / ".config" / "buff-helper" / "profile.yaml"

    assert "Linux Setup Assistant" in out
    assert "Selection Summary" in out
    assert "✓ Profile saved:" in out
    assert profile.exists()
