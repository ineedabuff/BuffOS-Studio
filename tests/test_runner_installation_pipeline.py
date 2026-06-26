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


def test_runner_executes_installation_pipeline():
    package_provider = FakeAptProvider()
    systemd_provider = FakeSystemdProvider()

    factory = InstallerFactory(
        package_provider,
        systemd_provider,
    )

    runner = Runner(factory=factory)
    runner.register(FakeAnalysisModule())

    runner.execute()

    assert "timeshift" in package_provider.installed
    assert "grub-btrfs" in package_provider.installed
    assert systemd_provider.is_enabled("grub-btrfsd.service") is True
    assert systemd_provider.is_active("grub-btrfsd.service") is True
