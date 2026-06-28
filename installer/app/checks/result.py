from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CheckResult:
    id: str
    title: str
    passed: bool
    fixable: bool = False
    message: str = ""
