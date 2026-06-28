from app.setup.answers import AnswerSet


def test_answer_set_ids():
    answers = AnswerSet(
        {
            "browser": ["firefox", "chrome"],
            "communication": ["vesktop"],
        }
    )

    assert answers.ids() == [
        "firefox",
        "chrome",
        "vesktop",
    ]
