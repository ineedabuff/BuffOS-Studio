from app.providers.fakes.fake_systemd import FakeSystemdProvider


def test_fake_systemd_provider():
    systemd = FakeSystemdProvider()

    systemd.enable("grub-btrfsd.service")
    systemd.start("grub-btrfsd.service")

    assert systemd.is_enabled("grub-btrfsd.service") is True
    assert systemd.is_active("grub-btrfsd.service") is True
