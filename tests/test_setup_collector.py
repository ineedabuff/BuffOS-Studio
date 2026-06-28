from app.setup.collector import collect_answers
from app.setup.questions import Question


def test_collect_answers():
    questions = [
        Question(
            id="browser",
            title="Browsers",
            category="browser",
            options=["firefox", "chrome"],
        ),
        Question(
            id="communication",
            title="Communication",
            category="communication",
            options=["vesktop", "discord"],
        ),
    ]

    answers = collect_answers(
        {
            "browser": "1 2",
            "communication": "1",
        },
        questions,
    )

    assert answers.selected == {
        "browser": ["firefox", "chrome"],
        "communication": ["vesktop"],
    }
