from app.plugins.manager import PluginManager
from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


def test_plugin_manager_registers_plugins():
    manager = PluginManager()
    plugin = Plugin(
        manifest=PluginManifest(
            name="core",
            version="1.0.0",
            description="Core plugin",
        )
    )

    manager.register(plugin)

    assert manager.all() == [plugin]


def test_plugin_manager_collects_plugin_items():
    analysis = object()
    validator = object()
    installer = object()
    command = object()
    topic = object()

    plugin = Plugin(
        manifest=PluginManifest(
            name="core",
            version="1.0.0",
            description="Core plugin",
        ),
        analyses=[analysis],
        validators=[validator],
        installers=[installer],
        commands=[command],
        learn_topics=[topic],
    )

    manager = PluginManager()
    manager.register(plugin)

    assert manager.analyses() == [analysis]
    assert manager.validators() == [validator]
    assert manager.installers() == [installer]
    assert manager.commands() == [command]
    assert manager.learn_topics() == [topic]
