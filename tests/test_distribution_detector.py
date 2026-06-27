from pathlib import Path

from app.os.detector import DistributionDetector


def test_distribution_detector(tmp_path: Path):
    os_release = tmp_path / "os-release"
    os_release.write_text(
        'NAME="Ubuntu"\n' 'VERSION_ID="26.04"\n' 'PRETTY_NAME="Ubuntu 26.04 LTS"\n'
    )

    detector = DistributionDetector(os_release)

    assert detector.detect()["NAME"] == "Ubuntu"
    assert detector.detect()["VERSION_ID"] == "26.04"
    assert detector.pretty_name() == "Ubuntu 26.04 LTS"
