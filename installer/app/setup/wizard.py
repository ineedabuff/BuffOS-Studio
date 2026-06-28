from __future__ import annotations

from pathlib import Path

from app.setup.answers import AnswerSet
from app.setup.confirm import confirm
from app.setup.installer import install_selection
from app.setup.interactive import ask
from app.setup.profile_writer import write_profile
from app.setup.questionnaire import build_questions
from app.setup.resolver import resolve_answers
from app.setup.summary import render_summary


def run() -> None:
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("        Linux Setup Assistant")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    selected: dict[str, list[str]] = {}

    for question in build_questions():
        answers = ask(question)
        selected.update(answers.selected)

    selection = resolve_answers(AnswerSet(selected))

    print()
    print(render_summary(selection))
    print()

    if confirm():
        profile = write_profile(
            selection,
            Path.home() / ".config" / "buff-helper" / "profile.yaml",
        )
        print(f"✓ Profile saved: {profile}")

        install_selection(selection)

        print("✓ Installation completed")
    else:
        print("Installation cancelled")
