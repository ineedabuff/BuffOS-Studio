import platform
from pathlib import Path

from app.core.logger import get_logger
from app.modules.base import Module

logger = get_logger()


class SystemCheckModule(Module):
    """Checks whether the system is ready for BuffOS installation."""

    name = "System Check"
    description = "Validate basic system requirements."

    def run(self) -> bool:
        logger.info("Checking operating system...")

        if platform.system() != "Linux":
            logger.error("Unsupported operating system.")
            return False

        logger.info(f"Operating system: {platform.system()}")

        os_release = Path("/etc/os-release")

        if os_release.exists():
            data = {}

            for line in os_release.read_text().splitlines():
                if "=" in line:
                    key, value = line.split("=", 1)
                    data[key] = value.strip('"')

            logger.info(f"Distribution : {data.get('PRETTY_NAME', 'Unknown')}")
            logger.info(f"Version      : {data.get('VERSION_ID', 'Unknown')}")
            logger.info(f"ID           : {data.get('ID', 'Unknown')}")

        else:
            logger.warning("/etc/os-release not found.")

        return True
