from app.plugins.storage.checks.subvolumes import SubvolumesCheck


class FakeProvider:
    class Result:
        stdout = """
ID 256 gen 2177 top level 5 path @
ID 257 gen 2178 top level 5 path @home
"""

    def run(self, *args, **kwargs):
        return self.Result()


def test_subvolumes_check():
    result = SubvolumesCheck(FakeProvider()).run()

    assert result.passed is True
    assert result.title == "Btrfs subvolumes"
