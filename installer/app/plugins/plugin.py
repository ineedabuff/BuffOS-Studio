from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Plugin:
    name: str
    description: str = ""
    analyses: list[Any] = field(default_factory=list)
    validators: list[Any] = field(default_factory=list)
    installers: list[Any] = field(default_factory=list)
    commands: list[Any] = field(default_factory=list)
    learn_topics: list[Any] = field(default_factory=list)
