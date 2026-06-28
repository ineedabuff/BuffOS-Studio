from __future__ import annotations

import shutil
import subprocess


def cmd(name: str) -> bool:
    return shutil.which(name) is not None


def pkg(name: str) -> bool:
    return (
        subprocess.run(
            ["dpkg", "-s", name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def install(pkgname: str) -> None:
    subprocess.run(
        ["sudo", "apt", "install", "-y", pkgname],
        check=False,
    )


def run() -> None:
    print("== Buff Helper NVIDIA ==")

    packages = [
        "nvidia-driver-595",
        "nvidia-settings",
        "nvidia-prime",
        "libnvidia-gl-595:i386",
    ]

    for package in packages:
        if pkg(package):
            print(f"✓ {package}")
            continue

        print(f"Installing {package}...")
        install(package)

    if cmd("nvidia-smi"):
        print("✓ nvidia-smi")
    else:
        print("✗ nvidia-smi")

    if cmd("vulkaninfo"):
        print("✓ vulkaninfo")
    else:
        print("Installing vulkan-tools...")
        install("vulkan-tools")

    print("NVIDIA profile completed.")
