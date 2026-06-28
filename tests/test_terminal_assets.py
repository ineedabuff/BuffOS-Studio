from pathlib import Path


def test_terminal_colors_asset_exists():
    path = Path("installer/app/plugins/terminal/assets/colors.json")

    assert path.exists()
    assert "#DDFF24" in path.read_text()
    assert "#1F51FF" in path.read_text()
