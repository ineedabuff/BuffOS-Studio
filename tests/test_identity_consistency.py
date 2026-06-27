from app.identity import APP_CLI, APP_NAME


def test_identity_consistency():
    assert APP_CLI == "buff"
    assert APP_NAME == "Buff Helper"
