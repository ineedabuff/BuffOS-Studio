from unittest.mock import patch

from app.install_engine.executor import execute_plan
from app.install_engine.plan import InstallPlan


def test_execute_plan():
    plan = InstallPlan(
        apt=["git"],
        flatpak=["org.mozilla.firefox"],
        scripts=["install-buff-zsh.sh"],
    )

    with patch("subprocess.run") as run:
        execute_plan(plan)

    assert run.call_count == 3
