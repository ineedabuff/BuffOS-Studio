from app.catalog.recommendations import recommended


def test_recommended():
    ids = {entry.id for entry in recommended()}

    assert "firefox" in ids
    assert "chrome" in ids
    assert "vesktop" in ids
