from app.plugins.storage.checks.btrfs import BtrfsCheck


class FakeProvider:
    class Result:
        stdout = "btrfs\n"

    def run(self, *args, **kwargs):
        return self.Result()


def test_btrfs_check():
    result = BtrfsCheck(FakeProvider()).run()

    assert result.passed is True
    assert result.title == "Btrfs"
