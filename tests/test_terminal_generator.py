from pathlib import Path

from app.generators.terminal.generator import (
    generate_bash,
    generate_zsh,
)


def test_generate_terminal(tmp_path: Path):
    bash = tmp_path / ".bashrc"
    zsh = tmp_path / ".zshrc"

    generate_bash(bash)
    generate_zsh(zsh)

    assert bash.exists()
    assert zsh.exists()

    assert "Buff Prompt" in bash.read_text()
    assert "Buff Prompt" in zsh.read_text()
