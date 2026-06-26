from app.core.dry_run import DryRun
from app.install.installation_plan import InstallationPlan
from app.install.installer_factory import InstallerFactory
from app.providers.fakes.fake_apt import FakeAptProvider
from app.providers.fakes.fake_systemd import FakeSystemdProvider


def test_dry_run(capsys):
    factory = InstallerFactory(
        FakeAptProvider(),
        FakeSystemdProvider(),
    )

    plan = InstallationPlan()
    plan.add(factory.timeshift())
    plan.add(factory.grub_btrfs())

    DryRun().show(plan)

    out = capsys.readouterr().out

    assert "Planned actions" in out
    assert "Timeshift" in out
    assert "grub-btrfs" in out
