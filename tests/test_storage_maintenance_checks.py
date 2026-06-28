from app.plugins.storage.checks.balance import BalanceCheck
from app.plugins.storage.checks.btrfsmaintenance import BtrfsMaintenanceCheck
from app.plugins.storage.checks.fstrim import FstrimCheck
from app.plugins.storage.checks.scrub import ScrubCheck


class FakeProvider:
    class Result:
        stdout = "enabled\n"

    def run(self, *args, **kwargs):
        return self.Result()

    def exists(self, path):
        return True

    def read_text(self, path):
        return """
BTRFS_SCRUB_PERIOD="monthly"
BTRFS_BALANCE_MOUNTPOINTS="/"
"""


def test_storage_checks():
    provider = FakeProvider()

    assert FstrimCheck(provider).run().passed
    assert ScrubCheck(provider).run().passed
    assert BalanceCheck(provider).run().passed
    assert BtrfsMaintenanceCheck(provider).run().passed
