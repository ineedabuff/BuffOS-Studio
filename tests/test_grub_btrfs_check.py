from app.plugins.storage.checks.grub_btrfs import GrubBtrfsCheck


class FakeProvider:
    def which(self, name):
        return "/usr/bin/grub-btrfs"

    def exists(self, path):
        return True


def test_grub_btrfs_check():
    assert GrubBtrfsCheck(FakeProvider()).run().passed
