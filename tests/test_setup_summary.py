from app.catalog.search import find_by_id
from app.setup.selection import Selection
from app.setup.summary import render_summary


def test_render_summary():
    firefox = find_by_id("firefox")
    vesktop = find_by_id("vesktop")

    assert firefox is not None
    assert vesktop is not None

    summary = render_summary(Selection([firefox, vesktop]))

    assert "Firefox" in summary
    assert "Vesktop" in summary
