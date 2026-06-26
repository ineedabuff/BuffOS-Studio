from app.installers.mount_options import MountOptionsInstaller
from app.providers.fakes.fake_fstab import FakeFstabProvider


def test_mount_options_installer():
    provider = FakeFstabProvider()

    installer = MountOptionsInstaller(provider)

    assert installer.install() is True
    assert installer.configure() is True
