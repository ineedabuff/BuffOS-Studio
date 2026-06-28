from app.plugins.storage.checks import (
    BtrfsCheck,
    MountOptionsCheck,
    SubvolumesCheck,
    TimeshiftCheck,
)
from app.plugins.storage.registry import CHECKS


def test_storage_registry():
    assert CHECKS == [
        BtrfsCheck,
        SubvolumesCheck,
        MountOptionsCheck,
        TimeshiftCheck,
    ]
