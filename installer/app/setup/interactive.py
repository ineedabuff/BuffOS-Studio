from __future__ import annotations

from app.setup.answers import AnswerSet
from app.setup.input_parser import parse_selection
from app.setup.questions import Question


def ask(question: Question) -> AnswerSet:
    print()
    print(question.title)
    print("-" * len(question.title))

    for index, option in enumerate(question.options, start=1):
        print(f"{index}) {option}")

    print()
    print("Choix: numéros séparés par des espaces, a=tout, Entrée=aucun")
    value = input("> ")

    indexes = parse_selection(value, len(question.options))

    return AnswerSet({question.id: [question.options[index] for index in indexes]})
