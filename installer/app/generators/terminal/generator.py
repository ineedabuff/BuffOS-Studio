from pathlib import Path

ASSETS = Path(__file__).parents[2] / "plugins" / "terminal" / "assets" / "templates"


def generate_zsh(destination: Path) -> None:
    destination.write_text(
        (ASSETS / "buff.zsh.j2").read_text(),
        encoding="utf-8",
    )


def generate_bash(destination: Path) -> None:
    destination.write_text(
        (ASSETS / "buff.bash.j2").read_text(),
        encoding="utf-8",
    )
