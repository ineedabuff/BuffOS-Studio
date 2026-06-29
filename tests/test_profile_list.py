from app.profile.list import available_profiles


def test_available_profiles():
    profiles = available_profiles()

    assert "buff" in profiles
