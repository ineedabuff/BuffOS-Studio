from app.version import APP_NAME, VERSION


def test_version():
    assert APP_NAME == "Buff Helper"
    assert VERSION == "0.3.0-dev"
