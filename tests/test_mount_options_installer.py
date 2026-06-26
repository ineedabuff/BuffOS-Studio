from app.installers.mount_options import MountOptionsInstaller
from app.providers.fakes.fake_fstab import FakeFstabProvider


def test_mount_options_installer():
    provider = FakeFstabProvider("UUID=123 / btrfs defaults,ssd 0 0\n")

    installer = MountOptionsInstaller(provider)

    assert installer.install() is True
    assert installer.configure() is True

    content = provider.read()

    assert "compress=zstd" in content
    assert "noatime" in content
    assert "ssd" in content
    assert "discard=async" in content
    assert "space_cache=v2" in content
    assert "defaults" not in content
