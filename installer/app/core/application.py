from __future__ import annotations

from app.core.engine import Engine
from app.core.logger import get_logger
from app.core.ui import print_header
from app.modules.system import SystemCheckModule


class Application:
    """Main BuffOS Studio application orchestrator."""

    def __init__(self) -> None:
        self.logger = get_logger("Application")
        self.engine = Engine()

    def start(self) -> None:
        print_header()
        self.logger.info("Starting BuffOS Studio application.")

        self._register_modules()
        self.engine.runner.execute()

    def _register_modules(self) -> None:
        self.logger.info("Registering modules.")
        self.engine.runner.register(SystemCheckModule())
