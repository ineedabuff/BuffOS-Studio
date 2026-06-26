from app.core.logger import get_logger
from app.core.ui import print_header

logger = get_logger()


def main() -> None:
    print_header()
    logger.info("BuffOS Studio launcher started.")
