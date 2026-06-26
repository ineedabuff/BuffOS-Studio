from app.analysis.result import CheckResult
from app.install.planner import InstallationPlanner
from app.providers.fakes.fake_apt import FakeAptProvider
from app.validators.validation_report import ValidationReport


def make_report(timeshift_ok: bool, grub_ok: bool) -> ValidationReport:
    report = ValidationReport()
    report.add(
        CheckResult(timeshift_ok, "Timeshift", "Valid" if timeshift_ok else "Invalid")
    )
    report.add(CheckResult(grub_ok, "grub-btrfs", "Valid" if grub_ok else "Invalid"))
    return report


def make_planner() -> InstallationPlanner:
    return InstallationPlanner(FakeAptProvider())


def test_planner_adds_timeshift_installer_when_timeshift_is_invalid():
    plan = make_planner().create(make_report(False, True))

    installers = plan.all()

    assert len(installers) == 1
    assert installers[0].__class__.__name__ == "TimeshiftInstaller"


def test_planner_adds_grub_btrfs_installer_when_invalid():
    plan = make_planner().create(make_report(True, False))

    installers = plan.all()

    assert len(installers) == 1
    assert installers[0].__class__.__name__ == "GrubBtrfsInstaller"


def test_planner_adds_both_installers_when_both_are_invalid():
    plan = make_planner().create(make_report(False, False))

    installers = plan.all()

    assert len(installers) == 2

    names = {installer.__class__.__name__ for installer in installers}

    assert names == {
        "TimeshiftInstaller",
        "GrubBtrfsInstaller",
    }


def test_planner_returns_empty_plan_when_everything_is_valid():
    plan = make_planner().create(make_report(True, True))

    assert plan.all() == []
