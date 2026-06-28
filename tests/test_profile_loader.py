from app.profile.loader import load


def test_load():
    assert "fastfetch" in load("apt")
    assert "ru.linux_gaming.PortProton" in load("flatpak")
