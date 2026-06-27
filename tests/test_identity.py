from app.identity import APP_CLI, APP_NAME, TAGLINE, VERSION


def test_identity():
    assert APP_NAME == "Buff Helper"
    assert APP_CLI == "buff"
    assert VERSION == "0.3.0-dev"
    assert TAGLINE == "Analyze. Repair. Optimize."
