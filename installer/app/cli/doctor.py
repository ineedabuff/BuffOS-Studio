from __future__ import annotations

import shutil
import subprocess


def ok_fn(text: str) -> None:
    print(f"\033[92m✓\033[0m {text}")


def fail(text: str) -> None:
    print(f"\033[91m✗\033[0m {text}")


def print_check(label: str, ok: bool) -> None:
    print(f"{"✓" if ok else "✗"} {label}")


def check(label: str, value: bool) -> bool:
    if value:
        ok_fn(label)
    else:
        fail(label)

    return value


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def systemd(unit: str) -> bool:
    return (
        subprocess.run(
            ["systemctl", "is-active", "--quiet", unit],
            check=False,
        ).returncode
        == 0
    )


def flatpak(app: str) -> bool:
    return (
        subprocess.run(
            ["flatpak", "info", app],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def section(title: str) -> None:
    print()
    print(f"\033[1;36m{title}\033[0m")
    print("─" * len(title))


def run_doctor() -> None:
    print()
    print("\033[1;97mBuff Helper Doctor\033[0m")
    print("=" * 40)

    passed = 0
    total = 0

    section("Storage")

    for name, value in [
        ("Timeshift", command_exists("timeshift")),
        ("grub-btrfsd", systemd("grub-btrfsd.service")),
        ("fstrim.timer", systemd("fstrim.timer")),
        ("btrfs-scrub.timer", systemd("btrfs-scrub.timer")),
    ]:
        total += 1
        passed += check(name, value)

    section("Gaming")

    for name, value in [
        ("NVIDIA", command_exists("nvidia-smi")),
        ("Steam", command_exists("steam")),
        ("GameMode", command_exists("gamemoded")),
        ("MangoHud", command_exists("mangohud")),
        ("PortProton", flatpak("ru.linux_gaming.PortProton")),
    ]:
        total += 1
        passed += check(name, value)

    print()
    print("=" * 40)

    score = round((passed / total) * 100)

    print(f"BUFF READY : {score}%")
    print(f"{passed}/{total} checks passed")
    print()
