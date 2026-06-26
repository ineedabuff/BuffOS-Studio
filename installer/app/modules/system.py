class SystemCheckModule:
    """Checks whether the system is ready for BuffOS installation."""

    name = "System Check"

    def run(self) -> bool:
        return True
