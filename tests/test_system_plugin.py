from app.plugins.system.plugin import SystemPlugin


def test_system_plugin():
    plugin = SystemPlugin()

    assert plugin.id == "system"
    assert plugin.name == "System"
    assert plugin.description == "System configuration and maintenance plugin"
    assert plugin.version == "0.1.0"

    assert len(plugin.analyses) == 3
