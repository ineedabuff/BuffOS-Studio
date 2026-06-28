from app.catalog.loader import load_entries


def test_load_catalog_entries():
    entries = load_entries()
    ids = {entry.id for entry in entries}

    assert "firefox" in ids
    assert "chrome" in ids
    assert "vesktop" in ids
    assert "discord" in ids
