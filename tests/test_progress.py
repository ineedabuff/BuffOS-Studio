from app.core.progress import Progress


def test_progress(capsys):
    progress = Progress()

    progress.step(1, 4, "Analyzing")
    progress.step(2, 4, "Validating")
    progress.finish()

    out = capsys.readouterr().out

    assert "[1/4] Analyzing" in out
    assert "[2/4] Validating" in out
    assert "Completed in" in out
