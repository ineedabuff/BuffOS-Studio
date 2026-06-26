from app.installers.runner import InstallerRunner
from app.installers.timeshift import TimeshiftInstaller
from app.providers.apt import AptProvider


def test_installer_runner():
    runner = InstallerRunner()
    runner.register(TimeshiftInstaller(AptProvider(dry_run=True)))

    assert runner.run() is True
