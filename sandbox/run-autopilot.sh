#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

source .venv/bin/activate

mkdir -p installer/app/generators/templates
touch installer/app/generators/__init__.py

if [ -f tools/generate.py ]; then
    cp tools/generate.py installer/app/generators/engine.py
fi

if [ -f tools/generate_docs.py ]; then
    cp tools/generate_docs.py installer/app/generators/docs.py
fi

if [ -d templates ]; then
    cp -r templates/* installer/app/generators/templates/
fi

cat <<'PY' > tests/test_generators_package.py
from pathlib import Path


def test_generators_package_exists():
    assert Path("installer/app/generators").exists()
    assert Path("installer/app/generators/engine.py").exists()


def test_generator_templates_exist():
    assert Path("installer/app/generators/templates/plugin/plugin.py.j2").exists()
PY

ruff check . --fix
black .
PYTHONPATH=installer pytest

git add installer/app/generators tests/test_generators_package.py

if git diff --cached --quiet; then
    echo "Nothing to commit."
else
    git commit -m "Migrate generators into application package"
    git push
fi

echo
echo "Autopilot completed successfully."
