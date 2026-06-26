from app.providers.fakes.fake_fstab import FakeFstabProvider


def test_fake_fstab_provider():
    provider = FakeFstabProvider("old")

    assert provider.read() == "old"

    provider.write("new")

    assert provider.read() == "new"
