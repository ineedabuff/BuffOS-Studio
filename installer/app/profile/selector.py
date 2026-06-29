from __future__ import annotations

from app.profile.default import default_profile
from app.profile.list import available_profiles


def select_profile() -> str:
    profiles = available_profiles()
    default = default_profile()

    print()
    print("Available profiles")
    print("------------------")

    for i, profile in enumerate(profiles, start=1):
        marker = " (default)" if profile == default else ""
        print(f"{i}) {profile}{marker}")

    answer = input(f"Profile [{default}]: ").strip()

    if answer == "":
        return default

    if answer.isdigit():
        index = int(answer) - 1

        if 0 <= index < len(profiles):
            return profiles[index]

    if answer in profiles:
        return answer

    return default
