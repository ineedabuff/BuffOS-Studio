from app.setup.questions import Question
from app.setup.session import collect_answer


def test_collect_answer():
    question = Question(
        id="browser",
        title="Choose your browsers",
        category="browser",
        options=["firefox", "chrome", "brave"],
    )

    answers = collect_answer(question, "1 3")

    assert answers.selected == {
        "browser": [
            "firefox",
            "brave",
        ]
    }
