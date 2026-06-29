from unittest.mock import patch

from app.install_engine.engine import InstallEngine


def test_install_engine_exists():
    assert callable(InstallEngine().install)


def test_install_known_app():
    with patch("app.install_engine.engine.execute_plan") as execute_plan:
        result = InstallEngine().install("firefox")

    assert result
    execute_plan.assert_called_once()


def test_install_unknown_app():
    assert not InstallEngine().install("does-not-exist")
