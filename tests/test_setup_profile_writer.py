from pathlib import Path

from app.catalog.search import find_by_id
from app.setup.profile_writer import write_profile
from app.setup.selection import Selection


def test_write_profile(tmp_path: Path):
    firefox = find_by_id("firefox")

    assert firefox is not None

    path = write_profile(
        Selection([firefox]),
        tmp_path / "profile.yaml",
    )

    text = path.read_text(encoding="utf-8")

    assert "applications:" in text
    assert "- firefox" in text
