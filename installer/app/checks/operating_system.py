import platform
from pathlib import Path

from app.checks.base import Check


class OperatingSystemCheck(Check):
    """Operating system related checks."""

    name = "Operating System"
    description = "Validate Linux distribution information."

    def run(self) -> bool:
        self.logger.info("Checking operating system...")

        if not self.is_linux():
            self.logger.error("Unsupported operating system.")
            return False

        self.logger.info(f"Operating system: {self.system()}")

        data = self.os_release()
        self.logger.info(f"Distribution : {data.get('PRETTY_NAME', 'Unknown')}")
        self.logger.info(f"Version      : {data.get('VERSION_ID', 'Unknown')}")
        self.logger.info(f"ID           : {data.get('ID', 'Unknown')}")

        return True

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
