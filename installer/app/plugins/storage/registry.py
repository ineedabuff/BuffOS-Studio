from app.checks.base import BaseCheck
from app.plugins.storage.checks import (
    BtrfsCheck,
    SubvolumesCheck,
)

CHECKS: list[type[BaseCheck]] = [
    BtrfsCheck,
    SubvolumesCheck,
]
