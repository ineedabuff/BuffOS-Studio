from __future__ import annotations

from app.profile.installer import run as install_profile


def run() -> None:
    print("========================================")
    print("        Applying BuffOS Profile")
    print("========================================")
    print()

    install_profile()

    print()
    print("✓ BuffOS profile applied.")
