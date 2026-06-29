from unittest.mock import patch

from app.profile.selector import select_profile


def test_default_selection():
    with patch("builtins.input", return_value=""):
        assert select_profile() == "buff"


def test_numeric_selection():
    with patch("builtins.input", return_value="1"):
        assert select_profile() == "buff"
