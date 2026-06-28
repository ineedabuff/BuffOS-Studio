from app.plugins.terminal.plugin import TerminalPlugin


def test_terminal_plugin():
    plugin = TerminalPlugin()

    assert plugin.id == "terminal"
    assert plugin.name == "Terminal"
    assert plugin.version == "0.1.0"
    assert plugin.description == "Buff terminal and shell customization plugin"
