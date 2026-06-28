# Linux Setup Assistant

## Mission

Linux Setup Assistant est un moteur universel permettant de construire, personnaliser, réparer et faire évoluer une installation GNU/Linux.

Il peut fonctionner :

- après une installation Linux
- pendant une installation via Calamares
- plusieurs mois après l'installation
- sur plusieurs distributions

Le moteur est entièrement piloté par un catalogue.

Le code ne contient jamais de liste de logiciels.

Toutes les applications, bundles, profils et recommandations proviennent du catalogue.

---

# Architecture

Core Engine

- Catalog Engine
- Profile Engine
- Detection Engine
- Recommendation Engine
- Installation Engine
- Doctor Engine
- Configuration Engine
- Marketplace Engine

---

# Interfaces

- CLI
- TUI
- GTK
- Qt
- Calamares
- Web

Toutes utilisent exactement le même moteur.

---

# Plugins

Une distribution fournit simplement un plugin.

Exemples :

- Ubuntu
- Kubuntu
- Fedora
- Arch
- Debian
- openSUSE
- CachyOS

---

# Catalog

Le catalogue décrit :

- applications
- bundles
- profils
- matériels
- bureaux
- distributions

---

# Philosophy

Le moteur ne connaît jamais les logiciels.

Il ne connaît que le catalogue.
