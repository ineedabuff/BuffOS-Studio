from __future__ import annotations

from app.setup.answers import AnswerSet
from app.setup.input_parser import parse_selection
from app.setup.questions import Question


def collect_answers(inputs: dict[str, str], questions: list[Question]) -> AnswerSet:
    selected: dict[str, list[str]] = {}

    for question in questions:
        indexes = parse_selection(
            inputs.get(question.id, ""),
            len(question.options),
        )

        selected[question.id] = [question.options[index] for index in indexes]

    return AnswerSet(selected)
