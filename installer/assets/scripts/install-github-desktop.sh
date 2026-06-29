#!/usr/bin/env bash
set -euo pipefail

if flatpak info io.github.shiftey.Desktop >/dev/null 2>&1; then
    echo "✓ GitHub Desktop already installed"
    exit 0
fi

flatpak install -y flathub io.github.shiftey.Desktop
