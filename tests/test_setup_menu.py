from app.setup.menu import show
from app.setup.questions import Question


def test_menu(capsys):
    show(
        Question(
            id="browser",
            title="Browsers",
            category="browser",
            options=["firefox", "chrome"],
        )
    )

    out = capsys.readouterr().out

    assert "Browsers" in out
    assert "firefox" in out
    assert "chrome" in out
