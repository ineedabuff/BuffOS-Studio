from __future__ import annotations

from app.core.events import EventBus
from app.core.logger import get_logger
from app.core.report import Report
from app.core.runner import Runner


class Engine:
    """BuffOS Engine."""

    def __init__(self) -> None:
        self.logger = get_logger("Engine")
        self.events = EventBus()
        self.report = Report()
        self.runner = Runner()

        self.logger.info("Engine initialized.")
