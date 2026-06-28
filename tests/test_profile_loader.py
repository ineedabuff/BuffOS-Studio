from app.profile.loader import load


def test_terminal_profile():
    assert "fastfetch" in load("apt", "terminal")


def test_gaming_profile():
    assert "gamemode" in load("apt", "gaming")


def test_nvidia_profile():
    assert "nvidia-driver-595" in load("apt", "nvidia")


def test_buff_profile():
    assert "ru.linux_gaming.PortProton" in load("flatpak", "buff")
