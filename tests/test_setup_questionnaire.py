from app.setup.questionnaire import build_questions


def test_build_questions():
    questions = build_questions()

    ids = {question.id for question in questions}

    assert "browser" in ids
    assert "communication" in ids

    browser = next(q for q in questions if q.id == "browser")

    assert "firefox" in browser.options
    assert "chrome" in browser.options
