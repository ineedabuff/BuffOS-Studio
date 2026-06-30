from unittest.mock import patch

from app.catalog.search import find_by_id
from app.setup.app_selector import edit_selection
from app.setup.selection import Selection


def test_edit_selection_keeps_default():
    firefox = find_by_id("firefox")

    assert firefox is not None

    with patch("builtins.input", return_value=""):
        selection = edit_selection(Selection([firefox]))

    assert selection.ids == ["firefox"]


def test_edit_selection_can_skip():
    firefox = find_by_id("firefox")

    assert firefox is not None

    with patch("builtins.input", return_value="n"):
        selection = edit_selection(Selection([firefox]))

    assert selection.ids == []
