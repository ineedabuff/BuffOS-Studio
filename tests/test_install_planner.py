from app.catalog.search import find_by_id
from app.install_engine.planner import create_plan
from app.setup.selection import Selection


def test_create_plan():
    firefox = find_by_id("firefox")
    vesktop = find_by_id("vesktop")

    assert firefox is not None
    assert vesktop is not None

    plan = create_plan(Selection([firefox, vesktop]))

    assert "org.mozilla.firefox" in plan.flatpak
    assert "dev.vencord.Vesktop" in plan.flatpak
