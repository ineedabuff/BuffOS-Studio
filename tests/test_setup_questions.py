from app.setup.questions import Question


def test_question_model():
    question = Question(
        id="browser",
        title="Choose your browsers",
        category="browser",
        options=["firefox", "chrome"],
    )

    assert question.id == "browser"
    assert question.multiple
    assert "firefox" in question.options
