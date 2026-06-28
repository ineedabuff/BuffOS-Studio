from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class SystemProvider:
    def run(
        self,
        command: list[str],
        *,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            command,
            check=check,
            capture_output=True,
            text=True,
        )

    def which(self, command: str) -> str | None:
        return shutil.which(command)

    def exists(self, path: str | Path) -> bool:
        return Path(path).exists()

    def read_text(self, path: str | Path) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write_text(self, path: str | Path, content: str) -> None:
        Path(path).write_text(content, encoding="utf-8")
