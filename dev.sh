#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

title() {
    echo
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo " $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo
}

step() {
    echo "▶ $1"
}

done_step() {
    echo "✓ $1"
    echo
}

title "Buff Helper Developer"

if [ -d ".venv" ]; then
    step "Activating virtual environment"
    # shellcheck disable=SC1091
    source ".venv/bin/activate"
    done_step "Virtual environment active"
else
    echo "⚠ .venv not found, using current Python environment"
    echo
fi

step "Running Ruff"
ruff check .
done_step "Ruff passed"

step "Running Black"
black --check .
done_step "Black passed"

step "Running Pytest"
PYTHONPATH=installer pytest
done_step "Pytest passed"

step "Checking CLI"
python -m app version
done_step "CLI works"

title "Ready to code 🚀"
