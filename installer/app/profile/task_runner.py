from __future__ import annotations

import subprocess
from pathlib import Path

from app.profile.tasks import profile_tasks


def run_profile_tasks(profile: str) -> None:
    for script in profile_tasks(profile):
        path = Path("installer/assets/scripts") / script
        subprocess.run(["bash", str(path)], check=False)
