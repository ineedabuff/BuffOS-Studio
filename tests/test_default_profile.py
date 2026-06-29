from app.setup.default_profile import load_default_profile


def test_default_profile():
    selection = load_default_profile()

    ids = {entry.id for entry in selection.entries}

    assert "firefox" in ids
    assert "vesktop" in ids
