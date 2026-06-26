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


def test_runner_dry_run_does_not_install(capsys):
    package_provider = FakeAptProvider()

    runner = Runner(
        factory=InstallerFactory(
            package_provider,
            FakeSystemdProvider(),
        ),
        dry_run=True,
    )
    runner.register(FakeAnalysisModule())

    runner.execute()

    out = capsys.readouterr().out

    assert "Planned actions" in out
    assert package_provider.installed == []
