from app.profile.default import default_profile


def test_default_profile():
    assert default_profile() == "buff"
