from __future__ import annotations

from app.profile.list import available_profiles


def default_profile() -> str:
    profiles = available_profiles()

    if "buff" in profiles:
        return "buff"

    return profiles[0]
