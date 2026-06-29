#!/usr/bin/env bash
set -euo pipefail

if command -v google-chrome >/dev/null 2>&1; then
    echo "✓ Google Chrome already installed"
    exit 0
fi

tmp="$(mktemp -d)"
cd "$tmp"

wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

cd /
rm -rf "$tmp"
