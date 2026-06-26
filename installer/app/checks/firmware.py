from pathlib import Path


class FirmwareCheck:
    """Firmware-related checks."""

    @staticmethod
    def is_uefi() -> bool:
        return Path("/sys/firmware/efi").exists()
