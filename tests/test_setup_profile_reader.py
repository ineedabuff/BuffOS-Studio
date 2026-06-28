from pathlib import Path

from app.setup.profile_reader import read_profile


def test_read_profile(tmp_path: Path):
    path = tmp_path / "profile.yaml"
    path.write_text(
        "applications:\n" "  - firefox\n" "  - vesktop\n",
        encoding="utf-8",
    )

    assert read_profile(path) == ["firefox", "vesktop"]
