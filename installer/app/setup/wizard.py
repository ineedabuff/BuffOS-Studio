from __future__ import annotations

from app.setup.menu import show
from app.setup.questionnaire import build_questions


def run() -> None:
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("        Linux Setup Assistant")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    for question in build_questions():
        show(question)
