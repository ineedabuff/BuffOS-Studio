from app.installers.runner import InstallerRunner
from app.installers.timeshift import TimeshiftInstaller


def test_installer_runner():
    runner = InstallerRunner()
    runner.register(TimeshiftInstaller())

    assert runner.run() is True
