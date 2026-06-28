from __future__ import annotations

from app.install_engine.executor import execute_plan
from app.install_engine.planner import create_plan
from app.install_engine.report import InstallReport
from app.setup.selection import Selection


def run_plan(selection: Selection) -> InstallReport:
    plan = create_plan(selection)
    return execute_plan(plan)
