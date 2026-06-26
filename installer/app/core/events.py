from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable


class EventBus:
    """Simple publish/subscribe event bus."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable) -> None:
        self._listeners[event].append(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for callback in self._listeners[event]:
            callback(*args, **kwargs)
