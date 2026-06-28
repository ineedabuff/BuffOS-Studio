from __future__ import annotations

from app.install_engine.plan_runner import run_plan
from app.setup.selection import Selection


def install_selection(selection: Selection) -> None:
    run_plan(selection)
