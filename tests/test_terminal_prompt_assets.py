from pathlib import Path


def test_terminal_prompt_assets_exist():
    base = Path("installer/app/plugins/terminal/assets")

    assert (base / "prompt.json").exists()
    assert (base / "templates/buff.zsh.j2").exists()
    assert (base / "templates/buff.bash.j2").exists()


def test_terminal_prompt_uses_buff_colors():
    zsh = Path(
        "installer/app/plugins/terminal/assets/templates/buff.zsh.j2"
    ).read_text()

    assert "#FF3131" in zsh
    assert "#DDFF24" in zsh
    assert "#1F51FF" in zsh
    assert "#0FFF50" in zsh
