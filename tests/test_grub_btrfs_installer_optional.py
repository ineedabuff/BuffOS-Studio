from app.installers.grub_btrfs import GrubBtrfsInstaller
from app.providers.fakes.fake_systemd import FakeSystemdProvider


class FailingProvider:
    def install(self, package: str) -> bool:
        return False


def test_grub_btrfs_installer_is_optional_when_package_is_missing():
    systemd = FakeSystemdProvider()

    installer = GrubBtrfsInstaller(FailingProvider(), systemd)

    assert installer.install() is True
    assert installer.configure() is True
    assert installer.skipped is True
