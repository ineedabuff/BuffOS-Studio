from unittest.mock import patch

from app.__main__ import main


def test_main():
    with (
        patch("sys.argv", ["buffos", "version"]),
        patch("builtins.print") as p,
    ):
        main()
        p.assert_called()
