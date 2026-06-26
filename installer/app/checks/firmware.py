from pathlib import Path

from app.checks.base import Check


class FirmwareCheck(Check):
    """Firmware-related checks."""

    name = "Firmware"
    description = "Validate UEFI firmware mode."

    def run(self) -> bool:
        self.logger.info("Checking firmware mode...")

        if self.is_uefi():
            self.logger.info("Firmware mode: UEFI")
            return True

        self.logger.error("Firmware mode: BIOS/Legacy")
        return False

    @staticmethod
    def is_uefi() -> bool:
        return Path("/sys/firmware/efi").exists()
