from __future__ import annotations

from app.setup.questions import Question


def show(question: Question) -> None:
    print()
    print(question.title)
    print("-" * len(question.title))
    print()

    for option in question.options:
        print(f"[ ] {option}")

    print()
    print("[n] Next")
    print("[p] Previous")
    print("[q] Quit")
