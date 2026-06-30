from __future__ import annotations

from app.catalog.profile_loader import load_profile
from app.cli.doctor import run_doctor
from app.install_engine.report_renderer import render_report
from app.profile.selector import select_profile
from app.setup.app_selector import edit_selection
from app.setup.confirm import confirm
from app.setup.installer import install_selection
from app.setup.summary import render_summary


def run() -> None:
    print()
    print("========================================")
    print("       Buff Helper Setup")
    print("========================================")

    print()
    print("[1/3] Initial diagnosis")
    print()

    run_doctor()

    print()
    print("[2/3] Loading Buff profile")
    print()

    profile = select_profile()
    selection = load_profile(profile)
    selection = edit_selection(selection)

    print(render_summary(selection))
    print()

    if not confirm("Install this profile?"):
        print("Cancelled.")
        return

    report = install_selection(selection)

    print()
    print(render_report(report))

    print()
    print("[3/3] Final diagnosis")
    print()

    run_doctor()

    print()
    print("✓ Setup completed.")
