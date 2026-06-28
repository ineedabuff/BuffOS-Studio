from app.install_engine.engine import InstallEngine


def test_install_engine_exists():
    assert callable(InstallEngine().install)
