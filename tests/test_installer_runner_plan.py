from app.install.installation_plan import InstallationPlan
from app.install.installer_factory import InstallerFactory
from app.installers.runner import InstallerRunner
from app.providers.fakes.fake_apt import FakeAptProvider
from app.providers.fakes.fake_systemd import FakeSystemdProvider


def test_installer_runner_executes_plan():
    factory = InstallerFactory(
        FakeAptProvider(),
        FakeSystemdProvider(),
    )

    plan = InstallationPlan()
    plan.add(factory.timeshift())
    plan.add(factory.grub_btrfs())

    runner = InstallerRunner()

    for installer in plan.all():
        runner.register(installer)

    assert runner.run() is True
