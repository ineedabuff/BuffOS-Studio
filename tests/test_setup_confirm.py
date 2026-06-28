from unittest.mock import patch

from app.setup.confirm import confirm


def test_confirm_yes_default():
    with patch("builtins.input", return_value=""):
        assert confirm()


def test_confirm_no():
    with patch("builtins.input", return_value="n"):
        assert not confirm()
