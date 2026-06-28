from __future__ import annotations

from app.plugins.storage.registry import CHECKS


class Doctor:
    def run(self):
        results = []

        for check_cls in CHECKS:
            check = check_cls()
            results.append(check.run())

        return results
