from __future__ import annotations

from pathlib import Path


class FstabProvider:
    def __init__(self, path: Path = Path("/etc/fstab")) -> None:
        self.path = path

    def read(self) -> str:
        return self.path.read_text()

    def write(self, content: str) -> None:
        self.path.write_text(content)
