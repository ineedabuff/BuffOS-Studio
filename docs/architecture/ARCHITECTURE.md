# Linux Setup Assistant Architecture

## Core

Le Core ne connaît aucun logiciel.

Il ne connaît que :

- Catalog
- Profiles
- Plugins
- Rules
- Hardware
- Desktop
- Distribution

---

## Catalog

Décrit les logiciels.

Exemple :

Chrome

Firefox

Steam

Spotify

...

---

## Profiles

Regroupent des logiciels.

Exemple :

Gaming

Developer

Creator

Journalist

Privacy

---

## Plugins

Chaque plugin ajoute des capacités.

Plugin NVIDIA

Plugin KDE

Plugin Ubuntu

Plugin Fedora

Plugin Btrfs

Plugin Gaming

---

## UI

Toutes les interfaces utilisent le même moteur.

CLI

TUI

GTK

Qt

Calamares

Web

---

## Engine

Catalog Engine

↓

Recommendation Engine

↓

Dependency Engine

↓

Installation Engine

↓

Configuration Engine

↓

Doctor Engine

↓

Repair Engine
