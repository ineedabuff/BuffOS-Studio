from __future__ import annotations

from app.catalog.search import find_by_id
from app.install_engine.executor import execute_plan
from app.install_engine.planner import create_plan
from app.setup.selection import Selection


class InstallEngine:
    def install(self, app_id: str) -> bool:
        entry = find_by_id(app_id)

        if entry is None:
            print(f"✗ Unknown application: {app_id}")
            return False

        print(f"== Installing {entry.name} ==")

        plan = create_plan(Selection([entry]))
        execute_plan(plan)

        return True
