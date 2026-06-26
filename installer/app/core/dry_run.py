from __future__ import annotations

from app.install.installation_plan import InstallationPlan


class DryRun:
    def show(self, plan: InstallationPlan) -> None:
        print()
        print("Planned actions")
        print("----------------")

        installers = plan.all()

        if not installers:
            print("Nothing to do.")
            return

        for installer in installers:
            print(f"• {installer.description}")
