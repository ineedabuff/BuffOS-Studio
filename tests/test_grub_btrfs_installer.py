from app.installers.grub_btrfs import GrubBtrfsInstaller
from app.providers.fakes.fake_apt import FakeAptProvider
from app.providers.fakes.fake_systemd import FakeSystemdProvider


def test_grub_btrfs_installer():
    provider = FakeAptProvider()
    systemd = FakeSystemdProvider()

    installer = GrubBtrfsInstaller(provider, systemd)

    assert installer.install() is True
    assert installer.configure() is True
    assert provider.installed == ["grub-btrfs"]
    assert systemd.is_enabled("grub-btrfsd.service") is True
    assert systemd.is_active("grub-btrfsd.service") is True
