from app.catalog.search import find_by_id
from app.setup.selection import Selection


def test_selection_ids():
    firefox = find_by_id("firefox")

    assert firefox is not None
    assert Selection([firefox]).ids == ["firefox"]
