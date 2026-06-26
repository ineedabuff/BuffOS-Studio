from __future__ import annotations

from app.analysis.analysis_report import AnalysisReport
from app.analysis.result import CheckResult


class MountOptionsValidator:
    REQUIRED = {
        "compress=zstd",
        "noatime",
        "ssd",
        "discard=async",
        "space_cache=v2",
    }

    def validate(self, report: AnalysisReport) -> CheckResult:
        mount = report.get("Mount Options")

        if mount is None:
            return CheckResult(False, "Mount Options", "Missing")

        options = set(mount.message.split(","))

        valid = all(
            any(opt.startswith(req) for opt in options) for req in self.REQUIRED
        )

        return CheckResult(
            success=valid,
            title="Mount Options",
            message="Valid" if valid else "Invalid",
        )
