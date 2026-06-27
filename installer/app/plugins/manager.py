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
