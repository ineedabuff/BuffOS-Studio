from __future__ import annotations


class FakeSystemdProvider:
    def __init__(self) -> None:
        self.enabled: list[str] = []
        self.started: list[str] = []

    def is_enabled(self, service: str) -> bool:
        return service in self.enabled

    def is_active(self, service: str) -> bool:
        return service in self.started

    def enable(self, service: str) -> bool:
        self.enabled.append(service)
        return True

    def start(self, service: str) -> bool:
        self.started.append(service)
        return True
