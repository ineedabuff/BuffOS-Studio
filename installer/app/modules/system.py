import platform
from pathlib import Path

from app.modules.base import Module


class SystemCheckModule(Module):
    """Checks whether the system is ready for BuffOS installation."""

    name = "System Check"
    description = "Validate basic system requirements."

    def run(self) -> bool:
        return self._check_os() and self._check_uefi()

    def _check_os(self) -> bool:
        self.logger.info("Checking operating system...")

        if platform.system() != "Linux":
            self.logger.error("Unsupported operating system.")
            return False

        self.logger.info(f"Operating system: {platform.system()}")

        os_release = Path("/etc/os-release")

        if os_release.exists():
            data = {}

            for line in os_release.read_text().splitlines():
                if "=" in line:
                    key, value = line.split("=", 1)
                    data[key] = value.strip('"')

            self.logger.info(f"Distribution : {data.get('PRETTY_NAME', 'Unknown')}")
            self.logger.info(f"Version      : {data.get('VERSION_ID', 'Unknown')}")
            self.logger.info(f"ID           : {data.get('ID', 'Unknown')}")
        else:
            self.logger.warning("/etc/os-release not found.")

        return True

    def _check_uefi(self) -> bool:
        self.logger.info("Checking firmware mode...")

        if Path("/sys/firmware/efi").exists():
            self.logger.info("Firmware mode: UEFI")
            return True

        self.logger.error("Firmware mode: BIOS/Legacy")
        return False
