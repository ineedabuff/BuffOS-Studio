from __future__ import annotations

from app.cli.apply.gaming import run as gaming
from app.cli.apply.nvidia import run as nvidia
from app.cli.apply.terminal import run as terminal


def run() -> None:
    print("========================================")
    print("      Buff Helper - Buff Profile")
    print("========================================")
    print()

    terminal()
    print()

    nvidia()
    print()

    gaming()
    print()

    print("✓ Buff profile completed.")
