import platform
from pathlib import Path

from app.analysis.base import Check
from app.analysis.result import CheckResult


class OperatingSystemAnalysis(Check):
    """Operating system related analysis."""

    name = "Operating System"
    description = "Validate Linux distribution information."

    def run(self) -> CheckResult:
        if not self.is_linux():
            return CheckResult(
                success=False,
                title=self.name,
                message="Unsupported operating system",
            )

        data = self.os_release()

        return CheckResult(
            success=True,
            title=self.name,
            message=data.get("PRETTY_NAME", "Unknown"),
        )

    @staticmethod
    def system() -> str:
        return platform.system()

    @staticmethod
    def is_linux() -> bool:
        return platform.system() == "Linux"

    @staticmethod
    def os_release() -> dict[str, str]:
        path = Path("/etc/os-release")

        if not path.exists():
            return {}

        data = {}

        for line in path.read_text().splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                data[key] = value.strip('"')

        return data
