import json

from app.plugins.storage.checks.timeshift import TimeshiftCheck


class FakeProvider:
    def exists(self, path):
        return True

    def read_text(self, path):
        return json.dumps(
            {
                "btrfs_mode": "true",
                "do_first_run": "false",
                "schedule_daily": "true",
                "count_daily": "7",
                "backup_device_uuid": "123",
            }
        )


def test_timeshift_check():
    assert TimeshiftCheck(FakeProvider()).run().passed
