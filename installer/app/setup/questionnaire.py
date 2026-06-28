from __future__ import annotations

from app.catalog.search import find_by_category
from app.setup.questions import Question


def build_questions() -> list[Question]:
    categories = [
        ("browser", "Choose your web browsers"),
        ("communication", "Choose your communication apps"),
        ("music", "Choose your music applications"),
        ("gaming", "Choose your gaming software"),
        ("development", "Choose your development tools"),
        ("ai", "Choose your AI assistants"),
    ]

    questions: list[Question] = []

    for category, title in categories:
        questions.append(
            Question(
                id=category,
                title=title,
                category=category,
                options=[app.id for app in find_by_category(category)],
            )
        )

    return questions
