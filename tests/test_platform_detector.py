from pathlib import Path

from app.platform.detector import PlatformDetector


def test_platform_detector_ubuntu(tmp_path: Path):
    os_release = tmp_path / "os-release"

    os_release.write_text("ID=ubuntu\n" 'NAME="Ubuntu"\n' 'VERSION_ID="26.04"\n')

    platform = PlatformDetector(os_release).detect()

    assert platform.name == "Ubuntu"
    assert platform.family == "debian"
    assert platform.package_manager == "apt"
    assert platform.supported is True


def test_platform_detector_arch(tmp_path: Path):
    os_release = tmp_path / "os-release"

    os_release.write_text("ID=arch\n" 'NAME="Arch Linux"\n' 'VERSION_ID="2026"\n')

    platform = PlatformDetector(os_release).detect()

    assert platform.family == "arch"
    assert platform.package_manager == "pacman"
    assert platform.supported is False
