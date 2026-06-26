from __future__ import annotations


class FakeFstabProvider:
    def __init__(self, content: str = "") -> None:
        self.content = content

    def read(self) -> str:
        return self.content

    def write(self, content: str) -> None:
        self.content = content
