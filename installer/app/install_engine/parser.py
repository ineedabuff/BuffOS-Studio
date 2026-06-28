from __future__ import annotations


def read_yaml_value(text: str, key: str) -> str:
    lines = text.splitlines()

    for index, line in enumerate(lines):
        if line.strip() == "install:":
            for child in lines[index + 1 :]:
                if child and not child.startswith(" "):
                    break

                stripped = child.strip()
                prefix = f"{key}:"

                if stripped.startswith(prefix):
                    return stripped.replace(prefix, "", 1).strip()

    return ""
