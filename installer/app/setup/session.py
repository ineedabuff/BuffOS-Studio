from __future__ import annotations

from app.setup.answers import AnswerSet
from app.setup.input_parser import parse_selection
from app.setup.questions import Question


def collect_answer(question: Question, value: str) -> AnswerSet:
    indexes = parse_selection(value, len(question.options))

    return AnswerSet({question.id: [question.options[index] for index in indexes]})
