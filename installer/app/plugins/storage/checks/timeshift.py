from __future__ import annotations

import json

from app.checks.base import BaseCheck
from app.checks.result import CheckResult
from app.providers.system import SystemProvider


class TimeshiftCheck(BaseCheck):
    id = "timeshift"
    title = "Timeshift"
    category = "storage"

    CONFIG = "/etc/timeshift/timeshift.json"

    def __init__(self, provider: SystemProvider | None = None):
        self.provider = provider or SystemProvider()

    def run(self) -> CheckResult:
        if not self.provider.exists(self.CONFIG):
            return CheckResult(
                id=self.id,
                title=self.title,
                passed=False,
            )

        cfg = json.loads(self.provider.read_text(self.CONFIG))

        passed = (
            cfg.get("btrfs_mode") == "true"
            and cfg.get("do_first_run") == "false"
            and cfg.get("schedule_daily") == "true"
            and cfg.get("count_daily") == "7"
            and bool(cfg.get("backup_device_uuid"))
        )

        return CheckResult(
            id=self.id,
            title=self.title,
            passed=passed,
        )
