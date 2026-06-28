#!/usr/bin/env bash
set -euo pipefail

echo "== Buff Helper Installer =="

sudo apt update
sudo apt install -y python3 python3-venv python3-pip git

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip

chmod +x buff-helper

echo
echo "✓ Buff Helper installed"
echo
echo "Run:"
echo "  ./buff-helper doctor"
echo "  ./buff-helper setup"
echo "  ./buff-helper wizard"
