from pathlib import Path

from app.providers.system import SystemProvider


def test_system_provider_which():
    provider = SystemProvider()

    assert provider.which("python") is not None


def test_system_provider_file_helpers(tmp_path: Path):
    provider = SystemProvider()
    path = tmp_path / "demo.txt"

    provider.write_text(path, "buff")

    assert provider.exists(path)
    assert provider.read_text(path) == "buff"
