from __future__ import annotations

from app.plugins.plugin import Plugin


class PluginManager:
    def __init__(self) -> None:
        self._plugins: list[Plugin] = []

    def register(self, plugin: Plugin) -> None:
        self._plugins.append(plugin)

    def all(self) -> list[Plugin]:
        return self._plugins

    def analyses(self) -> list[object]:
        return [analysis for plugin in self._plugins for analysis in plugin.analyses]

    def validators(self) -> list[object]:
        return [
            validator for plugin in self._plugins for validator in plugin.validators
        ]

    def installers(self) -> list[object]:
        return [
            installer for plugin in self._plugins for installer in plugin.installers
        ]

    def commands(self) -> list[object]:
        return [command for plugin in self._plugins for command in plugin.commands]

    def learn_topics(self) -> list[object]:
        return [topic for plugin in self._plugins for topic in plugin.learn_topics]
