from app.plugins.core.plugin import CorePlugin


def test_core_plugin():
    plugin = CorePlugin()

    assert plugin.name == "core"
    assert plugin.description == "Core Buff Helper plugin"

    assert len(plugin.analyses) == 9
    assert len(plugin.validators) == 4

    assert plugin.installers == []
    assert plugin.commands == []
    assert plugin.learn_topics == []
