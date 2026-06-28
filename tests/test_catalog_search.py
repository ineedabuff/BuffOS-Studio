from app.catalog.search import all_categories, find_by_category, find_by_id


def test_find_by_id():
    entry = find_by_id("firefox")

    assert entry is not None
    assert entry.name == "Firefox"


def test_find_by_category():
    entries = find_by_category("browser")
    ids = {entry.id for entry in entries}

    assert "firefox" in ids
    assert "chrome" in ids


def test_all_categories():
    assert "browser" in all_categories()
    assert "communication" in all_categories()
