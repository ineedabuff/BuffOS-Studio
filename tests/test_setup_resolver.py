from app.setup.answers import AnswerSet
from app.setup.resolver import resolve_answers


def test_resolve_answers():
    selection = resolve_answers(
        AnswerSet(
            {
                "browser": ["firefox", "chrome"],
                "communication": ["vesktop"],
            }
        )
    )

    assert selection.ids == [
        "firefox",
        "chrome",
        "vesktop",
    ]
