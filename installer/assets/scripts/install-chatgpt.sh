#!/usr/bin/env bash
set -euo pipefail

mkdir -p "$HOME/.local/share/applications"

cat > "$HOME/.local/share/applications/chatgpt.desktop" <<DESKTOP
[Desktop Entry]
Name=ChatGPT
Exec=xdg-open https://chatgpt.com
Type=Application
Categories=Network;AI;
Terminal=false
DESKTOP

echo "✓ ChatGPT launcher installed"
