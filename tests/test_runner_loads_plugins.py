from app.core.runner import Runner
from app.plugins.core.plugin import CorePlugin
from app.plugins.manager import PluginManager


def test_runner_loads_plugin_analyses():
    manager = PluginManager()
    manager.register(CorePlugin())

    runner = Runner()
    runner.load(manager)

    assert len(runner.modules) == 9
