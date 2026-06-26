from __future__ import annotations

from time import perf_counter


class Progress:
    def __init__(self) -> None:
        self._start = perf_counter()

    def step(self, current: int, total: int, message: str) -> None:
        print(f"[{current}/{total}] {message}")

    def finish(self) -> None:
        elapsed = perf_counter() - self._start
        print(f"\nCompleted in {elapsed:.2f}s")
