from __future__ import annotations


def parse_selection(value: str, maximum: int) -> list[int]:
    value = value.strip().lower()

    if value in {"", "n", "next"}:
        return []

    if value in {"a", "all"}:
        return list(range(maximum))

    selected: list[int] = []

    for part in value.replace(",", " ").split():
        if not part.isdigit():
            continue

        index = int(part) - 1

        if 0 <= index < maximum:
            selected.append(index)

    return selected
