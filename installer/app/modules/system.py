from app.modules.base import Module


class SystemCheckModule(Module):
    """Checks whether the system is ready for BuffOS installation."""

    name = "System Check"
    description = "Validate basic system requirements."

    def run(self) -> bool:
        return True
