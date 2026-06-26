from app.installers.mount_options import MountOptionsInstaller
from app.providers.fakes.fake_fstab import FakeFstabProvider


def test_mount_options_installer():
    provider = FakeFstabProvider(
        "UUID=123 / btrfs defaults,ssd 0 0\n"
    )

    installer = MountOptionsInstaller(provider)

    assert installer.install() is True
    assert installer.configure() is True

    assert provider.read() == (
        "UUID=123 / btrfs "
        "compress=zstd,noatime,ssd,discard=async,space_cache=v2,ssd 0 0\n"
    )
