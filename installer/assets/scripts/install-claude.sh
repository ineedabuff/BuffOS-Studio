#!/usr/bin/env bash
set -euo pipefail

mkdir -p "$HOME/.local/share/applications"

cat > "$HOME/.local/share/applications/claude.desktop" <<DESKTOP
[Desktop Entry]
Name=Claude
Exec=xdg-open https://claude.ai
Type=Application
Categories=Network;AI;
Terminal=false
DESKTOP

echo "✓ Claude launcher installed"
