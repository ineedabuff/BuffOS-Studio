from app.plugins.core.plugin import CorePlugin


def test_core_plugin_validators():
    plugin = CorePlugin()

    assert len(plugin.validators) == 4
