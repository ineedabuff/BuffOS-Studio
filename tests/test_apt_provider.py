from app.providers.apt import AptProvider


def test_apt_provider_dry_run():
    provider = AptProvider(dry_run=True)

    assert provider.install("timeshift") is True
