from __future__ import annotations

from app.catalog.search import find_by_id
from app.setup.answers import AnswerSet
from app.setup.selection import Selection


def resolve_answers(answers: AnswerSet) -> Selection:
    entries = []

    for entry_id in answers.ids():
        entry = find_by_id(entry_id)

        if entry is not None:
            entries.append(entry)

    return Selection(entries)
