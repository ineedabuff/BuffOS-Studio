from app.catalog.profile_loader import load_profile


def test_load_profile():
    selection = load_profile("buff")

    ids = {entry.id for entry in selection.entries}

    expected = {
        "firefox",
        "vesktop",
        "flatseal",
        "portproton",
        "steam",
        "mangohud",
        "goverlay",
        "gamemode",
        "fastfetch",
        "btop",
        "zsh",
    }

    assert expected <= ids
