from app.checks.operating_system import OperatingSystemCheck
from app.modules.base import Module


class SystemCheckModule(Module):
    """Runs system analysis checks."""

    name = "System Check"
    description = "Analyze the current system."

    def run(self):
        return OperatingSystemCheck().run()
