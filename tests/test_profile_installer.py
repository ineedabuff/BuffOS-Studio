from app.profile.installer import enable_systemd, install_apt, install_flatpak


def test_profile_installer():
    assert callable(install_apt)
    assert callable(install_flatpak)
    assert callable(enable_systemd)
