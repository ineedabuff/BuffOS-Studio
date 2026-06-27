from app.plugins.manager import PluginManager


def test_plugin_manager_discovers_core_plugin():
    manager = PluginManager()

    manager.discover()

    plugins = manager.all()

    assert len(plugins) >= 1
    assert any(plugin.id == "core" for plugin in plugins)
