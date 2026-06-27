from __future__ import annotations

from pathlib import Path


class DistributionDetector:
    def __init__(self, path: Path = Path("/etc/os-release")) -> None:
        self.path = path

    def detect(self) -> dict[str, str]:
        data: dict[str, str] = {}

        if not self.path.exists():
            return data

        for line in self.path.read_text().splitlines():
            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            data[key] = value.strip('"')

        return data

    def pretty_name(self) -> str:
        data = self.detect()
        return data.get("PRETTY_NAME", "Unknown Linux")
