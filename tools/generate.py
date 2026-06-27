from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(template: str, **variables: str) -> str:
    text = (ROOT / template).read_text(encoding="utf-8")

    for key, value in variables.items():
        text = text.replace("{{ " + key + " }}", value)

    return text
