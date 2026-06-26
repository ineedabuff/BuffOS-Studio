import platform
import shutil
import subprocess
from pathlib import Path

from app.modules.base import Module


class SystemCheckModule(Module):
    """Checks whether the system is ready for BuffOS installation."""

    name = "System Check"
    description = "Validate basic system requirements."

    def run(self) -> bool:
        return (
            self._check_os()
            and self._check_uefi()
            and self._check_secure_boot()
        )

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

        return True

    def _check_uefi(self) -> bool:
        self.logger.info("Checking firmware mode...")

        if Path("/sys/firmware/efi").exists():
            self.logger.info("Firmware mode: UEFI")
            return True

        self.logger.error("Firmware mode: BIOS/Legacy")
        return False

    def _check_secure_boot(self) -> bool:
        self.logger.info("Checking Secure Boot...")

        if shutil.which("mokutil") is None:
            self.logger.warning("mokutil is not installed.")
            return True

        result = subprocess.run(
            ["mokutil", "--sb-state"],
            capture_output=True,
            text=True,
        )

        output = result.stdout.strip()

        if "enabled" in output.lower():
            self.logger.warning("Secure Boot: ENABLED")
        elif "disabled" in output.lower():
            self.logger.info("Secure Boot: disabled")
        else:
            self.logger.info(output)

        return True
