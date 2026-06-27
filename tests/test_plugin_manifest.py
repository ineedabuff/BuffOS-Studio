from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


def test_plugin_manifest():
    manifest = PluginManifest(
        id="core",
        name="Core",
        version="1.0.0",
        description="Core plugin",
    )

    plugin = Plugin(manifest=manifest)

    assert plugin.id == "core"
    assert plugin.name == "Core"
    assert plugin.version == "1.0.0"
    assert plugin.description == "Core plugin"
    assert plugin.author == "Buff Helper Project"
    assert plugin.license == "MIT"
    assert plugin.enabled is True
