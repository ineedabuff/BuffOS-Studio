from app.setup.wizard import run


def test_setup_wizard():
    assert callable(run)
