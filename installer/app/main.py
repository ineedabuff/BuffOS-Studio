from app.core.logger import get_logger
from app.core.runner import Runner
from app.core.ui import print_header
from app.modules.system import SystemCheckModule

logger = get_logger()


def main() -> None:
    print_header()

    runner = Runner()

    runner.register(SystemCheckModule())

    runner.execute()


if __name__ == "__main__":
    main()
