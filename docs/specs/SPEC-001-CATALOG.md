# SPEC-001 - Software Catalog

Chaque logiciel est décrit par une fiche.

Le moteur ne contient aucune liste de logiciels.

Toutes les interfaces (CLI, TUI, GTK, Qt, Calamares, Web) utilisent le catalogue.

## Exemple

id: firefox

name: Firefox

category: browser

install:

  apt: firefox

  flatpak: org.mozilla.firefox

supports:

  ubuntu

  fedora

  arch

doctor:

  command: firefox

apply:

  flatpak

