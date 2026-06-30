from __future__ import annotations

from app.catalog.profile_loader import load_profile
from app.profile.selector import select_profile
from app.setup.selection import Selection


def select_profile_selection() -> Selection:
    profile = select_profile()
    return load_profile(profile)
