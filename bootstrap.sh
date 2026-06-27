#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Buff Helper Bootstrap"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo

if [ ! -d ".venv" ]; then
    echo "▶ Creating virtual environment"
    python -m venv .venv
    echo "✓ Virtual environment created"
    echo
fi

# shellcheck disable=SC1091
source ".venv/bin/activate"

echo "▶ Upgrading pip"
python -m pip install --upgrade pip
echo "✓ pip upgraded"
echo

echo "▶ Installing development dependencies"
pip install -r requirements-dev.txt
echo "✓ Dependencies installed"
echo

echo "▶ Installing Buff Helper editable package"
pip install -e .
echo "✓ Editable install complete"
echo

echo "▶ Running validation"
./dev.sh
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Buff Helper is ready 🚀"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
