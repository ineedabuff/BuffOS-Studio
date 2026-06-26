import subprocess


class FilesystemCheck:
    """Filesystem-related checks."""

    @staticmethod
    def root_filesystem() -> str:
        result = subprocess.run(
            ["findmnt", "-n", "-o", "FSTYPE", "/"],
            capture_output=True,
            text=True,
        )

        return result.stdout.strip()

    @staticmethod
    def is_btrfs() -> bool:
        return FilesystemCheck.root_filesystem() == "btrfs"
