#!/usr/bin/env bash
set -euo pipefail

echo "== Buff Helper Installer =="

sudo apt update
sudo apt install -y python3 python3-venv python3-pip git

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e .

echo
echo "✓ Buff Helper installed"
echo
echo "Run:"
echo "  source .venv/bin/activate"
echo "  PYTHONPATH=installer python -m app.cli.main doctor"
echo "  PYTHONPATH=installer python -m app.cli.main setup"
