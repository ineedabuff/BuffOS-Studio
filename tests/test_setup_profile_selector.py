from unittest.mock import patch

from app.setup.profile_selector import select_profile_selection


def test_select_profile_selection():
    with patch("app.setup.profile_selector.select_profile", return_value="buff"):
        selection = select_profile_selection()

    ids = {entry.id for entry in selection.entries}

    assert "firefox" in ids
    assert "vesktop" in ids
