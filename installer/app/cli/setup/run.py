from __future__ import annotations

from app.cli.apply.buff import run as apply_buff
from app.cli.doctor import run_doctor


def run() -> None:
    print()
    print("========================================")
    print("       Buff Helper Setup")
    print("========================================")

    print("\n[1/3] Initial diagnosis\n")
    run_doctor()

    print("\n[2/3] Applying Buff profile\n")
    apply_buff()

    print("\n[3/3] Final diagnosis\n")
    run_doctor()

    print("\n✓ Setup completed.")
