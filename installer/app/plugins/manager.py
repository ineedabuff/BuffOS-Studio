from __future__ import annotations

import importlib
import pkgutil

import app.plugins
from app.plugins.plugin import Plugin


class PluginManager:
    def __init__(self) -> None:
        self._plugins: list[Plugin] = []

    def register(self, plugin: Plugin) -> None:
        self._plugins.append(plugin)

    def discover(self) -> None:
        for module_info in pkgutil.iter_modules(app.plugins.__path__):
            if module_info.name.startswith("_"):
                continue

            module_name = f"app.plugins.{module_info.name}.plugin"

            try:
                module = importlib.import_module(module_name)
            except ModuleNotFoundError:
                continue

            plugin_class = getattr(module, "PLUGIN", None)

            if plugin_class is None:
                continue

            self.register(plugin_class())

    def all(self) -> list[Plugin]:
        return self._plugins

    def analyses(self) -> list[object]:
        analyses: list[object] = []

        for plugin in self._plugins:
            analyses.extend(plugin.analyses)

        return analyses

    def validators(self) -> list[object]:
        validators: list[object] = []

        for plugin in self._plugins:
            validators.extend(plugin.validators)

        return validators

    def installers(self) -> list[object]:
        installers: list[object] = []

        for plugin in self._plugins:
            installers.extend(plugin.installers)

        return installers

    def commands(self) -> list[object]:
        commands: list[object] = []

        for plugin in self._plugins:
            commands.extend(plugin.commands)

        return commands

    def learn_topics(self) -> list[object]:
        topics: list[object] = []

        for plugin in self._plugins:
            topics.extend(plugin.learn_topics)

        return topics
