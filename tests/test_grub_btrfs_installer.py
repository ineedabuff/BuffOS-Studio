from app.installers.grub_btrfs import GrubBtrfsInstaller
from app.providers.fakes.fake_apt import FakeAptProvider


def test_grub_btrfs_installer():
    provider = FakeAptProvider()
    installer = GrubBtrfsInstaller(provider)

    assert installer.install() is True
    assert provider.installed == ["grub-btrfs"]
