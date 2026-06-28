from app.checks.base import BaseCheck
from app.plugins.storage.checks import (
    BtrfsCheck,
    GrubBtrfsCheck,
    MountOptionsCheck,
    SubvolumesCheck,
    TimeshiftCheck,
)

CHECKS: list[type[BaseCheck]] = [
    BtrfsCheck,
    SubvolumesCheck,
    MountOptionsCheck,
    TimeshiftCheck,
    GrubBtrfsCheck,
]
