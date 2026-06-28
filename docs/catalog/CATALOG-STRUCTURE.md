# Catalog Structure

Linux Setup Assistant is catalog-first.

The engine does not hardcode applications.

## Main folders

installer/catalog/
  applications/
  bundles/
  profiles/
  hardware/
  desktop/
  distributions/

## Rule

Applications describe software.
Bundles group applications.
Profiles combine bundles, applications, hardware, desktop and preferences.
Plugins know how to install/configure for each distribution.

