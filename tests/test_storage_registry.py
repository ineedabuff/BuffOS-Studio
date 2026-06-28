from app.plugins.storage.checks import (
    BtrfsCheck,
    SubvolumesCheck,
)
from app.plugins.storage.registry import CHECKS


def test_storage_registry():
    assert CHECKS == [
        BtrfsCheck,
        SubvolumesCheck,
    ]
