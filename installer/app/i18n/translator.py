from __future__ import annotations


class Translator:
    def __init__(self, language: str = "en") -> None:
        self.language = language

    def translate(self, key: str) -> str:
        return key


translator = Translator()


def tr(key: str) -> str:
    return translator.translate(key)
