from __future__ import annotations

import shutil
import subprocess


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def systemctl_is_active(unit: str) -> bool:
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", unit],
        check=False,
    )
    return result.returncode == 0


def flatpak_app_installed(app_id: str) -> bool:
    result = subprocess.run(
        ["flatpak", "info", app_id],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def print_check(label: str, ok: bool) -> None:
    symbol = "✓" if ok else "✗"
    print(f"{symbol} {label}")


def run_doctor() -> None:
    print("Buff Helper Doctor")
    print("------------------")

    print_check("Timeshift", command_exists("timeshift"))
    print_check("grub-btrfsd", systemctl_is_active("grub-btrfsd.service"))
    print_check("fstrim.timer", systemctl_is_active("fstrim.timer"))
    print_check("btrfs-scrub.timer", systemctl_is_active("btrfs-scrub.timer"))

    print_check("NVIDIA", command_exists("nvidia-smi"))
    print_check("Steam", command_exists("steam"))
    print_check("GameMode", command_exists("gamemoded"))
    print_check("MangoHud", command_exists("mangohud"))
    print_check("PortProton", flatpak_app_installed("ru.linux_gaming.PortProton"))
