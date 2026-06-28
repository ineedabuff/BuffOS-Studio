from unittest.mock import Mock, patch

from app.install_engine.executor import execute_plan
from app.install_engine.plan import InstallPlan


def test_execute_plan():
    plan = InstallPlan(
        apt=["git"],
        flatpak=["org.mozilla.firefox"],
        scripts=["install-buff-zsh.sh"],
    )

    with (
        patch("app.install_engine.executor.apt_installed", return_value=False),
        patch("app.install_engine.executor.flatpak_installed", return_value=False),
        patch("subprocess.run", return_value=Mock(returncode=0)) as run,
    ):
        report = execute_plan(plan)

    assert run.call_count == 3
    assert report.success
    assert "git" in report.installed
    assert "org.mozilla.firefox" in report.installed
    assert "install-buff-zsh.sh" in report.installed


def test_execute_plan_skips_installed_items():
    plan = InstallPlan(
        apt=["git"],
        flatpak=["org.mozilla.firefox"],
        scripts=[],
    )

    with (
        patch("app.install_engine.executor.apt_installed", return_value=True),
        patch("app.install_engine.executor.flatpak_installed", return_value=True),
        patch("subprocess.run") as run,
    ):
        report = execute_plan(plan)

    run.assert_not_called()
    assert report.success
    assert "git" in report.skipped
    assert "org.mozilla.firefox" in report.skipped
