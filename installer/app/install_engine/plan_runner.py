from __future__ import annotations

from app.install_engine.executor import execute_plan
from app.install_engine.planner import create_plan
from app.setup.selection import Selection


def run_plan(selection: Selection) -> None:
    plan = create_plan(selection)
    execute_plan(plan)
