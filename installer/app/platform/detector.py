from __future__ import annotations

from pathlib import Path

from app.platform.platform import Platform


class PlatformDetector:
    def __init__(self, path: Path = Path("/etc/os-release")) -> None:
        self.path = path

    def detect(self) -> Platform:
        data: dict[str, str] = {}

        if self.path.exists():
            for line in self.path.read_text().splitlines():
                if "=" not in line:
                    continue

                key, value = line.split("=", 1)
                data[key] = value.strip('"')

        distro = data.get("ID", "").lower()
        version = data.get("VERSION_ID", "")

        if distro in {
            "ubuntu",
            "kubuntu",
            "xubuntu",
            "lubuntu",
            "ubuntu-studio",
            "pop",
            "linuxmint",
            "debian",
            "tuxedo",
        }:
            return Platform(
                name=data.get("NAME", distro),
                version=version,
                family="debian",
                package_manager="apt",
                supported=True,
            )

        if distro in {"arch", "cachyos", "endeavouros"}:
            return Platform(
                name=data.get("NAME", distro),
                version=version,
                family="arch",
                package_manager="pacman",
                supported=False,
            )

        if distro in {"fedora"}:
            return Platform(
                name=data.get("NAME", distro),
                version=version,
                family="fedora",
                package_manager="dnf",
                supported=False,
            )

        if distro in {"opensuse-tumbleweed", "opensuse-leap"}:
            return Platform(
                name=data.get("NAME", distro),
                version=version,
                family="opensuse",
                package_manager="zypper",
                supported=False,
            )

        return Platform(
            name=data.get("NAME", "Unknown Linux"),
            version=version,
            family="unknown",
            package_manager="unknown",
            supported=False,
        )
