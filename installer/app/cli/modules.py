from __future__ import annotations

from app.core.runner import Runner
from app.plugins.manager import PluginManager


def create_runner(dry_run: bool = False) -> Runner:
    manager = PluginManager()
    manager.discover()

    runner = Runner(dry_run=dry_run)
    runner.load(manager)

    return runner
