from app.plugins.manifest import PluginManifest
from app.plugins.plugin import Plugin


def test_plugin_manifest():
    manifest = PluginManifest(
        name="core",
        version="1.0.0",
        description="Core plugin",
    )

    plugin = Plugin(manifest=manifest)

    assert plugin.name == "core"
    assert plugin.version == "1.0.0"
    assert plugin.description == "Core plugin"
    assert plugin.enabled is True
