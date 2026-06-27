from app.version import APP_NAME, VERSION


def test_version():
    assert APP_NAME == "BuffOS Studio"
    assert VERSION == "0.2.0-dev"
