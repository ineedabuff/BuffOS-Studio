from unittest.mock import patch

from app.setup.interactive import ask
from app.setup.questions import Question


def test_ask():
    question = Question(
        id="browser",
        title="Browsers",
        category="browser",
        options=["firefox", "chrome"],
    )

    with patch("builtins.input", return_value="1"):
        answers = ask(question)

    assert answers.selected == {
        "browser": ["firefox"],
    }
