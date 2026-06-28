from pathlib import Path

ROOT = Path("installer/assets/scripts")


def test_buff_terminal_scripts_exist():
    for script in [
        "install-buff-term.sh",
        "install-buff-zsh.sh",
        "install-buff-extras.sh",
    ]:
        path = ROOT / script

        assert path.exists()
        assert path.read_text(encoding="utf-8").startswith("#!/usr/bin/env bash")


def test_buff_profile_postinstall_uses_assets_scripts():
    text = Path("installer/app/profiles/buff/postinstall.txt").read_text(
        encoding="utf-8"
    )

    assert "assets/scripts/install-buff-term.sh" in text
    assert "assets/scripts/install-buff-zsh.sh" in text
    assert "assets/scripts/install-buff-extras.sh" in text
