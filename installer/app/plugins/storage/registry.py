from app.checks.base import BaseCheck
from app.plugins.storage.checks import (
    BtrfsCheck,
    MountOptionsCheck,
    SubvolumesCheck,
)

CHECKS: list[type[BaseCheck]] = [
    BtrfsCheck,
    SubvolumesCheck,
    MountOptionsCheck,
]
