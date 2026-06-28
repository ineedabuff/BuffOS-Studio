from __future__ import annotations

from app.install_engine.plan_runner import run_plan
from app.install_engine.report import InstallReport
from app.setup.selection import Selection


def install_selection(selection: Selection) -> InstallReport:
    return run_plan(selection)
