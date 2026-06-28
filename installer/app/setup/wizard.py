from __future__ import annotations

from app.catalog.recommendations import recommended


def run() -> None:
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("        Linux Setup Assistant")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    print("Recommended applications")
    print()

    for entry in recommended():
        print(f"✓ {entry.name} [{entry.category}]")

    print()
