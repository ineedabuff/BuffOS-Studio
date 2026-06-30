from unittest.mock import patch

from app.profile.task_runner import run_profile_tasks


def test_run_profile_tasks():
    with (
        patch(
            "app.profile.task_runner.profile_tasks",
            return_value=["install-buff-zsh.sh"],
        ),
        patch("subprocess.run") as run,
    ):
        run_profile_tasks("buff")

    run.assert_called_once()
