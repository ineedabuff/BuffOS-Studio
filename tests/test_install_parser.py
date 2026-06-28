from app.install_engine.parser import read_yaml_value


def test_read_yaml_value():
    text = """
id: firefox
install:
  apt: firefox
  flatpak: org.mozilla.firefox
"""

    assert read_yaml_value(text, "apt") == "firefox"
    assert read_yaml_value(text, "flatpak") == "org.mozilla.firefox"
    assert read_yaml_value(text, "script") == ""
