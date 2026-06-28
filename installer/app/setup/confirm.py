from __future__ import annotations


def confirm(prompt: str = "Installer cette sélection ?") -> bool:
    value = input(f"{prompt} [Y/n] ").strip().lower()

    return value in {
        "",
        "y",
        "yes",
        "o",
        "oui",
    }
