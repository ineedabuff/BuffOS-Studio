#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo
echo "==========================================="
echo " Buff Helper Documentation Pack v1"
echo "==========================================="
echo

mkdir -p docs/en
mkdir -p docs/fr
mkdir -p docs/adr
mkdir -p docs/images
mkdir -p docs/reference
mkdir -p docs/tutorials

echo "✓ Documentation tree created"

mkdir -p installer/app/i18n
mkdir -p installer/app/i18n/locales

touch installer/app/i18n/__init__.py

echo "✓ i18n tree created"

echo "{}" > installer/app/i18n/locales/en.json
echo "{}" > installer/app/i18n/locales/fr.json

echo "✓ Locale files created"

echo
echo "Documentation Pack initialized."
