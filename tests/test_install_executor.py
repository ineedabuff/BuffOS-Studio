from unittest.mock import patch

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
        patch("subprocess.run") as run,
    ):
        execute_plan(plan)

    assert run.call_count == 3


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
        execute_plan(plan)

    run.assert_not_called()
