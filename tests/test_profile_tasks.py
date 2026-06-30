from app.profile.tasks import profile_tasks


def test_profile_tasks():
    tasks = profile_tasks("buff")

    assert "install-buff-term.sh" in tasks
    assert "install-buff-zsh.sh" in tasks
    assert "install-buff-extras.sh" in tasks
