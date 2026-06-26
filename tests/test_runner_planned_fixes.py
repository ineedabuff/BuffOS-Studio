from app.analysis.result import CheckResult
from app.core.runner import Runner
from app.install.installer_factory import InstallerFactory
from app.providers.fakes.fake_apt import FakeAptProvider
from app.providers.fakes.fake_systemd import FakeSystemdProvider


class FakeAnalysisModule:
    name = "Fake Analysis"

    def run(self):
        return [
            CheckResult(True, "Filesystem", "btrfs"),
            CheckResult(True, "Root Subvolume", "/@"),
            CheckResult(True, "Home Subvolume", "/@home"),
            CheckResult(
                True,
                "Mount Options",
                "compress=zstd,noatime,ssd,discard=async,space_cache=v2",
            ),
            CheckResult(False, "Timeshift", "Not installed"),
            CheckResult(False, "grub-btrfs", "Not installed"),
        ]


def test_runner_reports_planned_fixes():
    runner = Runner(
        factory=InstallerFactory(
            FakeAptProvider(),
            FakeSystemdProvider(),
        )
    )
    runner.register(FakeAnalysisModule())

    runner.execute()

    planned = runner.report._results[0]

    assert planned.title == "Planned Fixes"
    assert "TimeshiftInstaller" in planned.message
    assert "GrubBtrfsInstaller" in planned.message
