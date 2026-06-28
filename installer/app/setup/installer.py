from __future__ import annotations

from app.install_engine.engine import InstallEngine
from app.setup.selection import Selection


def install_selection(selection: Selection) -> None:
    engine = InstallEngine()

    for entry in selection.entries:
        engine.install(entry.id)
