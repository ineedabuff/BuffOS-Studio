from app.plugins.storage.checks.mount_options import MountOptionsCheck


class FakeProvider:
    class Result:
        stdout = "rw,noatime,compress=zstd:3,ssd,discard=async,space_cache=v2\n"

    def run(self, *args, **kwargs):
        return self.Result()


def test_mount_options_check():
    result = MountOptionsCheck(FakeProvider()).run()

    assert result.passed is True
    assert result.title == "Btrfs mount options"
