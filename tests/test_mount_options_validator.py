from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult
from app.validators.mount_options_validator import MountOptionsValidator


def test_mount_options_validator():
    report = AnalysisReport()

    report.add(
        CheckResult(
            True,
            "Mount Options",
            "rw,noatime,compress=zstd:3,ssd,discard=async,space_cache=v2",
        )
    )

    result = MountOptionsValidator().validate(report)

    assert result.success is True
    assert result.message == "Valid"
