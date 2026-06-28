from __future__ import annotations

import shutil
import subprocess

PACKAGES = [
    "zsh",
    "fastfetch",
    "bat",
    "eza",
    "fzf",
]


def installed(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def install(pkg: str) -> None:
    subprocess.run(
        ["sudo", "apt", "install", "-y", pkg],
        check=False,
    )


def run() -> None:
    print("== Buff Helper Terminal ==")

    mapping = {
        "zsh": "zsh",
        "fastfetch": "fastfetch",
        "batcat": "bat",
        "eza": "eza",
        "fzf": "fzf",
    }

    for command, package in mapping.items():
        if installed(command):
            print(f"✓ {package}")
            continue

        print(f"Installing {package}...")
        install(package)

    print("Terminal profile completed.")
