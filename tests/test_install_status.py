from app.install_engine.status import apt_installed, command_exists, flatpak_installed


def test_status_helpers_exist():
    assert callable(command_exists)
    assert callable(apt_installed)
    assert callable(flatpak_installed)
